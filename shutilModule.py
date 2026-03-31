import shutil
# shutil.rmtree("dir") #removes the directory using shutil module as shutil removes files as well as directories. 

# rmtree is remove directory tree meaning removes all the directory and its contents.

shutil.copy("newtext.txt" , "JohnDoe.txt")  #JohnDoe.txt file got its content overwritten with newtext.txt file content. 

shutil.move("JohnDoe.txt" , "dir/") #Moves the johndoe text file to a new directory "dir"