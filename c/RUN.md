cd c
make
make run
cd ..

---

## This created the filter's weights

The Makefile automates building the C project. Specifically:

make / make all — compiles main.c and wiener_filter.c into an executable named mmse_wiener using gcc with warnings (-Wall -Wextra) and optimization (-O2), linking the math library (-lm).

make run — builds (if needed) then immediately runs the executable.

make clean — deletes the compiled binary to force a fresh build next time.