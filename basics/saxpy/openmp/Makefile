# Fortran GCC compiler
CC=gcc

# compilation flags (none)
LDFLAGS=-fopenmp

# source file
SOURCE=./saxpy_openmp.c

# binary name
EXEC=a.out

all:
	$(CC) $(LDFLAGS) $(SOURCE) -o $(EXEC)
	@echo -e "----- COMPILATION DONE -----"


clean:
	rm -r $(EXEC)

