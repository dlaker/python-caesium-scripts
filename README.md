# python-caesium-scripts
caesium is the name of my laptop for those who are confused.

##compileRun.py description
compiles .py, .c, .cpp files

To install:
	git clone https://github.com/dereklaker/python-caesium-scripts/ <target dir (optional)>

Explanation:
	This works by adding a custom command to your vimrc that runs the python file at the current directory
	From there the script does the rest of the work for you! 

To link to vim:

	first you must symlink compileRun.py so you can run it anywhere on your Linux system
	To do this type:
	$ sudo ln -s /path/to/pythonfile.py /usr/local/bin/compileRun
	$ echo "command T !compileRun" >> ~/.vimrc

Notes:
	This can also be used to compile/run other types of files as well.
	In order to do this edit the source code with another glob block and put in the desired file extension
	You will also have to add in a new if check to see what the filetype is and run the desired command accordingly
	
	Example:
		python code

		if (glob.glob("*.sh") != []):
			return [x for x in glob.glob("*.sh")]
		else:
			pass
	
		...
	
		if (filename[-3:] == ".sh"):
			print("running ", filename)
			os.system("bash %s" %(filename))
		else:
			pass

##comment_code.py description
specific style commenting for source code
see Shane's Github for more information
http://github.com/Sorensen0303

