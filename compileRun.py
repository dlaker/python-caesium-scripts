#!/usr/bin/python
import os, glob

class main():

	def getFile(self):

		for file in glob.glob("*.c"):
			filename = file
		if (len(filename)) < 1:
			filename = glob.glob("*.py")
			return filename
		
	def enterCommand(self, filename):

		os.system("clear")
		filename = "".join(filename)
		newfilename = filename.strip('.c')
		os.system("gcc -o %s %s" %(newfilename, filename))
			
if __name__ == '__main__':
	filename = main().getFile()
	main().enterCommand(filename)
