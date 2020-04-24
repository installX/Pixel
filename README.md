![os logo](https://storage.googleapis.com/replit/images/1587636846745_1fdf330d89fbadafc82affb1c4daab9e.png)

```mywindow
vile :This is a  cool language made in python:
cover = :what is your name?|: = name
cover = :Pixmicro: = name/input
 vile :Hi,name//input:
```
This is how to do inputs in Pixel language.


By **PIXMICRO.INC**
Patners with **ONEYX PRO**

To print color do this:
```mywindow2
vile <color> :This is how to print color in Pixel: <color>
```
**This is the code that took to create Pixel.**
``` mywindow3
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
```
