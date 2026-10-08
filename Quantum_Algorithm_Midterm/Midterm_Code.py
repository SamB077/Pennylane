import numpy as np
import pennylane as qml
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from lamberthub import izzo2015
import time
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

MU_SUN = 1.32712440018e11  # km^3 / s^2
R_EARTH = 1.496e8          # km  (1 AU)
R_MARS = 2.279e8           # km  (1.524 AU)
DAY = 86400.0              # s

N_LAUNCH = 32 
N_TOF = 32      
N_QUBITS = 10   # 32 * 32 = 1024 = 2**10 candidates
N_CANDIDATES = N_LAUNCH * N_TOF

LAUNCH_WINDOW_DAYS = np.linspace(-50, 830, N_LAUNCH)  
TOF_WINDOW_DAYS = np.linspace(100, 900, N_TOF)       

VIZ_N_LAUNCH = 300
VIZ_N_TOF = 300
VIZ_PROGRESS_EVERY = 2000

N_EARTH = np.sqrt(MU_SUN / R_EARTH**3)
N_MARS = np.sqrt(MU_SUN / R_MARS**3)
V_EARTH = np.sqrt(MU_SUN / R_EARTH)
V_MARS = np.sqrt(MU_SUN / R_MARS)

PHASE_EARTH_0 = 0.0
PHASE_MARS_0 = np.deg2rad(44.5)  

def planet_state(theta, radius, speed):
    """Circular-orbit position (km) and velocity (km/s), z=0."""
    pos = radius * np.array([np.cos(theta), np.sin(theta), 0.0])
    vel = speed * np.array([-np.sin(theta), np.cos(theta), 0.0])
    return pos, vel

def transfer_delta_v(launch_day, tof_days):
    """Total delta-v (km/s) for one Earth->Mars Lambert transfer."""
    t_launch = launch_day * DAY
    tof = tof_days * DAY

    theta_e = PHASE_EARTH_0 + N_EARTH * t_launch
    theta_m = PHASE_MARS_0 + N_MARS * (t_launch + tof)

    r1, v_earth = planet_state(theta_e, R_EARTH, V_EARTH)
    r2, v_mars = planet_state(theta_m, R_MARS, V_MARS)

    try:
        v1, v2 = izzo2015(MU_SUN, r1, r2, tof, M=0, prograde=True)
    except Exception:
        return np.inf

    dv_departure = np.linalg.norm(np.array(v1) - v_earth)
    dv_arrival = np.linalg.norm(np.array(v2) - v_mars)
    return dv_departure + dv_arrival

def build_lambert_cost_grid():
    print(f"Evaluating {N_CANDIDATES} Lambert transfers...")
    t0 = time.time()
    costs = np.zeros(N_CANDIDATES)
    for i, ld in enumerate(LAUNCH_WINDOW_DAYS):
        for j, tof in enumerate(TOF_WINDOW_DAYS):
            costs[i * N_TOF + j] = transfer_delta_v(ld, tof)
    finite_max = np.max(costs[np.isfinite(costs)])
    costs[~np.isfinite(costs)] = finite_max * 10  # penalize non-converged geometry
    print(f"Done in {time.time()-t0:.2f}s "
          f"(compare to your N-body version's per-candidate physics loop).")
    return costs

def build_fine_cost_grid(n_launch=VIZ_N_LAUNCH, n_tof=VIZ_N_TOF):
    launch_days = np.linspace(LAUNCH_WINDOW_DAYS[0], LAUNCH_WINDOW_DAYS[-1], n_launch)
    tof_days = np.linspace(TOF_WINDOW_DAYS[0], TOF_WINDOW_DAYS[-1], n_tof)
    total = n_launch * n_tof

    print(f"Evaluating {total} Lambert transfers for the fine 3D cost surface "
          f"({n_launch} x {n_tof})...")
    t0 = time.time()
    costs = np.zeros(total)
    done = 0
    for i, ld in enumerate(launch_days):
        for j, tof in enumerate(tof_days):
            costs[i * n_tof + j] = transfer_delta_v(ld, tof)
            done += 1
            if done % VIZ_PROGRESS_EVERY == 0 or done == total:
                pct = 100 * done / total
                print(f"  {done}/{total} ({pct:.0f}%) -- elapsed {time.time()-t0:.1f}s")

    finite_max = np.max(costs[np.isfinite(costs)])
    costs[~np.isfinite(costs)] = finite_max * 10
    print(f"Fine grid done in {time.time()-t0:.1f}s.")
    return launch_days, tof_days, costs.reshape(n_launch, n_tof)


