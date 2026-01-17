import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- TARDIS Advanced Physics Constants ---
OMEGA = 117.038
ENTROPIC_COUPLING = 0.47
PLANCK_SCALE = 1.6e-35
CRITICAL_CURVATURE = 1e5 # Threshold for topological collapse

class MobiusManifold:
    def __init__(self, radius=10, width=5):
        self.R = radius
        self.W = width

    def parametric_surface(self, u, v):
        half_u = u / 2
        x = (self.R + (self.W * v / 2) * np.cos(half_u)) * np.cos(u)
        y = (self.R + (self.W * v / 2) * np.cos(half_u)) * np.sin(u)
        z = (self.W * v / 2) * np.sin(half_u)
        return x, y, z

    def get_local_curvature(self, u, v):
        """
        Calculates local curvature tensor magnitude (simplified).
        K ~ 1/R * Twist
        """
        # Twist increases with u
        twist_strain = np.abs(np.cos(u/2)) * (self.W / self.R)
        return twist_strain

class AdvancedTraveler:
    def __init__(self, mass=1.0, frequency_ratio=1.0):
        self.mass = mass
        self.freq_ratio = frequency_ratio # Ratio relative to OMEGA
        self.energy_cost = 0.0
        self.chirality = 1
        self.state_vector = np.array([1.0, 0.0, 0.0]) # [Normal, Binormal, Tangent]

    def calculate_entropic_drag(self, u, curvature):
        """
        H1: Entropic Resonance Hypothesis
        Drag is minimized when traveler frequency matches OMEGA harmonics.
        Drag = Mass * Curvature * | sin(Freq * u) |
        """
        # Resonance factor: minimal when freq_ratio is integer
        resonance_miss = np.sin(np.pi * self.freq_ratio) ** 2 
        base_drag = ENTROPIC_COUPLING * self.mass * curvature
        
        # If perfect resonance (miss ~ 0), drag is small. Else high.
        resonance_penalty = 1 + OMEGA * resonance_miss
        
        return base_drag * resonance_penalty

class MobiusLab:
    def __init__(self):
        self.manifold = MobiusManifold()
    
    def run_resonance_sweep(self, freq_range=(0.5, 3.0), steps=50):
        print("[LAB] Running Entropic Resonance Sweep...")
        freqs = np.linspace(freq_range[0], freq_range[1], steps)
        energies = []
        
        for f in freqs:
            traveler = AdvancedTraveler(mass=1.0, frequency_ratio=f)
            total_energy = 0
            
            # Simulate one loop
            u_vals = np.linspace(0, 2*np.pi, 100)
            for u in u_vals:
                k = self.manifold.get_local_curvature(u, 0)
                drag = traveler.calculate_entropic_drag(u, k)
                total_energy += drag
            
            energies.append(total_energy)
            
        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(freqs, energies, marker='o', color='purple')
        plt.title(f"H1: Entropic Resonance Spectrum (OMEGA={OMEGA})")
        plt.xlabel("Frequency Ratio (f / \u03a9)") # Omega symbol
        plt.ylabel("Total Entropic Energy Cost")
        plt.grid(True)
        plt.axvline(x=1.0, color='r', linestyle='--', label='Fundamental Resonance')
        plt.axvline(x=2.0, color='r', linestyle='--', label='2nd Harmonic')
        plt.legend()
        plt.savefig('lab_resonance_spectrum.png')
        print("[LAB] Resonance plot saved.")
        return freqs, energies

    def run_stability_test(self, max_mass=100.0):
        print("[LAB] Running Topological Stability Test (Mass Limit)...")
        masses = np.linspace(0.1, max_mass, 50)
        max_curvatures = []
        stable = []
        
        for m in masses:
            # H2: Stability Hypothesis
            # Traveler mass induces feedback curvature on the manifold
            # K_induced = K_0 + (Mass * OMEGA) / Tension
            
            induced_strain = (m * np.log(OMEGA)) 
            
            if induced_strain > CRITICAL_CURVATURE:
                stable.append(False)
                max_curvatures.append(CRITICAL_CURVATURE * 1.5) # Collapse
            else:
                stable.append(True)
                max_curvatures.append(induced_strain)
        
        # Plotting
        plt.figure(figsize=(10, 6))
        colors = ['green' if s else 'red' for s in stable]
        plt.scatter(masses, max_curvatures, c=colors)
        plt.axhline(y=CRITICAL_CURVATURE, color='black', linestyle='--', label='Critical Threshold')
        plt.title("H2: Topological Stability Limit")
        plt.xlabel("Traveler Mass (Information Density)")
        plt.ylabel("Induced Manifold Curvature")
        plt.legend()
        plt.savefig('lab_stability_limit.png')
        print("[LAB] Stability plot saved.")

    def run_recursion_test(self):
        print("[LAB] Running Recursive Branching Test (4 Pi Loop)...")
        traveler = AdvancedTraveler()
        
        u_vals = np.linspace(0, 4*np.pi, 200) # Two loops
        orientations = []
        
        for u in u_vals:
            # Orientation vector projection (simplified to cos(u/2))
            orientations.append(np.cos(u/2))
            
        plt.figure(figsize=(10, 6))
        plt.plot(u_vals, orientations, lw=2)
        
        # Mark key points
        plt.scatter([0], [1], color='green', label='Start (0)')
        plt.scatter([2*np.pi], [-1], color='red', label='Loop 1 End (Inverted/Branched)')
        plt.scatter([4*np.pi], [1], color='blue', label='Loop 2 End (Restored?)')
        
        plt.axhline(0, color='gray', lw=0.5)
        plt.title("H3: Recursive Branching Dynamics (Chirality Parity)")
        plt.xlabel("Topological Time (u)")
        plt.ylabel("Orientation Vector (NormalZ)")
        plt.legend()
        plt.grid()
        plt.savefig('lab_recursion_dynamics.png')
        print("[LAB] Recursion plot saved.")

def main():
    lab = MobiusLab()
    
    # Run Experiment Suite
    lab.run_resonance_sweep()
    lab.run_stability_test(max_mass=1000) # High mass to force collapse
    lab.run_recursion_test()
    
    print("[LAB] All experiments completed.")

if __name__ == "__main__":
    main()
