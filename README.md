# parallelization
Series of examples on how to optmize/parallelize serial codes.

## [basics](./basics)
This folder has some basic exercises that optimize and parallelize very simple serial codes.
### 1. [matmul](./basics/matmul)
This is an example of a matrix multiplication code. It is currently offered in Fortran. It was tested with GCC 10.2.1 20201220.
#### [serial](./basics/matmul/serial)
Serial code in Fortran. Makefile is available for compilation with GCC. 
#### [compiler_opt](./basics/matmul/compiler_opt)
This folder contains the serial code and a supporting Python script and Jupyter notebook that compiles and runs the code with every single individual GCC optmization flag (listed [here](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html)).
### 2. [saxpy](./basics/saxpy)
This is an example of a Single-precision A\*X plus Y code. It is currently offered in C. It was tested with GCC 10.2.1 20201220.
#### [serial](./basics/saxpy/serial)
Serial code in C. Makefile is available for compilation with GCC. 
#### [compiler_opt](./basics/matmul/compiler_opt)
This folder contains the serial code and a supporting Python script and Jupyter notebook that compiles and runs the code with every single individual GCC optmization flag (listed [here](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html)).





# CITE-ME
As all other projects in this GitHub, the programs are protected by a license/copyright that requires proper acknowledgement. Please refer to: https://github.com/babreu-ncsa/cite-me.