def plot_cost_surface(launch_days, tof_days, cost_grid, highlight_points=None,
                       save_path=None):

    if save_path is None:
        save_path = os.path.join(SCRIPT_DIR, "lambert_cost_surface_v2.png")
    TOF, LAUNCH = np.meshgrid(tof_days, launch_days)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")
    surf = ax.plot_surface(TOF, LAUNCH, cost_grid, cmap="viridis",
                            linewidth=0, antialiased=True, alpha=0.95)
    fig.colorbar(surf, ax=ax, shrink=0.6, label="Total delta-v (km/s)")

    if highlight_points:
        for tof, launch_day, cost, label, color in highlight_points:
            ax.scatter([tof], [launch_day], [cost], color=color, s=120,
                       edgecolors="black", linewidths=0.8, label=label, zorder=10)
        ax.legend()

    ax.set_xlabel("Time of flight (days)")
    ax.set_ylabel("Launch day")
    ax.set_zlabel("Total delta-v (km/s)")
    ax.set_title(f"Earth-Mars Lambert delta-v landscape "
                 f"({cost_grid.shape[0]}x{cost_grid.shape[1]} fine grid)")
    ax.view_init(elev=35, azim=-50)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    print(f"Saved 3D cost-surface plot to {save_path}")


DH_MAX_ITERATIONS = 40
DH_LAMBDA = 1.2
DH_MAX_M_CAP = 8

PRINT_EVERY_ITERATION = 1


def run_durr_hoyer(costs, n_qubits, seed=0):

    n_candidates = len(costs)
    dim = 2 ** n_qubits
    costs_diag = np.full(dim, fill_value=float(costs.max()) * 2.0)
    costs_diag[:n_candidates] = costs
    wires = list(range(n_qubits))

    dev = qml.device("default.qubit", wires=n_qubits)

    def oracle_diag(threshold_cost):
        return np.where(costs_diag < threshold_cost, -1.0, 1.0).astype(complex)

    @qml.qnode(dev)
    def grover_search(threshold_cost, n_iterations):
        for w in wires:
            qml.Hadamard(wires=w)
        marks = oracle_diag(threshold_cost)
        for _ in range(n_iterations):
            qml.DiagonalQubitUnitary(marks, wires=wires)
            qml.GroverOperator(wires=wires)
        return qml.probs(wires=wires)

    print(f"Starting Durr-Hoyer quantum minimum search "
          f"({n_qubits} qubits, up to {DH_MAX_ITERATIONS} iterations, "
          f"max_m capped at {DH_MAX_M_CAP})...")
    t0 = time.time()

    np.random.seed(seed)
    y = np.random.randint(0, n_candidates)
    best_cost = costs[y]
    m_sched = 1.0
    oracle_calls = 0
    history = []

    for it in range(DH_MAX_ITERATIONS):
        j = np.random.randint(0, max(1, int(np.ceil(m_sched))))
        probs = grover_search(best_cost, j)
        oracle_calls += j
        y_prime = int(np.random.choice(len(probs), p=np.asarray(probs) / np.sum(probs)))

        measured_cost = costs[y_prime] if y_prime < n_candidates else float("inf")
        improved = y_prime < n_candidates and measured_cost < best_cost

        if improved:
            y = y_prime
            best_cost = costs[y]
            m_sched = 1.0
        else:
            m_sched = min(DH_LAMBDA * m_sched, DH_MAX_M_CAP)

        history.append({
            "iteration": it + 1, "j": j, "measured_idx": y_prime,
            "measured_cost": measured_cost, "best_cost": best_cost,
            "improved": improved, "m_sched": m_sched,
            "oracle_calls_cumulative": oracle_calls, "elapsed": time.time() - t0,
        })

        if PRINT_EVERY_ITERATION and (it + 1) % PRINT_EVERY_ITERATION == 0:
            flag = " <- improved" if improved else ""
            print(f"    it {it+1:2d}/{DH_MAX_ITERATIONS}: j={j:2d}  "
                  f"measured cost={measured_cost:9.4f}  "
                  f"best so far={best_cost:9.4f} km/s{flag}  "
                  f"(m={m_sched:4.2f}, oracle calls so far={oracle_calls})")

        if (it + 1) % 10 == 0 or (it + 1) == DH_MAX_ITERATIONS:
            print(f"  --- checkpoint: iteration {it+1}/{DH_MAX_ITERATIONS}, "
                  f"best cost so far = {best_cost:.4f} km/s "
                  f"(elapsed {time.time()-t0:.2f}s) ---")

    return y, best_cost, oracle_calls, history


