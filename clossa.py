#!/usr/bin/python
#coding=utf8
import argparse, os

Config = argparse.ArgumentParser(prog="clossa", description="The CLOSSA Compiler", epilog="Free Software in Public Domain")
Config.add_argument("-o", "--out", action="append", nargs=1, help="Name of the output file")
Config.add_argument("-ansi", "--ansi", action="store_true", help="Follow the CLOSSA ANSI strict rules")
Config.add_argument("-p", "-pedantic", action="store_true", help="Follow the strict ISO CLOSSA")
Config.add_argument("-w", "-Werror", action="store_true", help="Treat all warnings as errors")
Config.add_argument('filename', metavar='code.clo', nargs=1, help='The file to be compiled.')
Config = Config.parse_args()

SynthCommand = "gcc "

if(len(Config.filename) != 1):
	print("You can only compile a single CLOSSA file.")
	exit(9)
if(Config.filename[0][::-1][0:4] != "olc."):
	print("You can only compile a CLOSSA (.clo) file.")
	exit(8)
SynthCommand += Config.filename[0] + " "
if(Config.out == True):
	SynthCommand += "-o " + Config.out + " "
if(Config.ansi == True):
	SynthCommand += "-ansi "
if(Config.p == True):
	SynthCommand += "-pedantic "
if(Config.w == True):
	SynthCommand += "-Werror "

Board = {
	"ΑΚΕΡΑΙΟΣ": "int",
	"ΠΡΑΓΜΑΤΙΚΟΣ": "double",
	"ΧΑΡΑΚΤΗΡΑΣ": "char",
	"ΔΟΜΗΜΑ": "struct",
	"ΕΝΩΣΗ": "union"

	"ΚΥΡΙΑ": "main",
	
	"ΕΚΤΥΠΩΣΕ": "printf",
	"ΔΙΑΒΑΣΕ": "scanf",
	"ΔΙΑΘΕΣΕ": "malloc",
	"ΕΛΕΥΘΕΡΩΣΕ": "free",
	"ΕΠΑΝΑΔΙΑΘΕΣΕ": "realloc",
	"ΚΑΘΑΡΑ_ΔΙΑΘΕΣΕ": "calloc",
	"ΔΙΑΒΑΣΕ_ΑΡΧΕΙΟ": "fgets",
	"ΓΡΑΨΕ_ΑΡΧΕΙΟ": "fputs",
	"ΔΙΑΒΑΣΕ_ΧΑΡΑΚΤΗΡΑ": "getc",
	"ΓΡΑΨΕ_ΧΑΡΑΚΤΗΡΑ": "putc",
	"ΤΕTΡΙ": "sqrt",
	"ΔΥΝ" : "pow",
	"ΑΝΤΣΥΜ" : "strcpy",
	"ΑΝΤΜΝΗ" : "memcpy",
	"ΣΥΓΚΣΥΜ" : "strcmp",
	"ΣΥΓΚΜΝΗ" : "memcmp"


	"ΕΠΕΣΤΡΕΨΕ": "return",

	"ΕΙΣΑΓΩΓΗ": "include",
	
	"\\Ν": "\\n",

	"ΑΝ": "if",
	"ΟΣΟ": "while",
	"ΚΑΝΕ": "do",
	"ΑΛΛΙΩΣ": "else",
	"ΑΛΛΙΩΣ_ΑΝ": "else if",
	"ΣΤΑΜΑΤΑ": "break",
	"ΣΥΝΕΧΙΣΕ": "continue",

	"ΒΑΣΒΙΒ": "stdlib.h",
	"ΣΥΜΒΟΛΟΣΕΙΡΑ": "string.h",
	"ΒΑΣΕΟ": "stdio.h"
}

