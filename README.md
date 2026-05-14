# MMSE Wiener Filter Lab

This project demonstrates the derivation and implementation of the Minimum Mean-Square Error Wiener filter across MATLAB, Python, C, and C++.

The goal is to connect theory with implementation:

- MATLAB: mathematical reference model and MSE visualization
- Python: vector construction, signal generation, and plotting
- C/C++: numerical calculation of the optimal Wiener weights

## Visual Overview

![MMSE Wiener Theory Step-by-Step Guide](assets/images/mmse_wiener_theory_guide.jpeg)

## Theory

The adaptive filter output is:

```math
y(n) = W^T X(n)
```

The error is:

```math
e(n) = d(n) - y(n)
```

The MSE cost function is:

```math
\xi = E[|e(n)|^2]
```

For the real-valued Version 1 lab, this is equivalent to:

```math
\xi = E[e^2(n)]
```

The Wiener-Hopf solution is:

```math
W_{opt} = R^{-1}P
```

where:

```math
R = E[X(n)X^T(n)]
```

```math
P = E[X(n)d(n)]
```

The minimum MSE is:

```math
\xi_{min} = E[|d(n)|^2] - P^T W_{opt}
```