def plot_convergence(history, classical_min, save_path=None):

    if save_path is None:
        save_path = os.path.join(SCRIPT_DIR, "lambert_durrhoyer_convergence.png")
    iters = [h["iteration"] for h in history]
    best = [h["best_cost"] for h in history]
    m_sched = [h["m_sched"] for h in history]
    improved_iters = [h["iteration"] for h in history if h["improved"]]
    improved_best = [h["best_cost"] for h in history if h["improved"]]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 7), sharex=True)

    ax1.step(iters, best, where="post", color="tab:blue", label="Best cost so far (quantum search)")
    ax1.scatter(improved_iters, improved_best, color="tab:blue", zorder=5, label="Improvement found")
    ax1.axhline(classical_min, color="tab:red", linestyle="--", label="Classical brute-force minimum")
    ax1.set_ylabel("Best total delta-v (km/s)")
    ax1.set_title("Durr-Hoyer search convergence")
    ax1.legend()
    ax1.grid(alpha=0.3)

    ax2.step(iters, m_sched, where="post", color="tab:green")
    ax2.scatter(improved_iters, [1] * len(improved_iters), color="tab:blue", marker="|", s=200, label="Improvement (m resets to 1)")
    ax2.set_xlabel("Iteration")
    ax2.set_ylabel("Schedule parameter m")
    ax2.set_title("Grover-iteration schedule (grows after no improvement, resets on improvement)")
    ax2.legend()
    ax2.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    print(f"Saved convergence plot to {save_path}")


def print_results_table(c_min, c_idx, q_min, q_idx, calls, n_candidates, launch_days, tof_days, n_tof):
    """Prints a plain-text version of the report's Table so the numbers
    can be copied"""
    c_launch_i, c_tof_j = divmod(c_idx, n_tof)
    q_launch_i, q_tof_j = divmod(q_idx, n_tof)
    correct = bool(np.isclose(q_min, c_min))

    rows = [
        ("Best total delta-v (km/s)", f"{c_min:.4f}", f"{q_min:.4f}"),
        ("Launch day / TOF (days)",
         f"{launch_days[c_launch_i]:.1f} / {tof_days[c_tof_j]:.1f}",
         f"{launch_days[q_launch_i]:.1f} / {tof_days[q_tof_j]:.1f}"),
        ("Number of cost evaluations", f"{n_candidates} (full grid)", f"~{calls} (oracle calls)"),
        ("Correct minimum recovered?", "-", "Yes" if correct else "No"),
    ]
    w0 = max(len(r[0]) for r in rows) + 2
    w1 = max(len(r[1]) for r in rows) + 2
    w2 = max(len(r[2]) for r in rows) + 2
    header = ("Quantity".ljust(w0) + "Classical brute force".ljust(w1) + "Durr-Hoyer (quantum)".ljust(w2))
    print("\n--- Table 1 (copy into the report) ---")
    print(header)
    print("-" * len(header))
    for label, c_val, q_val in rows:
        print(label.ljust(w0) + c_val.ljust(w1) + q_val.ljust(w2))
    print()


