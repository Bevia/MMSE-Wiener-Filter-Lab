#ifndef WIENER_FILTER_H   // "if WIENER_FILTER_H is NOT defined yet..."
#define WIENER_FILTER_H   // "...define it now (mark this file as seen)..."

#define N 3 // Filter order (3 for 3x3 matrix)

int solve_3x3(double R[N][N], double P[N], double W[N]);

#endif