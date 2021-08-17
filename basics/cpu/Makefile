# C++ compiler
CPP=g++
# Fortran compiler
FC=gfortran

# compilation flags
CDFLAGS=-std=gnu++17
FDFLAGS=

# source files
SOURCE_ARITH1=./arithmetic/single_double.f90
SOURCE_ARITH2=./arithmetic/single_double.cpp
SOURCE_ARRAY1=./arrayops/vector.f90
SOURCE_ARRAY2=./arrayops/vector.cpp
SOURCE_ARRAY3=./arrayops/matrix.f90
SOURCE_ARRAY4=./arrayops/matrix.cpp


# path to where binary is going (has to be previously created)
PATH_BIN=./bin

# binary names
EXEC_ARITH1=single_double_fortran
EXEC_ARITH2=single_double_cpp
EXEC_ARRAY1=vector_fortran
EXEC_ARRAY2=vector_cpp
EXEC_ARRAY3=matrix_fortran
EXEC_ARRAY4=matrix_cpp

all:
	$(FC) $(FDFLAGS) $(SOURCE_ARITH1) -o $(PATH_BIN)/$(EXEC_ARITH1)
	$(CPP) $(CDFLAGS) $(SOURCE_ARITH2) -o $(PATH_BIN)/$(EXEC_ARITH2)
	$(FC) $(FDFLAGS) $(SOURCE_ARRAY1) -o $(PATH_BIN)/$(EXEC_ARRAY1)
	$(CPP) $(CDFLAGS) $(SOURCE_ARRAY2) -o $(PATH_BIN)/$(EXEC_ARRAY2)
	$(FC) $(FDFLAGS) $(SOURCE_ARRAY3) -o $(PATH_BIN)/$(EXEC_ARRAY3)
	$(CPP) $(CDFLAGS) $(SOURCE_ARRAY4) -o $(PATH_BIN)/$(EXEC_ARRAY4)
	@echo -e "----- COMPILATION DONE -----"

arithmetic:
	$(FC) $(FDFLAGS) $(SOURCE_ARITH1) -o $(PATH_BIN)/$(EXEC_ARITH1)
	$(CPP) $(CDFLAGS) $(SOURCE_ARITH2) -o $(PATH_BIN)/$(EXEC_ARITH2)
	@echo -e "----- ARITHMETIC COMPILATION DONE -----"


arrayops:
	$(FC) $(FDFLAGS) $(SOURCE_ARRAY1) -o $(PATH_BIN)/$(EXEC_ARRAY1)
	$(CPP) $(CDFLAGS) $(SOURCE_ARRAY2) -o $(PATH_BIN)/$(EXEC_ARRAY2)
	$(FC) $(FDFLAGS) $(SOURCE_ARRAY3) -o $(PATH_BIN)/$(EXEC_ARRAY3)
	$(CPP) $(CDFLAGS) $(SOURCE_ARRAY4) -o $(PATH_BIN)/$(EXEC_ARRAY4)
	@echo -e "----- ARRAYOPS COMPILATION DONE -----"


clean:
	rm -r $(PATH_BIN)/*

.PHONY: arithmetic, arrayops
