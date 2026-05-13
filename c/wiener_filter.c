#include <stdio.h>
#include <math.h>
#include "wiener_filter.h"

/*
 * Solves the 3x3 linear system:
 *
 *      R W = P
 *
 * using Gaussian elimination with partial pivoting.
 *
 * This avoids computing inverse(R) explicitly.
 *
 * Returns:
 *      0 on success
 *     -1 if matrix is singular or nearly singular
 */
int solve_3x3(double R[N][N], double P[N], double W[N])
{
    double A[N][N + 1];

    // Build augmented matrix [R | P]
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            A[i][j] = R[i][j];
        }
        A[i][N] = P[i];
    }

    // Forward elimination
    for (int k = 0; k < N; k++) {

        // Partial pivoting
        int pivot_row = k;
        double max_value = fabs(A[k][k]);

        for (int i = k + 1; i < N; i++) {
            double value = fabs(A[i][k]);
            if (value > max_value) {
                max_value = value;
                pivot_row = i;
            }
        }

        // Check for singular matrix
        if (max_value < 1e-12) {
            return -1;
        }

        // Swap rows if needed
        if (pivot_row != k) {
            for (int j = k; j < N + 1; j++) {
                double temp = A[k][j];
                A[k][j] = A[pivot_row][j];
                A[pivot_row][j] = temp;
            }
        }

        // Eliminate entries below pivot
        for (int i = k + 1; i < N; i++) {
            double factor = A[i][k] / A[k][k];

            for (int j = k; j < N + 1; j++) {
                A[i][j] -= factor * A[k][j];
            }
        }
    }

    // Back substitution
    for (int i = N - 1; i >= 0; i--) {
        double sum = A[i][N];

        for (int j = i + 1; j < N; j++) {
            sum -= A[i][j] * W[j];
        }

        W[i] = sum / A[i][i];
    }

    return 0;
}