import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"

w_python = np.loadtxt(DATA_DIR / "weights_python.csv", delimiter=",")
w_c = np.loadtxt(DATA_DIR / "weights_c.csv", delimiter=",")

print("MMSE Wiener Filter Lab - Weight Comparison")
print("------------------------------------------")
print()
print("Python weights:")
print(w_python)
print()
print("C weights:")
print(w_c)
print()
print("Difference Python - C:")
print(w_python - w_c)
print()
print("Maximum absolute difference:")
print(np.max(np.abs(w_python - w_c)))

matlab_file = DATA_DIR / "weights_matlab.csv"

if matlab_file.exists():
    w_matlab = np.loadtxt(matlab_file, delimiter=",")
    print()
    print("MATLAB weights:")
    print(w_matlab)
    print()
    print("Difference Python - MATLAB:")
    print(w_python - w_matlab)
    print()
    print("Maximum absolute difference:")
    print(np.max(np.abs(w_python - w_matlab)))
else:
    print()
    print("MATLAB weights not found yet.")
    print("Run matlab/main_mmse_demo.m to generate weights_matlab.csv.")