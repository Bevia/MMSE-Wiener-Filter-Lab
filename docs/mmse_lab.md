# MMSE Wiener Filter Lab — Step-by-Step Workflow

This document explains how to reproduce the Version 1 MMSE Wiener Filter Lab from start to finish.

Version 1 uses:

- Real-valued signals
- A Wiener filter of length `N = 3`
- Python for dataset generation and validation
- MATLAB as the reference model
- C as the implementation under test

The core equation is the Wiener-Hopf equation:

$$
RW = P
$$

where:

- `R` is the autocorrelation matrix
- `P` is the cross-correlation vector
- `W` is the optimal Wiener weight vector

The goal of the lab is to prove that MATLAB and C compute the same optimal Wiener filter weights from the same `R` and `P`.

---

## 1. Project Structure

Your project should look like this:

```text
MMSE-Wiener-Filter-Lab/
│
├── data/
│   ├── R_matrix.csv
│   ├── P_vector.csv
│   ├── input_signal.csv
│   ├── desired_signal.csv
│   ├── weights_python.csv
│   ├── weights_matlab.csv
│   ├── weights_c.csv
│   ├── output_python.csv
│   ├── output_matlab.csv
│   ├── error_python.csv
│   └── error_matlab.csv
│
├── matlab/
│   └── main_mmse_demo.m
│
├── c/
│   ├── main.c
│   ├── wiener_filter.c
│   ├── wiener_filter.h
│   └── Makefile
│
├── python/
│   ├── generate_data.py
│   └── compare_weights.py
│
└── docs/
    ├── mmse_derivation.md
    └── mmse_lab.md
```

---

## 2. Recommended Workflow

There are two possible workflows.

### Workflow A — Local MATLAB

This is the recommended workflow if you have MATLAB installed locally.

```text
Python generates the dataset
MATLAB verifies the reference solution
C solves the same Wiener-Hopf system
Python compares the results
```

The sequence is:

```text
generate_data.py → MATLAB → C → compare_weights.py
```

### Workflow B — MATLAB Online

This workflow is useful if you are using MATLAB Online and uploading files is inconvenient.

```text
MATLAB generates the dataset
C solves the same Wiener-Hopf system
Python compares the results
```

The sequence is:

```text
MATLAB Online → download CSV files → C → compare_weights.py
```

For GitHub and local reproducibility, Workflow A is cleaner.

---

# Workflow A — Local MATLAB

Use this workflow when MATLAB is installed on your computer.

---

## 3. Start from a Clean Dataset

From the project root, remove old CSV files:

```bash
rm data/*.csv
```

This prevents old outputs from being mixed with a new run.

After this step, the `data/` folder should be empty.

---

## 4. Generate the Dataset with Python

From the project root, run:

```bash
python3 python/generate_data.py
```

This script generates:

- input signal `x(n)`
- desired signal `d(n)`
- autocorrelation matrix `R`
- cross-correlation vector `P`
- Python Wiener weights
- Python output signal
- Python error signal

The Python script should create:

```text
data/
├── input_signal.csv
├── desired_signal.csv
├── R_matrix.csv
├── P_vector.csv
├── weights_python.csv
├── output_python.csv
└── error_python.csv
```

The most important files are:

```text
R_matrix.csv
P_vector.csv
```

These define the Wiener-Hopf system:

$$
RW = P
$$

---

## 5. Run the MATLAB Reference Model

Now run MATLAB locally.

From MATLAB, run:

```matlab
run('matlab/main_mmse_demo.m')
```

The MATLAB script reads:

```text
data/R_matrix.csv
data/P_vector.csv
data/input_signal.csv
data/desired_signal.csv
```

Then it solves:

$$
RW_{matlab} = P
$$

using:

```matlab
W_matlab = R \ P;
```

This is preferred over:

```matlab
W_matlab = inv(R) * P;
```

because solving the linear system directly is numerically better than explicitly computing the inverse.

After running MATLAB, the following file should be created:

```text
data/weights_matlab.csv
```

Depending on your MATLAB script, it may also create:

```text
data/output_matlab.csv
data/error_matlab.csv
```

---

## 6. Build and Run the C Implementation

The C implementation reads:

```text
data/R_matrix.csv
data/P_vector.csv
```

and solves the same system:

$$
RW_c = P
$$

From the project root, enter the C folder:

```bash
cd c
```

Clean previous builds:

```bash
make clean
```

Build the C program:

```bash
make
```

Run it:

```bash
make run
```

Return to the project root:

```bash
cd ..
```

After running C, this file should be created:

```text
data/weights_c.csv
```

---

## 7. Compare MATLAB and C with Python

From the project root, run:

```bash
python3 python/compare_weights.py
```

The script compares:

```text
data/weights_matlab.csv
data/weights_c.csv
```

It prints:

- MATLAB weights
- C weights
- difference between MATLAB and C
- maximum absolute difference

A successful result should look like this:

```text
MMSE Wiener Filter Lab - MATLAB vs C Weight Comparison
------------------------------------------------------

MATLAB weights:
[ 0.70100109 -0.40017179  0.20148352]

C weights:
[ 0.70100109 -0.40017179  0.20148352]

Difference MATLAB - C:
[ 4.79061235e-13  1.36002321e-13 -8.90121310e-14]

Maximum absolute difference: 4.790612351258e-13

PASS: MATLAB and C weights match within tolerance.
```

The exact numbers may change depending on the dataset, but MATLAB and C should match very closely.

---

## 8. Validation Criteria

The validation passes if the maximum absolute difference is smaller than:

```text
1e-9
```

Example:

```text
Maximum absolute difference: 4.79e-13
```

This is a successful result.

A difference around `1e-13` is just floating-point numerical precision.

---

