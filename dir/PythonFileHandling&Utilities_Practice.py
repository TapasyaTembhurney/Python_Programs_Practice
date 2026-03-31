# Create a text file notes.txt using Python and write "Learning Python is fun!" into it.
# Open notes.txt , read its content and print it in console.

with open("notes.txt" , "w") as f:
    f.write("Learning Python is Fun!.")

with open("notes.txt" , "r") as f:
    print(f.read())

with open("tasks.txt", "w") as f:
    f.write("line 1\n")
    f.write("line 2\n")
    f.write("line 3\n")

with open("tasks.txt" , "a") as f:
    f.write("Task Completed!")

with open("tasks.txt" , "r") as f:
    for line in f.readlines():
        print(line)


