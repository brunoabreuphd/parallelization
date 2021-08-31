# Fortran GCC compiler
FC=gfortran

# compilation flags (none))
FDFLAGS=-fopenmp

# source file
SOURCE=./dotprod_openmp.f90

# binary name
EXEC=a.out

all:
	$(FC) $(SOURCE) -o $(EXEC) $(FDFLAGS)
	@echo -e "----- COMPILATION DONE -----"


clean:
	rm -r $(EXEC)

