# Fortran GCC compiler
FC=gfortran

# compilation flags (none))
FDFLAGS=

# source file
SOURCE=./matmul_serial.f90

# binary name
EXEC=matmul_serial

all:
	$(FC) $(FDFLAGS) $(SOURCE) -o $(EXEC)
	@echo -e "----- COMPILATION DONE -----"


clean:
	rm -r $(EXEC)

