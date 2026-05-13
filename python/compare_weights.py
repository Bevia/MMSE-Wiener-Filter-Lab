import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"

w_matlab = np.loadtxt(DATA_DIR / "weights_matlab.csv", delimiter=",").reshape(-1)
w_c = np.loadtxt(DATA_DIR / "weights_c.csv", delimiter=",").reshape(-1)

diff = w_matlab - w_c
max_abs_diff = np.max(np.abs(diff))

print("MMSE Wiener Filter Lab - MATLAB vs C Weight Comparison")
print("------------------------------------------------------")
print()

print("MATLAB weights:")
print(w_matlab)
print()

print("C weights:")
print(w_c)
print()

print("Difference MATLAB - C:")
print(diff)
print()

print(f"Maximum absolute difference: {max_abs_diff:.12e}")

tolerance = 1e-9

if max_abs_diff < tolerance:
    print()
    print("PASS: MATLAB and C weights match within tolerance.")
else:
    print()
    print("WARNING: MATLAB and C weights differ more than expected.")