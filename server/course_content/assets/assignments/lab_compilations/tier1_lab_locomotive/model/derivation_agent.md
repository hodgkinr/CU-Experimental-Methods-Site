# Provided Unverified Derivation - Locomotive Crank Kinematics

---

## Student Instruction

The following derivation is provided so that this lab can focus on data analysis and model validation rather than deriving the crank-slider kinematics from scratch. Treat it as **provided but unverified**. Review the geometry, sign conventions, and algebra before using the final equation in your analysis.

Verification is the right word here: students are not being asked to create an original derivation, but they are responsible for checking whether the provided derivation is internally consistent and appropriate for the data they analyze.

---

## Geometry And Variables

![Locomotive Crank Geometry and Variables](../overview/loco_diagram.PNG "Locomotive Crank Geometry and Variables")

The apparatus consists of:

- A disk rotating about fixed point O
- A crank pin A located a radius `r` from O
- A rigid connecting bar of length `l` from A to the sliding collar point B
- A vertical slide for B
- A horizontal offset `d` from the vertical slide to the disk centerline

Variables:

| Symbol | Meaning |
|--------|---------|
| theta | Disk angle |
| beta | Connecting-bar angle from the vertical slide |
| omega_D | Disk angular velocity, `theta_dot` |
| omega_B | Connecting-bar angular velocity, `beta_dot` |
| v_B_y | Vertical velocity of the collar |

The derivation source PDF is retained in `derivation/ASEN2003 Lab3 Locomotive Derivation.pdf`.

---

## Position Relations

Using unit vectors `i` to the right and `j` upward, the crank-pin position relative to O is written as:

```text
r_A = -r sin(theta) i + r cos(theta) j
```

The collar point B relative to A is:

```text
r_B/A = -l sin(beta) i - l cos(beta) j
```

The horizontal constraint gives:

```text
sin(beta) = (d - r sin(theta)) / l
```

Students should check this relation against the physical geometry and the chosen positive direction for theta.

---

## Bar Angular Velocity

Differentiate the horizontal constraint:

```text
sin(beta) = (d - r sin(theta)) / l
```

which gives:

```text
cos(beta) beta_dot = -(r/l) cos(theta) theta_dot
```

Since `theta_dot = omega_D`,

```text
omega_B = beta_dot = -(r cos(theta) / (l cos(beta))) omega_D
```

The derivation PDF also reaches an equivalent magnitude relationship through rigid-body velocity relations. Students should verify the sign convention they use in MATLAB, especially if their theta direction or positive collar velocity direction differs from the diagram.

---

## Collar Velocity

The collar is constrained to move vertically, so the horizontal velocity of B is zero. The vertical velocity follows from differentiating the B position or from the two-point rigid-body velocity relation.

Starting from:

```text
r_B = d i + (r cos(theta) - l cos(beta)) j
```

differentiate:

```text
v_B_y = -r sin(theta) theta_dot + l sin(beta) beta_dot
```

Substitute `theta_dot = omega_D` and the expression for `beta_dot`:

```text
v_B_y = -r omega_D sin(theta)
        - r omega_D cos(theta) tan(beta)
```

Final compact form:

```text
v_B_y = -omega_D r [sin(theta) + cos(theta) tan(beta)]
```

with:

```text
beta = asin((d - r sin(theta)) / l)
```

---

## Verification Checklist

Before using the model, verify:

- `abs((d - r sin(theta))/l) <= 1` over the analyzed theta range
- `theta`, `beta`, and trigonometric functions use radians in MATLAB
- `r`, `l`, `d`, and `v_B_y` use consistent units
- Positive velocity direction matches the plotted experimental collar velocity
- The model is evaluated at the measured `theta_exp`, not only a separate model grid
- Residuals are computed as signed differences using a stated convention

---

## Important Limitation

This is a kinematic model. It predicts collar velocity from geometry and disk angular velocity. It does not model motor dynamics, friction, gravity, structural flex, or mechanical slack. Those effects should appear in the residual discussion, not as terms in the provided velocity equation unless the instructional team intentionally extends the model.

---