## 9. Full Local MATLAB Command Sequence

From the project root:

```bash
rm data/*.csv
python3 python/generate_data.py
```

Then run MATLAB:

```matlab
run('matlab/main_mmse_demo.m')
```

Then return to the terminal and run:

```bash
cd c
make clean
make
make run
cd ..
python3 python/compare_weights.py
```

Expected final result:

```text
PASS: MATLAB and C weights match within tolerance.
```

---

# Workflow B — MATLAB Online

Use this workflow if you are using MATLAB Online and do not want to upload CSV files manually.

In this workflow, MATLAB Online generates the dataset itself.

---

## 10. Start from MATLAB Online

In MATLAB Online, use a self-contained MATLAB script that generates:

- input signal `x(n)`
- desired signal `d(n)`
- `R_matrix.csv`
- `P_vector.csv`
- `weights_matlab.csv`
- `output_matlab.csv`
- `error_matlab.csv`

Run:

```matlab
run('MMSE.m')
```

The script should create a `data/` folder in MATLAB Drive and save the CSV files there.

Expected MATLAB Online output files:

```text
input_signal.csv
desired_signal.csv
R_matrix.csv
P_vector.csv
weights_matlab.csv
output_matlab.csv
error_matlab.csv
```

---

## 11. Download MATLAB Online CSV Files

Download the generated CSV files from MATLAB Online.

Then copy them into your local project folder:

```text
MMSE-Wiener-Filter-Lab/data/
```

Your local `data/` folder should contain:

```text
data/
├── input_signal.csv
├── desired_signal.csv
├── R_matrix.csv
├── P_vector.csv
├── weights_matlab.csv
├── output_matlab.csv
└── error_matlab.csv
```

The key files are:

```text
R_matrix.csv
P_vector.csv
weights_matlab.csv
```

These must all come from the same MATLAB run.

---

## 12. Run the C Implementation Locally

From the project root:

```bash
cd c
make clean
make
make run
cd ..
```

The C program reads:

```text
data/R_matrix.csv
data/P_vector.csv
```

and writes:

```text
data/weights_c.csv
```

---

## 13. Compare MATLAB Online and C Results

From the project root:

```bash
python3 python/compare_weights.py
```

Expected result:

```text
PASS: MATLAB and C weights match within tolerance.
```

---

# Additional Notes

---

## 14. Why `output_matlab.csv` Has Fewer Samples

The original input signal has 1000 samples.

The filter length is:

```text
N = 3
```

The first valid input vector is:

$$
X(3) =
\begin{bmatrix}
x(3) \\
x(2) \\
x(1)
\end{bmatrix}
$$

So the number of valid output samples is:

```text
1000 - 3 + 1 = 998
```

Therefore:

```text
input_signal.csv      has 1000 samples
desired_signal.csv    has 1000 samples
output_matlab.csv     has 998 samples
error_matlab.csv      has 998 samples
```

This is expected.

---

## 15. Expected Weight Values

The Version 1 example usually generates the desired signal using a true system close to:

$$
h =
\begin{bmatrix}
0.7 \\
-0.4 \\
0.2
\end{bmatrix}
$$

So the estimated Wiener weights should be close to:

$$
W =
\begin{bmatrix}
0.7 \\
-0.4 \\
0.2
\end{bmatrix}
$$

A typical result is:

```text
W =
[ 0.70100109
 -0.40017179
  0.20148352 ]
```

The weights are not exactly equal to the true system because:

- noise is added to the desired signal
- expectations are estimated using a finite number of samples

---

## 16. Common Mistakes

### Mistake 1: Not rerunning C after replacing CSV files

If you replace:

```text
R_matrix.csv
P_vector.csv
```

you must rerun C.

Otherwise, `weights_c.csv` may belong to an older dataset.

Correct sequence:

```bash
cd c
make clean
make
make run
cd ..
python3 python/compare_weights.py
```

---

### Mistake 2: Mixing files from different runs

These files must belong to the same run:

```text
R_matrix.csv
P_vector.csv
weights_matlab.csv
weights_c.csv
```

If `R_matrix.csv` and `P_vector.csv` come from one run, but `weights_matlab.csv` comes from another, the validation will fail.

---

### Mistake 3: Running the C program from the wrong folder

If your C code uses paths like:

```c
const char *r_file = "../data/R_matrix.csv";
const char *p_file = "../data/P_vector.csv";
const char *w_file = "../data/weights_c.csv";
```

then the C program should be run from inside the `c/` folder.

That is why this workflow uses:

```bash
cd c
make run
cd ..
```

If your C code uses paths like:

```c
const char *r_file = "data/R_matrix.csv";
const char *p_file = "data/P_vector.csv";
const char *w_file = "data/weights_c.csv";
```

then the program should be run from the project root.

The relative paths must match the folder where the executable runs.

---

### Mistake 4: Forgetting that Python and MATLAB may generate different random data

If Python generates the dataset, MATLAB should read that dataset.

If MATLAB generates the dataset, Python should not regenerate it before the comparison.

The rule is simple:

```text
One dataset per validation run.
```

Do not mix Python-generated `R` and `P` with MATLAB-generated weights from another run.

---

## 17. What the Validation Proves

The validation proves that:

```text
The same R and P were used by MATLAB and C
MATLAB solved R W = P
C solved R W = P
Python compared both weight vectors
The difference was within floating-point precision
```

Therefore, the C implementation correctly solves the Wiener-Hopf equation.

---

## 18. Final Summary

The lab demonstrates the complete engineering path:

```text
Theory → Dataset Generation → MATLAB Reference Model → C Implementation → Python Validation
```

The key equation is:

$$
RW = P
$$

MATLAB and C solve the same equation.

Python verifies that both results match within floating-point precision.