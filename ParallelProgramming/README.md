I have use `gcc` to compile the c code available here on OSX

## Install

- Install GCC with OpenMP as default gcc in Mac is CLANG and doesn't have OMP. 
- Install gcc via home brew. `brew install gcc`
- maybe in your shell you can use `alias gcc=gcc-11` to make it easy (and follow online tutorials `make`)


## Compile and run
for example the hello world example can be run as follows

- to compile run `gcc -fopenmp hello.c  -o hello`
- run the example by `./hello`
