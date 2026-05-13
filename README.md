# MMSE Wiener Filter Lab

This project demonstrates the derivation and implementation of the Minimum Mean-Square Error Wiener filter across MATLAB, Python, C, and C++.

The goal is to connect theory with implementation:

- MATLAB: mathematical reference model and MSE visualization
- Python: vector construction, signal generation, and plotting
- C/C++: numerical calculation of the optimal Wiener weights

## Theory

The adaptive filter output is:

y(n) = W^T X(n)

The error is:

e(n) = d(n) - y(n)

The MSE cost function is:

xi = E[|e(n)|^2]

The Wiener-Hopf solution is:

Wopt = R^{-1}P

where:

R = E[X(n)X^T(n)]
P = E[X(n)d(n)]

The minimum MSE is:

xi_min = E[|d(n)|^2] - P^T Wopt