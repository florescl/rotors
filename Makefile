CC = gcc
LIBS = -lm -lgsl -lgslcblas
OPT = -g -O0
#OPT=-O4
CFLAGS = $(OPT) -Wall 
LDFLAGS = $(OPT) -Wall 


SRCS = Z3_rotors.c 4slice_split.c random_rotors.c

all: Z3_rotors 4slice_split random_rotors

random_rotors: random_rotors.o
	$(CC) $(LDFLAGS) $^ $(LIBS) -o $@

Z3_rotors: Z3_rotors.o 
	$(CC) $(LDFLAGS) $^ $(LIBS) -o $@

4slice_split: 4slice_split.o
	$(CC) $(LDFLAGS) $^ $(LIBS) -o $@

clean: 
	/bin/rm -f 4slice_split.o Z3_rotors.o random_rotors.o