if __name__ == "__main__":
    costs = build_lambert_cost_grid()
    c_idx = int(np.argmin(costs))
    c_min = costs[c_idx]
    print(f"Classical brute-force min = {c_min:.4f} km/s at index {c_idx}\n")

    q_idx, q_min, calls, history = run_durr_hoyer(costs, N_QUBITS, seed=42)

    print("\n--- Results ---")
    print(f"Classical brute-force min : {c_min:.4f} km/s at index {c_idx} "
          f"({N_CANDIDATES} full evaluations)")
    print(f"Durr-Hoyer quantum result : {q_min:.4f} km/s at index {q_idx} "
          f"(~{calls} oracle queries)")
    print(f"Correct minimum found     : {np.isclose(q_min, c_min)}")

    launch_i, tof_j = divmod(q_idx, N_TOF)
    c_launch_i, c_tof_j = divmod(c_idx, N_TOF)
    print(f"\nBest transfer -> launch day {LAUNCH_WINDOW_DAYS[launch_i]:.1f}, "
          f"time of flight {TOF_WINDOW_DAYS[tof_j]:.1f} days, "
          f"delta-v {q_min:.4f} km/s")

    print_results_table(c_min, c_idx, q_min, q_idx, calls, N_CANDIDATES, LAUNCH_WINDOW_DAYS, TOF_WINDOW_DAYS, N_TOF)

    grid = costs.reshape(N_LAUNCH, N_TOF)
    plt.figure(figsize=(8, 6))
    plt.imshow(grid, origin="lower", aspect="auto", extent=[TOF_WINDOW_DAYS[0], TOF_WINDOW_DAYS[-1],
                       LAUNCH_WINDOW_DAYS[0], LAUNCH_WINDOW_DAYS[-1]], cmap="viridis")
    plt.colorbar(label="Total delta-v (km/s)")
    plt.scatter(TOF_WINDOW_DAYS[tof_j], LAUNCH_WINDOW_DAYS[launch_i], c="red", marker="*", s=220, edgecolors="white", linewidths=0.8, label="Durr-Hoyer result", zorder=5)
    plt.scatter(TOF_WINDOW_DAYS[c_tof_j], LAUNCH_WINDOW_DAYS[c_launch_i], facecolors="none", edgecolors="white", marker="o", s=260, linewidths=1.5, label="Classical minimum", zorder=5)
    plt.xlabel("Time of flight (days)")
    plt.ylabel("Launch day")
    plt.title("Earth-Mars Lambert delta-v grid (porkchop-style)")
    plt.legend()
    plt.tight_layout()
    porkchop_path = os.path.join(SCRIPT_DIR, "lambert_durrhoyer_result.png")
    plt.savefig(porkchop_path, dpi=150)
    print(f"Saved plot to {porkchop_path}")

    plot_convergence(history, c_min)

    fine_launch_days, fine_tof_days, fine_grid = build_fine_cost_grid()
    fine_min_idx = np.unravel_index(np.argmin(fine_grid), fine_grid.shape)
    fine_min_launch = fine_launch_days[fine_min_idx[0]]
    fine_min_tof = fine_tof_days[fine_min_idx[1]]
    fine_min_cost = fine_grid[fine_min_idx]
    print(f"\nFine-grid minimum          : {fine_min_cost:.4f} km/s at "
          f"launch day {fine_min_launch:.1f}, TOF {fine_min_tof:.1f} days "
          f"(for reference -- this grid is independent of the 32x32 search grid)")

    q_launch_day = LAUNCH_WINDOW_DAYS[launch_i]
    q_tof = TOF_WINDOW_DAYS[tof_j]
    c_launch_day = LAUNCH_WINDOW_DAYS[c_launch_i]
    c_tof = TOF_WINDOW_DAYS[c_tof_j]
    highlight_points = [(c_tof, c_launch_day, transfer_delta_v(c_launch_day, c_tof), "Classical minimum (search grid)", "red"),
        (q_tof, q_launch_day, transfer_delta_v(q_launch_day, q_tof), "Durr-Hoyer result (search grid)", "orange"),
        (fine_min_tof, fine_min_launch, fine_min_cost,"Fine-grid minimum", "white"),
    ]
    plot_cost_surface(fine_launch_days, fine_tof_days, fine_grid, highlight_points=highlight_points)
