# Fortran GCC compiler
FC=gfortran

# compilation flags (none)
FDFLAGS=

# source file
SOURCE=./dotprod_serial.f90

# binary name
EXEC=a.out

all:
	$(FC) $(FDFLAGS) $(SOURCE) -o $(EXEC)
	@echo -e "----- COMPILATION DONE -----"


clean:
	rm -r $(EXEC)

