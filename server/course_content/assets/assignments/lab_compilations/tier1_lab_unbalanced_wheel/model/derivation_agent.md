# Provided Unverified Derivation — Unbalanced Wheel: Inertia Distribution and Rolling Dynamics

---

## How Students Should Use This Derivation

This derivation is provided so the lab can focus on experimental data analysis,
model implementation, and model-data comparison rather than on dynamics
derivation from a blank page. It is **not** externally verified.

Students should verify the derivation before using it as the basis for their
analysis. Verification means checking the assumptions, signs, units, limiting
cases, and energy terms well enough to decide whether the model is appropriate
for comparison with the measured data.

The current setup uses the outside Aero building ramp. The ramp angle β must
be measured for that setup before numerical model predictions are finalized.

Recommended verification checks:

- Confirm the rolling-without-slip constraint: v_cm = Rω
- Confirm the ramp-height relation: h = Rθ sin(β) using the current ramp angle
- Confirm that all kinetic-energy terms have units of joules
- Confirm that the friction moment contributes negative work: −Qθ
- Check the unbalanced-mass potential term by evaluating θ = 0
- Check the difference between the point-mass model and rigid-body model
- Check whether the provided rigid-body inertia term is being counted once,
  not double-counted with translational kinetic energy

The goal is not to re-create the derivation from scratch. The goal is to be able
to defend the model you use when you compare it with data.

---

## Section 1 — Physical Setup and Coordinate System

A cylindrical wheel rolls down the outside Aero building ramp without slipping. A trailing support apparatus is rigidly attached to the wheel; it translates but does not rotate. An eccentric mass can be bolted to the wheel to create the unbalanced configuration.

**Coordinate system:**

- θ = rotation angle, measured clockwise from the perpendicular vector into the ramp
- θ = 0 is the position when the wheel starts moving from rest
- For unbalanced trials: eccentric mass is positioned perpendicular to the ramp surface at θ = 0

**Rolling constraint:**

v_cm = Rω

where v_cm is the velocity of the wheel center and ω = dθ/dt.

**System Parameters:**

| Symbol | Value | Units | Description |
|--------|-------|-------|-------------|
| M | 11.7 | kg | Mass of cylindrical wheel |
| M₀ | 0.7 | kg | Mass of trailing support apparatus |
| m | 3.4 | kg | Mass of eccentric mass |
| R | 0.235 | m | Radius of cylinder |
| κ | 0.203 | m | Radius of gyration of wheel |
| I | Mκ² | kg·m² | Moment of inertia of wheel about its center |
| β | **TBD** | deg | Outside-ramp slope angle; measure before deployment |
| r | 0.178 | m | Distance from wheel center to eccentric mass center |
| r_extra | 0.019 | m | Radius of eccentric mass, modeled as a solid rod |
| g | 9.81 | m/s² | Gravitational acceleration |

---

## Section 2 — Work-Energy Principle

The work-energy principle applied to the complete system is:

W_net = ΔKE = KE_final − KE_initial

The wheel starts from rest, so KE_initial = 0 for all trials.

The kinetic energy of the rolling system includes:

- rotational kinetic energy of the wheel: ½Iω²
- translational kinetic energy of the wheel center: ½Mv_cm²
- translational kinetic energy of the trailing apparatus: ½M₀v_cm²

Using the rolling constraint, all kinetic-energy terms can be written in terms of ω.

For the unbalanced configuration, the eccentric mass adds translational kinetic energy and, in MODEL_4, rotational kinetic energy about its own center.

---

## Section 3 — MODEL_1: Balanced Wheel, No Friction

**Configuration:** Wheel and trailing apparatus only; no eccentric mass; no friction moment.

**Assumptions:**

- Cylinder rolls without slipping
- Trailing apparatus translates but does not rotate
- No friction at the axle

Energy equation:

(M + M₀)gRθ sin(β) = ½[(M + M₀)R² + Mκ²]ω²

Solving for angular velocity:

ω₁(θ) = √{2(M + M₀)gRθ sin(β) / [(M + M₀)R² + Mκ²]}

---

## Section 4 — MODEL_2: Balanced Wheel, Constant Friction Moment

