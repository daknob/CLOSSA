#!/usr/bin/python
#coding=utf8
import argparse, os, sys, random, codecs

Config = argparse.ArgumentParser(prog="clossa", description="The CLOSSA Compiler", epilog="Licensed under modified NPOSL-3.0")
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
if(len(Config.out[0]) == 1):
	SynthCommand += "-o " + Config.out[0][0] + " "
if(Config.ansi == True):
	SynthCommand += "-ansi "
if(Config.p == True):
	SynthCommand += "-pedantic "
if(Config.w == True):
	SynthCommand += "-Werror "

Board = {
	#	Variables
	u"ΑΚΕΡΑΙΟΣ": "int",
	u"ΠΡΑΓΜΑΤΙΚΟΣ": "double",
	u"ΧΑΡΑΚΤΗΡΑΣ": "char",
	u"ΔΟΜΗΜΑ": "struct",
	u"ΕΝΩΣΗ": "union",
	u"ΑΡΧΕΙΟ": "FILE",
	u"ΚΕΝΟ": "void",
	u"ΠΡΟΣΗΜΑΣΜΕΝΟΣ": "signed",
	u"ΜΕΓΑΛΟΣ": "long",
	u"ΜΗ_ΠΡΟΣΗΜΑΣΜΕΝΟΣ": "unsigned",
	u"ΕΞΩΤΕΡΙΚΟ" : "extern",

	#	User-Created Functions
	u"ΑΡΧΙΚΗ": "main",
		
	#	Built-in Functions
	u"ΕΚΤΥΠΩΣΕ": "printf",
	u"ΔΙΑΒΑΣΕ": "scanf",
	u"ΔΙΑΘΕΣΕ": "malloc",
	u"ΕΛΕΥΘΕΡΩΣΕ": "free",
	u"ΕΠΑΝΑΔΙΑΘΕΣΕ": "realloc",
	u"ΚΑΘΑΡΑ_ΔΙΑΘΕΣΕ": "calloc",
	u"ΔΙΑΒΑΣΕ_ΑΡΧΕΙΟ": "fgets",
	u"ΓΡΑΨΕ_ΑΡΧΕΙΟ": "fputs",
	u"ΔΙΑΒΑΣΕ_ΧΑΡΑΚΤΗΡΑ": "getc",
	u"ΓΡΑΨΕ_ΧΑΡΑΚΤΗΡΑ": "putc",
	u"ΤΕTΡΙ": "sqrt",
	u"ΔΥΝ" : "pow",
	
	#	Preprocessor	
	u"ΕΙΣΑΓΩΓΗ": "include",
	u"ΟΡΙΣΜΟΣ": "define",
	u"ΟΡΙΣΜΟΣ_ΤΥΠΟΥ": "typedef",
		
	#	Defines
	u"\\Ν": "\\n",
	u"ΤΑ": "EOF",
	u"ΤΙΠΟΤΑ": "NULL",
	u"ΒΑΣΕΙΣ": "stdin",
	u"ΒΑΣΕΞΟΔ": "stdout",
	u"ΒΑΣΛΑΘΟΣ": "stderr",

	#	Control Flow Manipulation
	u"ΑΝ": "if",
	u"ΟΣΟ": "while",
	u"ΚΑΝΕ": "do",
	u"ΑΛΛΙΩΣ": "else",
	u"ΑΛΛΙΩΣ_ΑΝ": "else if",
	u"ΣΤΑΜΑΤΑ": "break",
	u"ΣΥΝΕΧΙΣΕ": "continue",
	u"ΕΠΕΣΤΡΕΨΕ": "return",
	u"ΠΑΝΕ_ΣΤΟ": "goto",

	#	string.h
	u"ΣΥΓΚΜΝΗ" : "memcmp",
	u"ΑΝΤΣΥΜ" : "strcpy",
	u"ΣΥΓΚΡΣΥΜ" : "strcmp",
	u"ΕΝΩΣΗΣΥΜ" : "strcat",
	u"ΔΙΑΧΣΥΜ" : "strtok",
	u"ΑΝΑΖΣΥΜ" : "strstr",
    
	#	Libraries
	u"ΒΑΣΒΙΒ": "stdlib.h",
	u"ΣΥΜΒΟΛΟΣΕΙΡΑ": "string.h",
	u"ΒΑΣΕΟ": "stdio.h"

}

try:
    sourcefile = codecs.open(Config.filename[0], "r", encoding="utf-8")
    sourcecode = sourcefile.read()
    for greek in Board:
    	sourcecode = sourcecode.replace(greek, Board[greek])
    tempname = str(random.randint(1,999999999999)) + ".c"
    tempfile = codecs.open(tempname, "w+", encoding="utf-8")
    tempfile.write(sourcecode)
    tempfile.close()
    sourcefile.close()
    SynthCommand += tempname
    os.system(SynthCommand)
    os.remove(tempname)
except:
    print "An error occured while reading / writing to files."
