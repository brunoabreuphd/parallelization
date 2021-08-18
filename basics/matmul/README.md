# matmul

This is a simple Fortran code that performs matrix multiplication. The idea here is that we have three matrices N, M, P such that P = M x N. In terms of each element of the product, we have

![equation](https://latex.codecogs.com/gif.latex?P_%7Bij%7D%20%3D%20%5Csum_%7Bk%7D%20M_%7Bik%7DN_%7Bkj%7D)

Therefore, to calculate all the elements of P, a triple (nested) do loop is required. This is obviously the intensive part of the computation and we will test how different compiler optimization options change the total run time of the calculation. We will be using a Fortran code and GCC compilers. The original code uses 1000x1000 matrices. I ran this on a Macbook, with GCC 10.2.1 20201220.

## [serial](./serial)
This folder contains the Fortran serial code that performs matrix multiplication, [matmul_serial.f90](./serial/matmul_serial.f90), and a [Makefile](./serial/Makefile) to help users with no compilation experience (if that is your case, just bring your Terminal session to the [serial](./serial) folder and type *make*). The binary will have the default *a.out* name. Execute the binary and check the output for the multiplication time.

## [compiler_opt](./compiler_opt)
This folder contains the serial code and supporting Python files. The GCC compilation flags that perform optimization can be found [here](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html) (there are many). If you do not want to deal with Python, just edit the *FDFLAGS* variable in the [Makefile](./compiler_opt/Makefile) to include some of the flags, compile it and run it to see the optimized run time. If you are okay with Python, you may want to check:
- [gcc_opt_flags.ipynb](./compiler_opt/gcc_opt_flags.ipynb): This is a Jupyter notebook that calls GCC (gfortran) with every single compilation flag for optimization listed in the GCC documentation, then plots the times. 
- [gcc_opt_flags.py](./compiler_opt/gcc_opt_flags.ipynb): It does the same as the notebook, but I provided it in case you want to call it from a place where you don't have access to a Jupyter notebook (a remote cluster, for instance). The graphs are saved to *png* files.
These Python codes do not require fancy imports: pretty much any base Anaconda distribution that I am aware of should have the necessary packages already installed. However, in case it does not work for you, the environment is specified in [conda_env.yml](./compiler_opt/conda_env.yml).

### Conclusions
- None of the flags listed in the Optimize Options of the GNU Compiler documentation changes the execution time of a matrix multiplication significantly.
- Instead of trying individual options, one should always first use the bundled options (-Ox)
- For this simple code, level 2 optimization reduces execution time dramatically
- Compiler optimizations can be obscure. Make sure your code runs without errors before using them (writing a simple test is a good practice)

### Further exercises
There are several things that you can do to improve your experience and bring it closer to your target situation. Here are a few suggestions:
- Change the matrix size (go larger). How does the compiler optimization work?
- Re-write this code in a different language (such as C/C++). What happens?
- Try to use different compilers (Intel, for instance). What are the flags available for optimization? How do they work?

If you do these changes or any others that you wish, let me know about your results!
