# RUN IT

## Reproducing the MMSE Wiener Filter Lab — Version 1
This document explains how to reproduce the Version 1 workflow of the MMSE Wiener Filter Lab.
Version 1 uses:
- Real-valued signals
- Filter length `N = 3`
- MATLAB as the reference model
- C as the implementation under test
- Python as the validation/comparison tool
The goal is to verify that MATLAB and C compute the same optimal Wiener weights:

```text
R W = P
```

where:

* R is the autocorrelation matrix
* P is the cross-correlation vector
* W is the optimal Wiener weight vector

⸻

1. Project Structure

The project should be organized as follows:

```text
MMSE-Wiener-Filter-Lab/
│
├── data/
│   ├── R_matrix.csv
│   ├── P_vector.csv
│   ├── input_signal.csv
│   ├── desired_signal.csv
│   ├── weights_matlab.csv
│   ├── weights_c.csv
│   ├── output_matlab.csv
│   └── error_matlab.csv
│
├── matlab/
│   └── MMSE.m
│
├── c/
│   ├── main.c
│   ├── wiener_filter.c
│   ├── wiener_filter.h
│   └── Makefile
│
├── python/
│   └── compare_weights.py
│
└── docs/
    └── mmse_derivation.md
```

⸻

2. Run the MATLAB Reference Model

In MATLAB or MATLAB Online, run:

run('MMSE.m')

The MATLAB script generates the test data and solves the Wiener-Hopf equation using:

W_matlab = R \ P;

This is the MATLAB reference solution.

After running MATLAB, it should generate the following files:

input_signal.csv
desired_signal.csv
R_matrix.csv
P_vector.csv
weights_matlab.csv
output_matlab.csv
error_matlab.csv

If you are using MATLAB Online, download these CSV files to your computer.

⸻

3. Copy the MATLAB CSV Files into the Local Project

Place the MATLAB-generated CSV files into the local data/ folder:

MMSE-Wiener-Filter-Lab/data/

At minimum, the C validation requires:

R_matrix.csv
P_vector.csv
weights_matlab.csv

The full dataset should look like this:

data/
├── R_matrix.csv
├── P_vector.csv
├── input_signal.csv
├── desired_signal.csv
├── weights_matlab.csv
├── output_matlab.csv
└── error_matlab.csv

⸻

4. Build and Run the C Implementation

From the project root, go into the c/ folder:

cd c

Clean any previous build:

make clean

Build the C program:

make

Run it:

make run

The C implementation reads:

../data/R_matrix.csv
../data/P_vector.csv

or, depending on your final Makefile/path setup:

data/R_matrix.csv
data/P_vector.csv

It then solves:

R W = P

using Gaussian elimination with partial pivoting.

The C program writes:

data/weights_c.csv

or:

../data/weights_c.csv

depending on where the program is executed from.

Return to the project root:

cd ..

⸻

5. Compare MATLAB and C Weights with Python

Run the Python comparison script from the project root:

python3 python/compare_weights.py

The script reads:

data/weights_matlab.csv
data/weights_c.csv

It prints:

MATLAB weights
C weights
Difference MATLAB - C
Maximum absolute difference

A successful result should look similar to:

MMSE Wiener Filter Lab - MATLAB vs C Weight Comparison
------------------------------------------------------
MATLAB weights:
[ 0.70100109 -0.40017179  0.20148352]
C weights:
[ 0.70100109 -0.40017179  0.20148352]
Difference MATLAB - C:
[ 4.79061235e-13  1.36002321e-13 -8.90121310e-14]
Maximum absolute difference: 4.790612351258e-13

⸻

6. Validation Criteria

The validation passes if the maximum absolute difference is very small.

Recommended tolerance:

1e-9

If:

maximum absolute difference < 1e-9

then the MATLAB and C solutions match within floating-point precision.

Example:

Maximum absolute difference: 4.79e-13

This is a successful result.

⸻

7. What This Proves

The validation confirms that:

MATLAB generated R and P
MATLAB solved R W = P
C read the same R and P
C solved R W = P
Python compared both results
MATLAB and C weights matched within numerical precision

Therefore, the C implementation correctly solves the same Wiener-Hopf system as the MATLAB reference model.

⸻

8. Common Mistakes

Mistake 1: Forgetting to rerun C after changing the CSV files

If you replace R_matrix.csv or P_vector.csv, you must rerun the C program.

Otherwise, weights_c.csv may still contain old results.

Run:

cd c
make clean
make
make run
cd ..

Then compare again:

python3 python/compare_weights.py

Mistake 2: MATLAB and C using different datasets

The following files must all belong to the same MATLAB run:

R_matrix.csv
P_vector.csv
weights_matlab.csv
weights_c.csv

If R_matrix.csv and P_vector.csv come from one run, but weights_matlab.csv comes from another run, the comparison will fail.

Mistake 3: Running the C program from the wrong folder

If the C code uses relative paths like:

../data/R_matrix.csv

then the program must be run from inside the c/ folder.

If the C code uses:

data/R_matrix.csv

then the program must be run from the project root.

The relative paths must match the working directory.

⸻

9. Expected Final Result

For the current Version 1 dataset, the expected weights are approximately:

W =
[ 0.70100109
 -0.40017179
  0.20148352 ]

These are close to the true system used to generate the desired signal:

h =
[ 0.7
 -0.4
  0.2 ]

The small difference is expected because the desired signal includes random noise and the expectations are estimated from a finite number of samples.

⸻

10. Final Reproduction Command Sequence

From the local project root:

cd c
make clean
make
make run
cd ..
python3 python/compare_weights.py

Expected result:

PASS: MATLAB and C weights match within tolerance.

---

## RE-RUN IT

If you want to re-rerun it, start here.. then go to previous RUN IT

rm data/*.csv

now /data should be empty...

Then regenerate the MATLAB CSV files first:

run('MMSE.m')

Download/copy the generated CSV files into your local:

MMSE-Wiener-Filter-Lab/data/

Then rerun C:

cd c
make clean
make
make run
cd ..

Then compare:

python3 python/compare_weights.py

Expected final result:

PASS: MATLAB and C weights match within tolerance.

The important rule: after deleting or replacing R_matrix.csv and P_vector.csv, always rerun C so weights_c.csv belongs to the same dataset.