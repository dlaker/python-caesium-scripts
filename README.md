# python-caesium-scripts
caesium is the name of my laptop for those who are confused.

##comment_code.py description
###specific style commenting for source code

##compileRun.py description
compiles .c .py and .cpp files

To link to vim:

	first you must symlink compileRun.py so you can run it anywhere on your Linux system
	To do this type:
	$ sudo ln -s /path/to/pythonfile.py /usr/local/bin
	$ echo "command T !/path/to/compileRun.py" >> ~/.vimrc

Explanation:
	This works by adding a custom command to your vimrc that runs the python file at the current directory
	From there the script does the rest of the work for you! 


