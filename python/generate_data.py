import numpy as np
from pathlib import Path

# ------------------------------------------------------------
# MMSE / Wiener Filter Lab - Version 1
# Real-valued case, filter length N = 3
#
# Goal:
#   Generate an input signal x(n)
#   Generate a desired signal d(n) by passing x(n) through
#   a known 3-tap system and adding noise
#   Build the autocorrelation matrix R
#   Build the cross-correlation vector P
#   Solve Wopt = R^{-1} P using Python
#   Export all data to CSV for MATLAB and C
# ------------------------------------------------------------

np.random.seed(7)

# Project paths
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

# Wiener filter length
N = 3

# Number of samples
num_samples = 1000

# True system/channel we want to identify
# The Wiener filter should learn values close to this vector.
h_true = np.array([0.7, -0.4, 0.2])

# Generate random real-valued input signal
x = np.random.randn(num_samples)

# Generate desired signal d(n)
# d(n) = h0*x(n) + h1*x(n-1) + h2*x(n-2) + noise
noise_std = 0.05
d = np.zeros(num_samples)

for n in range(N - 1, num_samples):
    x_vec = np.array([x[n], x[n - 1], x[n - 2]])
    d[n] = h_true @ x_vec + noise_std * np.random.randn()

# Build data matrix X
# Each row is:
#   X(n)^T = [x(n), x(n-1), x(n-2)]
X = []

for n in range(N - 1, num_samples):
    X.append([x[n], x[n - 1], x[n - 2]])

X = np.array(X)
d_valid = d[N - 1:]

# Estimate autocorrelation matrix R and cross-correlation vector P
#
# R = E[X(n) X^T(n)]
# P = E[X(n) d(n)]
#
# Sample estimates:
# R ≈ (X^T X) / M
# P ≈ (X^T d) / M
M = len(d_valid)

R = (X.T @ X) / M
P = (X.T @ d_valid) / M

# Solve Wiener-Hopf equation:
#   R Wopt = P
#
# Avoid explicitly computing inverse(R).
# This is numerically better than Wopt = inv(R) @ P.
W_python = np.linalg.solve(R, P)

# Compute output and error using estimated weights
y = X @ W_python
e = d_valid - y

mse = np.mean(e**2)
ed2 = np.mean(d_valid**2)
xi_min_formula = ed2 - P.T @ W_python

# Export data
np.savetxt(DATA_DIR / "input_signal.csv", x, delimiter=",")
np.savetxt(DATA_DIR / "desired_signal.csv", d, delimiter=",")
np.savetxt(DATA_DIR / "R_matrix.csv", R, delimiter=",")
np.savetxt(DATA_DIR / "P_vector.csv", P, delimiter=",")
np.savetxt(DATA_DIR / "weights_python.csv", W_python, delimiter=",")
np.savetxt(DATA_DIR / "output_python.csv", y, delimiter=",")
np.savetxt(DATA_DIR / "error_python.csv", e, delimiter=",")

# Print summary
print("MMSE Wiener Filter Lab - Version 1")
print("----------------------------------")
print(f"Filter length N: {N}")
print(f"Samples used: {M}")
print()
print("True system h:")
print(h_true)
print()
print("Estimated Wiener weights from Python:")
print(W_python)
print()
print("Autocorrelation matrix R:")
print(R)
print()
print("Cross-correlation vector P:")
print(P)
print()
print(f"MSE from actual error:       {mse:.8f}")
print(f"MMSE formula Ed2 - P^T W:    {xi_min_formula:.8f}")