**Modification of MODEL_1:** Add a constant negative moment Q applied to the shaft of the wheel. Q represents friction at the axle; its value is unknown and must be determined empirically.

The friction moment does negative work:

W_Q = −Qθ

The energy equation becomes:

(M + M₀)gRθ sin(β) − Qθ = ½[(M + M₀)R² + Mκ²]ω²

Solving for angular velocity:

ω₂(θ, Q) = √{2[(M + M₀)gRθ sin(β) − Qθ] / [(M + M₀)R² + Mκ²]}

**Empirical determination of Q:**

- Q is not known from first principles; fit it to balanced experimental data
- Try 5 or more values of Q
- Identify a value that reasonably matches both balanced trials
- Carry the same Q into MODEL_3 and MODEL_4 unchanged

---

## Section 5 — MODEL_3: Unbalanced Wheel, Eccentric Mass as Particle

**Modification of MODEL_2:** Add the eccentric mass m at radius r, modeled as a point particle.

The eccentric mass center moves in a circle of radius r about the wheel center. Its velocity has two components that depend on both ω and the current angular position θ.

The extra mass changes height both because the wheel center moves down the ramp and because the mass rotates around the wheel center. Relative to the initial configuration:

Δh_extra = Rθ sin(β) − r cos(θ + β) + r cos(β)

The translational speed of the eccentric mass contributes:

v_extra² = ω²(R² + 2Rr cos(θ) + r²)

Combining balanced-wheel energy, eccentric-mass potential-energy change, eccentric-mass translational kinetic energy, and friction work:

ω₃(θ, Q) = √{2[(M + M₀)gRθ sin(β) + mg(Rθ sin(β) − r cos(θ + β) + r cos(β)) − Qθ] / [(M + M₀)R² + Mκ² + m(R² + 2Rr cos(θ) + r²)]}

---

## Section 6 — MODEL_4: Unbalanced Wheel, Eccentric Mass as Rigid Body

**Modification of MODEL_3:** Model the eccentric mass as a rigid body rather than a point particle. This adds a rotational kinetic-energy term for the eccentric mass about its own center of mass.

I_extra = ½mr_extra²

The rigid-body version uses the same numerator as MODEL_3. The difference is the additional rotational kinetic energy of the eccentric mass about its own center:

ω₄(θ, Q) = √{2[(M + M₀)gRθ sin(β) + mg(Rθ sin(β) − r cos(θ + β) + r cos(β)) − Qθ] / [(M + M₀)R² + Mκ² + m(R² + 2Rr cos(θ) + r²) + I_extra]}

Verification note: students should check whether the orbital contribution associated with the eccentric mass is already included before adding any additional parallel-axis term.

---

## Section 7 — Residual Analysis Checks

After fitting models to data, use residual statistics to help judge agreement.

**Residual definition:**

ε_i = ω_observed,i − ω_predicted(θ_i)

**Important:** Do not take the absolute value of residuals. A non-zero mean residual may indicate systematic bias in the model or setup.

**Evaluation rule:** Evaluate the model at the experimentally measured θ_i values. Residuals must compare matched model and experimental points.

**Useful checks:**

| Check | Formula or method | What it helps you notice |
|-------|-------------------|--------------------------|
| Mean residual | ε̄ = (1/N)Σ ε_i | Possible systematic bias |
| Standard deviation | σ_ε = std(ε) | Random spread around the model |
| Uncertainty of mean | σ_ε / √N | Precision of the mean residual estimate |
| N | count of observations | Amount of data in the reliable range |
| Outlier count | count of unusually large residuals | Whether a few points dominate the mismatch |
| Scaled histogram | plot ε_i / σ_ε | Whether residuals look random or structured |

These checks guide interpretation; they do not automatically prove which model is correct.

---

## References

- Taylor, J.R. (1997). *An Introduction to Error Analysis*. University Science Books. (Residual statistics and error analysis framework)
- Meriam, J.L. & Kraige, L.G. *Engineering Mechanics: Dynamics*. (Work-energy methods for rigid bodies)
- Sample report: keep staff-only unless intentionally released by the teaching team

---
