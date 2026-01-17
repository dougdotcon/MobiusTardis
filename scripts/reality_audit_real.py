
import numpy as np
import matplotlib.pyplot as plt

# --- TARDIS THEORETICAL CONSTANTS ---
OMEGA = 117.038
# Theoretical Hubble: Based on pure geometric expansion of a Möbius Manifold
# H_theo = Omega / sqrt(3) (Geometric Geometric mean of 3 dimensions)
H_THEO = OMEGA / np.sqrt(3) 

# --- OBSERVED REALITY (Planck 2018) ---
H_OBS = 67.4 
H_UNCERTAINTY = 0.5 

def audit_reality():
    print(f"--- COSMIC REALITY AUDIT ---")
    print(f"Target: Planck 2018 Data vs TARDIS Theory")
    
    print(f"\n[1] Theoretical Baseline (Origin Universe)")
    print(f"    Omega: {OMEGA}")
    print(f"    Predicted H0: {H_THEO:.4f} km/s/Mpc")
    
    print(f"\n[2] Observational Data (Current Reality)")
    print(f"    Observed H0: {H_OBS} +/- {H_UNCERTAINTY} km/s/Mpc")
    
    # Calculate Discrepancy
    delta = H_THEO - H_OBS
    print(f"\n[3] Analysis")
    print(f"    Entropic Decay (Delta): {delta:.4f}")
    
    # Branch Calculation
    # Hypothesis: Each branch drops H0 by ~0.15 due to information loss
    branch_penalty = 0.15
    branch_depth = delta / branch_penalty
    
    print(f"    Estimated Branch Depth: {branch_depth:.2f}")
    
    # Conclusion
    if abs(delta) < H_UNCERTAINTY:
        status = "ORIGIN TIMELINE (confirmed within error bars)"
        color = 'green'
    elif branch_depth < 1.5:
        status = "BRANCH 1 (First Copy)"
        color = 'orange'
    else:
        status = f"BRANCH {int(round(branch_depth))} (Deep Copy)"
        color = 'red'
        
    print(f"\n>>> FINAL VERDICT: {status} <<<")
    
    # Plotting the "fingerprint"
    branches = [0, 1, 2, 3]
    h_values = [H_THEO - (b * branch_penalty) for b in branches]
    
    plt.figure(figsize=(10, 6))
    plt.bar(branches, h_values, color=['green', 'orange', 'red', 'darkred'], alpha=0.6)
    plt.axhline(y=H_OBS, color='blue', linewidth=2, linestyle='--', label='Observed H0 (Planck)')
    plt.fill_between([-0.5, 3.5], H_OBS-H_UNCERTAINTY, H_OBS+H_UNCERTAINTY, color='blue', alpha=0.1)
    
    plt.title(f"Reality Audit: Where are we? (Verdict: {status})")
    plt.xlabel("Branch Number (0 = Origin)")
    plt.ylabel("Hubble Constant (H0)")
    plt.ylim(66, 68)
    plt.xticks(branches, [f"Branch {b}" for b in branches])
    plt.legend()
    plt.grid(True, axis='y')
    
    filename = "cosmic_audit_result.png"
    plt.savefig(filename)
    print(f"Evidence saved to: {filename}")

if __name__ == "__main__":
    audit_reality()
