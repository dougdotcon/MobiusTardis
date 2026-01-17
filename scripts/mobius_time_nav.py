import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- TARDIS Constants ---
OMEGA = 117.038
ENTROPIC_COUPLING = 0.47

class MobiusManifold:
    """
    Represents the topological fabric of time as a Möbius strip.
    """
    def __init__(self, radius=10, width=5):
        self.R = radius
        self.W = width

    def parametric_surface(self, u, v):
        """
        Parametric equations for the Möbius Strip.
        u: [0, 2*pi] (The 'Time' loop)
        v: [-1, 1]   (The 'Entropy/Width' dimension)
        """
        # x = (R + w/2 * cos(u/2)) * cos(u)
        # y = (R + w/2 * cos(u/2)) * sin(u)
        # z = w/2 * sin(u/2)
        
        half_u = u / 2
        
        x = (self.R + (self.W * v / 2) * np.cos(half_u)) * np.cos(u)
        y = (self.R + (self.W * v / 2) * np.cos(half_u)) * np.sin(u)
        z = (self.W * v / 2) * np.sin(half_u)
        
        return x, y, z

    def calculate_curvature(self, u, v):
        """
        Calculates local curvature (representing gravitational strain).
        Simplified proxy: just looking at the twist factor.
        """
        return np.sin(u/2) * OMEGA # TARDIS modification

class TimeTraveler:
    """
    Navigates the manifold.
    """
    def __init__(self, mass=1.0):
        self.mass = mass
        self.entropy_state = 1.0 # Initial baseline entropy
        self.chirality = 1       # +1: Normal, -1: Inverted (Branched)

    def traverse_loop(self, steps=100):
        """
        Simulates a full traversal of the time loop (0 to 2pi).
        """
        u_vals = np.linspace(0, 2*np.pi, steps)
        # Path stays in the "center" of the strip (v=0) for simplicity,
        # but we track the normal vector orientation to detect the flip.
        
        trajectory = []
        orientation_history = []
        
        print(f"[*] Initiating Temporal Jump. OMEGA = {OMEGA}")
        
        for u in u_vals:
            # Traveling along the t-axis (u)
            # Entropic drag increases with u
            current_entropy = self.entropy_state * np.exp(u / OMEGA)
            
            # Record state
            trajectory.append((u, current_entropy))
            
            # The 'Normal' vector rotates by Pi over a 2Pi loop
            # Check orientation factor: cos(u/2)
            orientation = np.cos(u/2)
            orientation_history.append(orientation)

        # Final check
        initial_orientation = orientation_history[0] # cos(0) = 1
        final_orientation = orientation_history[-1]  # cos(pi) = -1
        
        branched = False
        if abs(initial_orientation - final_orientation) > 1.9:
            self.chirality *= -1
            branched = True
            
        return trajectory, branched

def visualize_simulation(trajectory, manifold):
    """
    Plots the Möbius strip and the traveler's path.
    """
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')

    # 1. Plot Möbius Strip Mesh
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(-1, 1, 10)
    u_grid, v_grid = np.meshgrid(u, v)
    
    x, y, z = manifold.parametric_surface(u_grid, v_grid)
    
    # Plot surface with partial transparency
    ax.plot_surface(x, y, z, alpha=0.3, color='cyan', edgecolor='gray', linewidth=0.5)

    # 2. Plot Trajectory (The Timeline)
    # We map the 1D trajectory (u, entropy) back to 3D coordinates on the strip (v=0)
    u_traj = [t[0] for t in trajectory]
    x_t, y_t, z_t = manifold.parametric_surface(np.array(u_traj), 0)
    
    ax.plot(x_t, y_t, z_t, color='red', linewidth=3, label='Time Traveler Path')
    
    # 3. Mark Start and End
    ax.scatter(x_t[0], y_t[0], z_t[0], color='green', s=100, label='Start (Present)')
    ax.scatter(x_t[-1], y_t[-1], z_t[-1], color='purple', s=100, label='Return (Branched Past)')

    # Labels and Style
    ax.set_title(f"TARDIS Time Navigation (Möbius Topology)\nOMEGA = {OMEGA}", fontsize=14)
    ax.set_xlabel('X (Space)')
    ax.set_ylabel('Y (Space)')
    ax.set_zlabel('Z (Entropy/Branch)')
    ax.legend()
    
    # Save instead of show
    output_path = 'mobius_simulation_result.png'
    plt.savefig(output_path)
    print(f"[*] Visualization saved to {output_path}")

def main():
    print("------------------------------------------------")
    print(" TARDIS CHRONONAVIGATION SYSTEM v1.0")
    print("------------------------------------------------")
    
    # Initialize Physics
    manifold = MobiusManifold()
    traveler = TimeTraveler()
    
    # execute Jump
    trajectory, branched = traveler.traverse_loop()
    
    print(f"\n[RESULTS ANALYSIS]")
    print(f"Traversed Path Length: {len(trajectory)} steps")
    
    if branched:
        print(f"STATUS: SUCCESS - BRANCH DETECTED")
        print(f"Chirality Flip: {traveler.chirality}")
        print(f"> The traveler returned to the starting coordinate, but 'inverted'.")
        print(f"> This represents arrival at a PARALLEL TIMELINE (Branch).")
        print(f"> No Grandfather Paradox generated.")
    else:
        print(f"STATUS: FAILURE - CLOSED LOOP")
        print(f"> Traveler returned to exact original state.")
        print(f"> Causality violation probable.")

    # Visualize
    visualize_simulation(trajectory, manifold)

if __name__ == "__main__":
    main()
