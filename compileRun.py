#!/usr/bin/python
import os, glob


def getFile():

	if (glob.glob("*.c") != []):
		return [x for x in glob.glob("*.c")]
	else:
		pass

	if (glob.glob("*.py") != []):
		return [x for x in glob.glob("*.py")]
	else:
		pass

	if (glob.glob("*.cpp") != []):
		return [x for x in glob.glob("*.cpp")]
	else:
		pass
	
def enterCommand(filename):

	os.system("clear")
	filename = "".join(filename[0])

	if (filename[-2:] == ".c"):
		print("compiling ", filename)
		newfilename = filename.strip('.c')
		os.system("gcc -o %s %s" %(newfilename, filename))
	else:
		pass

	if (filename[-3:] == ".py"):
		print("running ", filename)
		os.system("python %s" %(filename))
	else:
		pass

	if (filename[-4:] == ".cpp"):
		print("compiling ", filename)
		newfile = filename.strip('.cpp')
		os.system("g++ -o %s %s" %(newfile, filename))

class main():
	filename = getFile()
	enterCommand(filename)
