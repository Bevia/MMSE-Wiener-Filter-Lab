# The Journey to the Minimum: A Step-by-Step Derivation of MMSE
## 1. Why We Seek the Minimum
The objective of a Wiener filter is to estimate a desired signal, $d(n)$, using a linear combination of input samples.
The filter output is:
$$
y(n) = W^T X(n)
$$
where:
$$
X(n) =
\begin{bmatrix}
x(n) \\
x(n-1) \\
x(n-2)
\end{bmatrix}
$$
For Version 1 of this project, we use a real-valued filter of length:
$$
N = 3
$$
The estimation error is:
$$
e(n) = d(n) - y(n)
$$
The goal is to choose the weight vector $W$ such that the average squared error is minimized.
That average squared error is called the Mean-Square Error, or MSE:
$$
\xi = E[e^2(n)]
$$
For real-valued signals, this is equivalent to:
$$
\xi = E[|e(n)|^2]
$$
For complex-valued communication systems, the more general expression is:
$$
\xi = E[|e(n)|^2] = E[e(n)e^*(n)]
$$
In this Version 1 project, we use the real-valued case.
---
## 2. Main Players in the Equation
| Quantity | Symbol | Dimension for N = 3 | Meaning |
|---|---:|---:|---|
| Desired signal | $d(n)$ | Scalar | The target signal we want to estimate |
| Input vector | $X(n)$ | $3 \times 1$ | Current and delayed input samples |
| Weight vector | $W$ | $3 \times 1$ | Adjustable FIR filter coefficients |
| Filter output | $y(n)$ | Scalar | Estimated output from the filter |
| Error signal | $e(n)$ | Scalar | Difference between target and output |
| Autocorrelation matrix | $R$ | $3 \times 3$ | Statistical structure of the input |
| Cross-correlation vector | $P$ | $3 \times 1$ | Statistical relation between input and desired signal |
| MSE | $\xi$ | Scalar | Average squared estimation error |
For $N = 3$, the input vector is:
$$
X(n) =
\begin{bmatrix}
x(n) \\
x(n-1) \\
x(n-2)
\end{bmatrix}
$$
The weight vector is:
$$
W =
\begin{bmatrix}
w_0 \\
w_1 \\
w_2
\end{bmatrix}
$$
The filter output is therefore:
$$
y(n) = W^T X(n)
$$
Expanded:
$$
y(n) =
\begin{bmatrix}
w_0 & w_1 & w_2
\end{bmatrix}
\begin{bmatrix}
x(n) \\
x(n-1) \\
x(n-2)
\end{bmatrix}
$$
So:
$$
y(n) = w_0x(n) + w_1x(n-1) + w_2x(n-2)
$$
---
## 3. The Error Signal
The error is the difference between the desired signal and the filter output:
$$
e(n) = d(n) - y(n)
$$
Substituting the filter output:
$$
e(n) = d(n) - W^T X(n)
$$
The Wiener filter tries to find the best $W$ so that $e(n)$ is as small as possible on average.
The cost function is:
$$
\xi = E[e^2(n)]
$$
Substitute the error expression:
$$
\xi = E[(d(n) - W^T X(n))^2]
$$
This is the starting point of the MMSE derivation.
---
## 4. Expanding the MSE Cost Function
Starting from:
$$
\xi = E[(d(n) - W^T X(n))^2]
$$
Expand the square:
$$
\xi = E[d^2(n) - 2d(n)W^TX(n) + (W^TX(n))^2]
$$
Using linearity of expectation:
$$
\xi = E[d^2(n)] - 2E[d(n)W^TX(n)] + E[(W^TX(n))^2]
$$
Now we simplify each term.
---
## 5. The First Term: Desired Signal Power
The first term is:
$$
E[d^2(n)]
$$
This is the expected power of the desired signal.
It is independent of the filter weights.
So when we optimize with respect to $W$, this term behaves like a constant.
---
## 6. The Second Term: Cross-Correlation
The second term is:
$$
-2E[d(n)W^TX(n)]
$$
Because $W$ is deterministic during the optimization, it can be taken outside the expectation:
$$
-2W^T E[X(n)d(n)]
$$
We define the cross-correlation vector:
$$
P = E[X(n)d(n)]
$$
Therefore:
$$
-2E[d(n)W^TX(n)] = -2W^TP
$$
Since the result is a scalar, we can also write:
$$
-2W^TP = -2P^TW
$$
Both forms are equivalent in the real-valued case.
---
## 7. The Third Term: Autocorrelation
The third term is:
$$
E[(W^TX(n))^2]
$$
Rewrite the square:
$$
(W^TX(n))^2 = W^TX(n)X^T(n)W
$$
Therefore:
$$
E[(W^TX(n))^2] = E[W^TX(n)X^T(n)W]
$$
Again, $W$ is deterministic during the optimization, so it can be taken outside the expectation:
$$
E[W^TX(n)X^T(n)W] = W^T E[X(n)X^T(n)] W
$$
We define the autocorrelation matrix:
$$
R = E[X(n)X^T(n)]
$$
Therefore:
$$
E[(W^TX(n))^2] = W^TRW
$$
---
## 8. Final MSE Cost Function
Combining the three terms gives:
$$
\xi = E[d^2(n)] - 2W^TP + W^TRW
$$
This is the MSE performance surface.
For this project:
$$
N = 3
$$
so:
$$
W =
\begin{bmatrix}
w_0 \\
w_1 \\
w_2
\end{bmatrix}
$$
$$
P =
\begin{bmatrix}
p_0 \\
p_1 \\
p_2
\end{bmatrix}
$$
$$
R =
\begin{bmatrix}
r_{00} & r_{01} & r_{02} \\
r_{10} & r_{11} & r_{12} \\
r_{20} & r_{21} & r_{22}
\end{bmatrix}
$$
So the cost function is a quadratic function of the three filter weights.
Because $R$ is an autocorrelation matrix, it is symmetric:
$$
R^T = R
$$
For a well-conditioned input signal, $R$ is also positive definite. That means the MSE surface has one unique minimum.
---
## 9. Finding the Minimum
To find the minimum, take the gradient of the MSE with respect to the weight vector $W$.
Starting from:
$$
\xi = E[d^2(n)] - 2W^TP + W^TRW
$$
The first term is constant:
$$
\nabla_W E[d^2(n)] = 0
$$
The second term gives:
$$
\nabla_W(-2W^TP) = -2P
$$
The third term gives:
$$
\nabla_W(W^TRW) = 2RW
$$
This result assumes $R$ is symmetric, which is true for a real-valued autocorrelation matrix.
Therefore, the gradient is:
$$
\nabla_W \xi = -2P + 2RW
$$
At the minimum, the gradient is zero:
$$
-2P + 2RW = 0
$$
Divide by 2:
$$
-P + RW = 0
$$
Therefore:
$$
RW = P
$$
This is the Wiener-Hopf equation.
---
## 10. The Wiener-Hopf Equation
The optimal weight vector satisfies:
$$
RW_{opt} = P
$$
If $R$ is invertible, then:
$$
W_{opt} = R^{-1}P
$$
This is the closed-form Wiener solution.
However, in real numerical software, it is usually better to solve:
$$
RW_{opt} = P
$$
directly instead of explicitly computing:
$$
R^{-1}
$$
That is why this project uses:
- MATLAB: `Wopt = R \ P`
- Python: `np.linalg.solve(R, P)`
- C: Gaussian elimination solving `R W = P`
This is numerically better than computing the inverse explicitly.
---
## 11. Minimum MSE
The general MSE equation is:
$$
\xi = E[d^2(n)] - 2W^TP + W^TRW
$$
At the optimum:
$$
W = W_{opt}
$$
so:
$$
\xi_{min} = E[d^2(n)] - 2W_{opt}^TP + W_{opt}^TRW_{opt}
$$
From the Wiener-Hopf equation:
$$
RW_{opt} = P
$$
Substitute this into the third term:
$$
W_{opt}^TRW_{opt} = W_{opt}^TP
$$
Therefore:
$$
\xi_{min} = E[d^2(n)] - 2W_{opt}^TP + W_{opt}^TP
$$
So:
$$
\xi_{min} = E[d^2(n)] - W_{opt}^TP
$$
Because the result is a scalar:
$$
W_{opt}^TP = P^TW_{opt}
$$
Therefore, we can also write:
$$
\xi_{min} = E[d^2(n)] - P^TW_{opt}
$$
Both forms are equivalent for the real-valued case.
---
## 12. Version 1 Numerical Example
In this project, we generate a real input signal $x(n)$.
The desired signal is created by passing $x(n)$ through a known three-tap system:
$$
h =
\begin{bmatrix}
0.7 \\
-0.4 \\
0.2
\end{bmatrix}
$$
The desired signal is:
$$
d(n) = 0.7x(n) - 0.4x(n-1) + 0.2x(n-2) + v(n)
$$
where $v(n)$ is small random noise.
The Wiener filter does not know the true coefficients directly. It only sees:
- the input samples $x(n)$
- the desired signal $d(n)$
From those samples, it estimates:
$$
R = E[X(n)X^T(n)]
$$
and:
$$
P = E[X(n)d(n)]
$$
Then it solves:
$$
RW_{opt} = P
$$
The expected result is that the estimated Wiener weights are close to:
$$
W_{opt} \approx
\begin{bmatrix}
0.7 \\
-0.4 \\
0.2
\end{bmatrix}
$$
They will not be exactly equal because the desired signal contains noise and because we are estimating expectations using a finite number of samples.
---
## 13. Sample-Based Estimation
In theory:
$$
R = E[X(n)X^T(n)]
$$
$$
P = E[X(n)d(n)]
$$
In code, we do not have perfect expectations. We estimate them using a finite number of samples.
If we collect $M$ training vectors, then:
$$
R \approx \frac{1}{M}X^TX
$$
and:
$$
P \approx \frac{1}{M}X^Td
$$
where $X$ is the data matrix containing many input vectors.
For example:
$$
X =
\begin{bmatrix}
x(2) & x(1) & x(0) \\
x(3) & x(2) & x(1) \\
x(4) & x(3) & x(2) \\
\vdots & \vdots & \vdots
\end{bmatrix}
$$
and:
$$
d =
\begin{bmatrix}
d(2) \\
d(3) \\
d(4) \\
\vdots
\end{bmatrix}
$$
Then:
$$
R \approx \frac{1}{M}X^TX
$$
$$
P \approx \frac{1}{M}X^Td
$$
---
## 14. Why This Becomes a Bowl
The MSE equation:
$$
\xi = E[d^2(n)] - 2W^TP + W^TRW
$$
is a quadratic function of the weights.
For $N = 1$, it is a parabola.
For $N = 2$, it is a bowl-shaped surface.
For $N = 3$, it is a bowl in three-dimensional weight space, although harder to visualize directly.
The matrix $R$ controls the shape of the bowl.
If $R$ has widely spread eigenvalues, the bowl becomes elongated. In adaptive filtering, this affects convergence speed for gradient-based methods such as steepest descent and LMS.
In this project, we first solve the Wiener problem directly using the closed-form linear system:
$$
RW_{opt} = P
$$
Later, this can be extended to iterative methods such as:
- steepest descent
- LMS
- NLMS
- RLS
---
## 15. Real-Valued Case Versus Complex-Valued Case
This Version 1 project uses real-valued signals.
Therefore:
$$
y(n) = W^TX(n)
$$
$$
R = E[X(n)X^T(n)]
$$
$$
P = E[X(n)d(n)]
$$
$$
\xi = E[e^2(n)]
$$
For complex-valued baseband communication systems, the notation changes.
The transpose becomes the Hermitian transpose:
$$
y(n) = W^HX(n)
$$
The autocorrelation matrix becomes:
$$
R = E[X(n)X^H(n)]
$$
The MSE becomes:
$$
\xi = E[|e(n)|^2]
$$
where:
$$
|e(n)|^2 = e(n)e^*(n)
$$
This is important in digital communications because I/Q signals are usually complex-valued.
---
## 16. Implementation Mapping
This project maps the theory into three languages.
### Python
Python generates the input signal, desired signal, $R$, and $P$.
It solves:
$$
RW = P
$$
using:

