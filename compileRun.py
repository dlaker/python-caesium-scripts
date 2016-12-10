#!/usr/bin/python
import os, glob

class main():

	def getFile(self):

		if (glob.glob("*.c") != []):
			return [x for x in glob.glob("*.c")]
		else:
			pass

		if (glob.glob("*.py") != []):
			return [x for x in glob.glob("*.py")]
		else:
			pass
		
	def enterCommand(self, filename):

		os.system("clear")
		filename = "".join(filename[0])

		if (filename[-2:] == ".c"):
			newfilename = filename.strip('.c')
			os.system("gcc -o %s %s" %(newfilename, filename))
		else:
			pass

		if (filename[-3:] == ".py"):
			os.system("python %s" %(filename))
		else:
			pass
			
if __name__ == '__main__':
	filename = main().getFile()
	main().enterCommand(filename)
