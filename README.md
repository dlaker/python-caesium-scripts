# python-caesium-scripts
caesium is the name of my laptop for those who are confused.

##comment_code.py description
specific style commenting for source code

##compileRun.py description
compiles .py, .c, .cpp files

To link to vim:

	first you must symlink compileRun.py so you can run it anywhere on your Linux system
	To do this type:
	$ sudo ln -s /path/to/pythonfile.py /usr/local/bin
	$ echo "command T !/path/to/compileRun.py" >> ~/.vimrc

Explanation:
	This works by adding a custom command to your vimrc that runs the python file at the current directory
	From there the script does the rest of the work for you! 

Notes:
	This can also be used to compile/run other types of files as well.
	In order to do this edit the source code with another glob block and put in the desired file extension
	You will also have to add in a new if check to see what the filetype is and run the desired command accordingly
	
	Example:
		```python
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
		```