W_python = np.linalg.solve(R, P)

MATLAB

MATLAB verifies the same solution using:

W_matlab = R \ P;

It also plots:

* desired signal $d(n)$
* filter output $y(n)$
* error $e(n)$

C

C reads the exported $R$ and $P$ values from CSV files.

Then it solves:

$$
RW = P
$$

using Gaussian elimination with partial pivoting.

The C implementation demonstrates how the mathematical equation becomes an engineering implementation.

⸻

17. Key Takeaways

The Wiener filter finds the best linear estimator in the MMSE sense.

The core result is:

$$
RW_{opt} = P
$$

and if $R$ is invertible:

$$
W_{opt} = R^{-1}P
$$

The minimum MSE is:

$$
\xi_{min} = E[d^2(n)] - P^TW_{opt}
$$

For this Version 1 project:

* $N = 3$
* signals are real-valued
* $X(n) = [x(n), x(n-1), x(n-2)]^T$
* $R$ is $3 \times 3$
* $P$ is $3 \times 1$
* $W_{opt}$ is $3 \times 1$

The result is a complete path from:

Theory → Matrix Form → Numerical Solution → Code Implementation
Main changes I made:
I changed all display math to `$$ ... $$`, fixed every `xi` to `\xi`, removed the accidental `-RP?` line, changed the derivative with respect to vector $begin:math:text$W$end:math:text$ into the cleaner gradient notation `\nabla_W`, and kept inline math as `$...$` so GitHub renders it nicely.