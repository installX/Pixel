from termcolor import cprint
strn = "12345678"

data = open('code.pix', 'r').read()
i = "12345"
ic = "123456"
ix = "123456789111"


def datafile():
	tok = ""
	for char in data:
		tok += char
		if tok == "\n":
			tok = ""

		if tok == "vile :":
			print(tok[:5])
			tok = ""

datafile()

def parse(token):
	
	if "vile :" or "vile ::" or "vile 2" or "vile 3" or "vile 4" or "vile 5" or "vile 6" or "vile 7" or "vile 8" or "vile 9" and "\n" in token:
		print(token[len(i):])


	if "vile :" in token:
		cp = cprint(token[len(i):], 'red')
		print(str(cp))

parse(data)

#input

#button

#cprint no text

#website for Language

#more than one line of code

#package for language

#make runable

#____|/Help code OS in language\|____#

#code in language in other repls

#Do updates in language if needed

import os
os.system('python3 language.py code.pix')
