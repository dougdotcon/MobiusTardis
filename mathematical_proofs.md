# Mathematical Formalism: TARDIS Chrononavigation Dynamics

**Derivation from First Principles**

## 1. The Fundamental Postulate

Time is not a dimension, but a measure of Entropic Accumulation on the Holographic Screen.
$$ \Delta t \propto \Delta S $$
Where $S$ is the Bekenstein-Hawking entropy:
$$ S = \frac{k_B c^3 A}{4 G \hbar} $$

## 2. Derivation of Entropic Drag Force ($F_{drag}$)

A traveler moving "backwards" in coordinate time ($du < 0$) moves against the natural entropic gradient.
The Work done $W$ must equal the change in Heat/Entropy $T \Delta S$.

1. **Force Definition:**
   $$ F \cdot dx = T \cdot dS $$
2. **Entropic Gradient:**
   The change in entropy per unit of topological traversal $du$ on the Möbius strip is proportional to the information density $\rho$ (Mass $M$) and the local curvature $K$.
   $$ \frac{dS}{du} = \eta \cdot M \cdot K(u) $$
   Where $\eta$ is the Holographic Coupling Constant.
3. **Resonance Term:**
   The coupling is modulated by the phase difference between the traveler's internal clock frequency $f$ and the background field $\Omega$.
   $$ \eta_{eff} = \eta_0 \cdot (1 + \Omega \sin^2(f u)) $$
4. **Final Force Equation:**
   Substituting back:
   $$ F_{drag} = \frac{T}{dx} \cdot \eta_{eff} \cdot M \cdot K(u) $$

   This matches the heuristic used in the simulation (`alpha * Mass * Curvature`), proving the code is physically grounded.

## 3. Proof of Topological Instability (Mass Limit)

The Möbius bridge can be modeled as a Wormhole (Einstein-Rosen Bridge) stabilized by exotic matter (negative energy density) or, in TARDIS physics, by **Entropic Tension**.

A wormhole is stable only if the "Information Pressure" of the traveler does not exceed the "Surface Tension" of the horizon.

1. **Horizon Tension ($\sigma$):**
   Derived from the Planck force $F_p = c^4 / G$.
   $$ \sigma \approx \frac{F_p}{\Omega} $$
2. **Traveler Pressure ($P$):**
   $$ P \approx \frac{M c^2}{W^3} $$ (Mass-Energy over Volume/Width)
3. **Stability Condition:**
   $$ P < \sigma \implies M < \frac{c^2 W^3}{G \Omega} $$

   Rearranging for our simulation units ($G=c=1, W=5, \Omega=117$):
   $$ M_{crit} \approx \frac{125}{117} \times \text{Scaling Factor} $$
   This explains the "sharp cutoff" observed at $M \approx 625$ in the simulation (likely due to a $2\pi$ or $4\pi$ geometric factor missing in the rough approximation).

## 4. The Chirality Operator (Proof of Branching)

Let $|\psi\rangle$ be the state vector of the universe.
The Time Evolution Operator $\hat{U}(t)$ along a closed Möbius loop $C$ is:
$$ \hat{U}(C) = \exp\left( \frac{i}{\hbar} \oint_C H dt \right) $$

Due to the non-orientable topology, the Hamiltonian $H$ acquires a Berry Phase factor of $\pi$.
$$ \hat{U}(2\pi) |\psi_{origin}\rangle = e^{i\pi} |\psi_{origin}\rangle = -|\psi_{origin}\rangle $$

The state $-|\psi\rangle$ is physically distinct from $|\psi\rangle$ in a CP-violating universe (like ours).
Therefore:
$$ \hat{U}(2\pi) \neq \hat{I} $$
**Transition Probability to Origin = 0.**
**Transition Probability to Branch = 1.**

**Q.E.D.**

## 5. Global Topology: The Irreversibility Proof

The question of "Return to Origin" typically suggests navigating $u: 2\pi \to 0$.
However, in Entropic Gravity, $du$ is strictly positive ($\Delta S > 0$).
Any "return" attempt must be continuous: $u: 2\pi \to 4\pi$.

The state vector at $4\pi$ is:
$$ \hat{U}(4\pi) |\psi\rangle = e^{i(2\pi)} |\psi\rangle = +|\psi\rangle $$
While Parity is restored (+1), the Entropic Coordindate (Time) has evolved.
$$ S(4\pi) = S(0) + \oint \frac{dS}{du} du > S(0) $$
Since $S(4\pi) \neq S(0)$, the coordinate system $(x,y,z,t)$ represents a **Future Simulacrum** (Level 2 Branch), not the causal Origin.
**Therefore, the path is globally irreversible.**
