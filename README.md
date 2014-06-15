<h3>The CLOSSA Compiler</h3>
CLOSSA, or in Greek "CΛΩΣΣΑ" is a C-based language suitable for teaching high school students programming. It is designed to replace the current "ΓΛΩΣΣΑ" being taught by adding more power yet maintaining a Greek enviroment for the students to work on. It is not type-safe like ΓΛΩΣΣΑ but adds way more capabilities to the hands of the developers. Although it is not yet fully documented, we are working on making this compiler work and more documentation will follow afterwards. It is obviously not a trolling attempt. The language supports integers, doubles, longs, characters -all signed or unsigned, structs and even external libraries. Some could argue this is a badly translated version of C, although this is not the case, since this is actually using the same or similar translation patterns as the ΓΛΩΣΣΑ language. With CΛΩΣΣΑ you can do much more than with the original ΓΛΩΣΣΑ, and most importantly it compiles and runs on actual computers. You can create from a simple Hello World program to a fully featured driver for the hardware of your choice.
<br/>
<h3>Usage:</h3>

```
$ clossa -h
usage: clossa [-h] [-o OUT] [-ansi] [-p] [-w] code.clo

The CLOSSA Compiler

positional arguments:
  code.clo           The file to be compiled.

optional arguments:
  -h, --help         show this help message and exit
  -o OUT, --out OUT  Name of the output file
  -ansi, --ansi      Follow the CLOSSA ANSI strict rules
  -p, -pedantic      Follow the strict ISO CLOSSA
  -w, -Werror        Treat all warnings as errors

Licensed under modified NPOSL-3.0
$
```

<br/>

