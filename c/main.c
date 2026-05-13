#include <stdio.h>
#include <stdlib.h>
#include "wiener_filter.h"

/*
 * Simple CSV reader for a 3x3 matrix.
 */
int read_matrix_3x3(const char *filename, double R[N][N])
{
    FILE *file = fopen(filename, "r");

    if (!file) {
        printf("Error: could not open %s\n", filename);
        return -1;
    }

    for (int i = 0; i < N; i++) {
        if (fscanf(file, "%lf,%lf,%lf",
                   &R[i][0], &R[i][1], &R[i][2]) != 3) {
            printf("Error: invalid matrix format in %s\n", filename);
            fclose(file);
            return -1;
        }
    }

    fclose(file);
    return 0;
}

/*
 * Simple CSV reader for a 3-element vector.
 */
int read_vector_3(const char *filename, double P[N])
{
    FILE *file = fopen(filename, "r");

    if (!file) {
        printf("Error: could not open %s\n", filename);
        return -1;
    }

    for (int i = 0; i < N; i++) {
        if (fscanf(file, "%lf", &P[i]) != 1) {
            printf("Error: invalid vector format in %s\n", filename);
            fclose(file);
            return -1;
        }
    }

    fclose(file);
    return 0;
}

int write_vector_3(const char *filename, double W[N])
{
    FILE *file = fopen(filename, "w");

    if (!file) {
        printf("Error: could not write %s\n", filename);
        return -1;
    }

    for (int i = 0; i < N; i++) {
        fprintf(file, "%.12f\n", W[i]);
    }

    fclose(file);
    return 0;
}

int main(void)
{
    double R[N][N];
    double P[N];
    double W[N];

    const char *r_file = "../data/R_matrix.csv";
    const char *p_file = "../data/P_vector.csv";
    const char *w_file = "../data/weights_c.csv";

    printf("MMSE Wiener Filter Lab - C Implementation\n");
    printf("-----------------------------------------\n");

    if (read_matrix_3x3(r_file, R) != 0) {
        return 1;
    }

    if (read_vector_3(p_file, P) != 0) {
        return 1;
    }

    int status = solve_3x3(R, P, W);

    if (status != 0) {
        printf("Error: failed to solve R W = P\n");
        return 1;
    }

    printf("Estimated Wiener weights from C:\n");
    for (int i = 0; i < N; i++) {
        printf("W[%d] = %.12f\n", i, W[i]);
    }

    if (write_vector_3(w_file, W) != 0) {
        return 1;
    }

    printf("\nWeights written to: %s\n", w_file);

    return 0;
}