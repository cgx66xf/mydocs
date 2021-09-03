import os

"""
print(dir(os)) #this will output all the attributes and methods of the module
print(os.getcwd()) #pwd
os.chdir('/home/troll/Desktop') #cd 
print(os.listdir()) #ls
os.mkdir('dir1') #mkdir
os.mkdirs('dir1/subdir1') #mkdir but it also creates subdirs
os.rmdir('dir1') #rmdir
os.removedirs('dir1/subdir1')
os.rename('test.txt', 'newname.txt')
print(os.stat('test.txt')) #gives us stats about a file

for dirpath, dirnames, filenames in os.walk(os.getcwd):    #this yields a 3 value tuple of a top down file tree
	print("Current path:", dirpath)
	print("Directories:", dirnames)
	print("Files", filenames)
	
print(os.environ())  #this outputs the enviremont variables
print(os.environ.get('HOME')) #prints the enviremont variable of the home directory 
os.path.join(os.environ.get('HOME'), 'test.txt')  #joins the paths

print(os.path.basename('/home/Desktop/code/os.py')    #outputs os.py
print(os.path.dirname('/home/Desktop/code/os.py')   #outputs /home/Desktop/code
print(os.path.split('/home/Desktop/code/os.py')  #outputs ('/home/Desktop/code', 'os.py')
os.path.exists('/dir1/dir2/test.txt')  #checks if path exists
print(os.path.isdir('/dir1/dir2')   #outputs True if its a directory
print(os.path.isfile('/dir1/dir2')  #outputs True if its a file
print(os.path.splitext('/dir1/dir2/test.txt')  #outputs ('/dir1/dir2/test', '.txt')
























"""
