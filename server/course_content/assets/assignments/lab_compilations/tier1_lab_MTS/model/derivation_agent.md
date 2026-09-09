# Unverified Derivation - MTS EXCEED Compliance Model

---

## How Students Should Use This Derivation

This derivation is provided so the laboratory exercise can focus on experimental data analysis, model implementation, and model-data comparison. It is not externally verified by the laboratory staff in the current source PDF.

Students are required to verify the derivation and assumptions before using it in final analysis. Verification means checking dimensions, elastic variables, boundary conditions, and whether a simple series-compliance model is adequate for the physical MTS EXCEED testing apparatus.

---

## Stress Definition

An axial load `P` is applied to a specimen with initial width `w` and thickness `t`.

```text
A0 = w t
sigma = P / A0
```

where:

| Symbol | Meaning | Units |
|--------|---------|-------|
| `A0` | Initial cross-sectional area | area units consistent with `w` and `t` |
| `P` | Applied axial load | force |
| `sigma` | Engineering stress | force / area |

---

## Two Strain Measures

The source PDF distinguishes two measures of strain.

### Nominal Crosshead Strain

Nominal strain is derived from total crosshead displacement relative to the initial free grip-to-grip specimen length:

```text
epsilon_n = delta_total / Lg
```

### Extensometer Strain

Extensometer strain is measured locally by the Epsilon extensometer over its fixed gage length:

```text
epsilon_e = DeltaLe / L0
```

For the Epsilon 3542 axial extensometer in this PDF:

```text
L0 = 1.000 in
```

---

## Total Crosshead Displacement Model

The crosshead displacement includes more than specimen stretch. The source PDF identifies machine frame compliance, load-cell elasticity, grip/specimen interface motion, and possible specimen slip as contributors.

```text
delta_total = delta_specimen + delta_compliance + delta_slip
```

Assuming the system is in the linear-elastic regime before material yield and no slip occurs:

```text
delta_slip = 0
delta_compliance = P Cm
delta_specimen = P Lg / (A0 E)
```

where:

| Symbol | Meaning | Units |
|--------|---------|-------|
| `Cm` | Machine compliance parameter | displacement / force, such as in/lb or mm/N |
| `E` | Material elastic modulus from a better local strain measurement | stress units |
| `Lg` | Free grip-to-grip specimen length | length |

Substituting into the total displacement model gives:

```text
delta_total = P Lg / (A0 E) + P Cm
```

Dividing by load:

```text
delta_total / P = Lg / (A0 E) + Cm
```

Solving for machine compliance:

```text
Cm = delta_total / P - Lg / (A0 E)
Cm = epsilon_n Lg / P - Lg / (A0 E)
```

---

## Apparent Elastic Modulus Relation

If students compute elastic modulus using nominal strain from crosshead displacement, they obtain an apparent modulus `Eapp`. The source PDF gives the series-spring relation:

```text
1 / Eapp = 1 / E + Cm (A0 / Lg)
```

The PDF states that students should plot `1/Eapp` against `A0/Lg` across multiple specimens or free lengths, then check whether the slope gives a consistent `Cm` and the intercept matches `1/E` from the extensometer.

**Placeholder requiring teaching-team decision:** the current PDF only gives one nominal specimen width and thickness for the basic ASEN 3501 setup. If students are expected to estimate `Cm` from a slope, the assigned data must include multiple specimens, multiple free lengths, or another explicit method for compliance estimation.

---

## Verification Checks

Before relying on this model, verify:

- `sigma = P/A0` uses consistent force and area units
- `epsilon_n` and `epsilon_e` are dimensionless
- `Cm` has units of displacement per force
- the no-slip assumption is reasonable for the selected elastic-region data
- the elastic-region data are selected before yield
- crosshead displacement and extensometer strain are not treated as interchangeable measurements
- preload and grip seating steps do not hide or erase real specimen load history

---
