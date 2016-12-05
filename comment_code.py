#!/usr/bin/python
"""
Author: Derek Laker
Special Thanks To: Shane Sorensen
Description: Quick commenting script for the lazy. Sample output in the readme.md
"""

import os
file_name = input("What is the filename: ")
chars = words = lines = max_c = 0
with open(file_name, 'r') as in_file:
	for line in in_file:
		lines += 1
		words += len(line.split())
		chars = len(line)
		if (max_c < chars):
			max_c = chars
in_file.close()		

spaces = int(max_c) + 10
new_file = (file_name + "_")

with open(file_name, 'r') as src:
	with open(new_file, 'w') as dest:
		for line in src:
			chars = len(line)
			print ("\n")
			print (line)
			u_input = input("Describe this line of code: " )	
			if (len(u_input) < 1):
				dest.write('%s\n' % (line.rstrip('\n')))
			else:
				dest.write('%s%s\n' % (line.rstrip('\n'),(" " * (spaces - chars) + "//"+ u_input))) 
src.close()
dest.close()

os.rename(file_name, file_name + ".src")
os.rename(new_file, file_name)
print("\nYour outputfile is named: %s\n" % file_name)
print("The source file is now renamed to: %s\n" % (file_name + ".src"))
