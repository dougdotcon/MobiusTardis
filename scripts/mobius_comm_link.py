
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# --- TARDIS CONSTANTS ---
OMEGA = 117.038
CRITICAL_MASS = 625.0
BRIDGE_WIDTH = 10.0
ENTROPIC_COUPLING = 0.47

class QuantumSignal:
    def __init__(self, frequency, message_content):
        self.mass = 0.0 # Photons have no mass
        self.frequency = frequency
        self.content = message_content
        self.integrity = 1.0 # 100% Integrity
        self.position = 0.0 # u coordinate

    def propagate(self, u_step, curvature):
        # Massless particles ignore curvature drag!
        # But they interact with "Topological Noise" (Jitter)
        
        noise = (curvature * 0.01) * np.random.normal(0, 0.1)
        
        # Signal degrades only if noise > threshold
        if abs(noise) > 0.5:
            self.integrity -= 0.1
            
        self.position += u_step
        return self.integrity

class MassivePayload:
    def __init__(self, mass):
        self.mass = mass
        self.position = 0.0
        self.alive = True

    def calculate_drag(self, curvature):
        return ENTROPIC_COUPLING * self.mass * curvature

class MobiusBridge:
    def __init__(self):
        self.R = 5.0
        self.W = BRIDGE_WIDTH

    def get_curvature(self, u):
        # Curvature spikes at the twist (u = pi)
        # Simplified Gaussian spike for simulation
        spike = np.exp( - ((u - np.pi)**2) / 0.5 )
        return spike * 10.0 # Generic High Curvature

def run_telephony_test():
    print("\n--- RUNNING CHRONO-TELEPHONY TEST (H4) ---")
    bridge = MobiusBridge()
    
    # Subject A: Massive Army (1000 units > Critical)
    army = MassivePayload(mass=1000.0)
    
    # Subject B: Data Packet (0 units)
    signal = QuantumSignal(frequency=OMEGA, message_content="SOS_FROM_BRANCH_A")
    
    steps = 100
    u_range = np.linspace(0, 2*np.pi, steps)
    dt = u_range[1] - u_range[0]
    
    army_status = []
    signal_status = []
    curvature_log = []
    
    for u in u_range:
        k = bridge.get_curvature(u)
        curvature_log.append(k)
        
        # 1. Process Army
        if army.alive:
            drag = army.calculate_drag(k)
            # Check stability
            stress = drag * 0.1
            if stress > 100: # Threshold
                army.alive = False
                print(f"FAILED: Massive Payload destroyed at u={u:.2f} due to Gravitational Shear.")
        
        army_status.append(1 if army.alive else 0)
        
        # 2. Process Signal
        current_integrity = signal.propagate(dt, k)
        signal_status.append(current_integrity)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(u_range, army_status, 'r--', label='Massive Payload (Army)', linewidth=2)
    plt.plot(u_range, signal_status, 'g-', label='Quantum Signal (Data)', linewidth=2)
    plt.plot(u_range, np.array(curvature_log)/10, 'k:', label='Bridge Curvature (Scaled)', alpha=0.5)
    
    plt.title("H4: Chrono-Telephony Viability")
    plt.xlabel("Möbius Coordinate (u)")
    plt.ylabel("Integrity / Status")
    plt.axvline(x=np.pi, color='orange', linestyle='--', label='The Twist (Danger Zone)')
    plt.legend()
    plt.grid(True)
    plt.savefig('telephony_test.png')
    print("SUCCESS: Telephony Plot Generated.")


def run_reality_check():
    print("\n--- RUNNING REALITY AUDIT (H5) ---")
    # Simulate Entropic Noise Floor for different branches
    # Branch 0 (Origin): Low Noise
    # Branch 1: Noise + Residual
    # Branch 2: Noise + 2*Residual
    
    t_points = np.linspace(0, 100, 500)
    
    # Noise Models
    noise_B0 = np.random.normal(0, 1.0, 500) # Pure Gaussian
    noise_B1 = np.random.normal(0, 1.0, 500) + 2.5 # Shifted Mean (Entropic Heat)
    noise_B2 = np.random.normal(0, 1.0, 500) + 5.0 # More Heat
    
    plt.figure(figsize=(10, 6))
    plt.hist(noise_B0, bins=30, alpha=0.5, color='blue', label='Origin (Branch 0)')
    plt.hist(noise_B1, bins=30, alpha=0.5, color='orange', label='1st Copy (Branch 1)')
    plt.hist(noise_B2, bins=30, alpha=0.5, color='red', label='2nd Copy (Branch 2)')
    
    plt.title("H5: Cosmic Entropic Background (CEB) Signature")
    plt.xlabel("Entropic Noise Level (Arb. Units)")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True)
    plt.savefig('reality_check_signature.png')
    print("SUCCESS: Reality Check Plot Generated.")

if __name__ == "__main__":
    run_telephony_test()
    run_reality_check()
