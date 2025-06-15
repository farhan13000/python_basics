file1 = open("test1.txt", "r")
file4 = open("test4.txt", "w") # open with write mode will create the file if it doesn't exist
# The above code opens a file in read mode and another file in write mode.
for line in file1:
    tokens = line.split()
    print(tokens)
    file4.write(" ".join(tokens) + "\n")

file1.close()
file4.close()
# The above code opens a file in read mode, reads its content, prints it, and then closes the file.
# The following code opens a file in write mode, writes some text to it, and then closes the file.
# =================================================================================================================================


file2 = open("test2.txt", "w")
file2.write("Rizwan Khan")
file2.close()
# The above code opens a file in write mode, writes "Rizean Khans" to it, and then closes the file.
# The following code opens a file in append mode, appends some text to it, and then closes the file.
# =================================================================================================================================

file3 = open("test2.txt", "a")
file3.write(" Furkan Khan")
file3.close()
# The above code opens a file in append mode, appends "Furkan Khan" to it, and then closes the file.
# =================================================================================================================================


# Note about file modes:
# "r" - Read mode (default) - Opens a file for reading. If the file does not exist, it raises an error.
# "w" - Write mode - Opens a file for writing. If the file does not exist, it creates a new file. If it exists, it truncates the file to zero length.
# "a" - Append mode - Opens a file for appending. If the file does not exist, it creates a new file. If it exists, it appends to the end of the file.
# "r+" - Read and write mode - Opens a file for both reading and writing. If the file does not exist, it raises an error.
# "w+" - Write and read mode - Opens a file for both writing and reading. If the file does not exist, it creates a new file. If it exists, it truncates the file to zero length.
# "a+" - Append and read mode - Opens a file for both appending and reading. If the file does not exist, it creates a new file. If it exists, it appends to the end of the file.
# "x" - Exclusive creation mode - Opens a file for writing, but fails if the file already exists. It raises a FileExistsError if the file exists.

# Note about file handling:
# Always close the file after you are done with it to free up system resources.
# You can use the 'with' statement to automatically close the file after the block of code is executed.
# Example of using 'with' statement for file handling
with open("test5.txt", "w") as file5:
    file5.write("This is a test file created using 'with' statement.")
# The above code opens a file in write mode using the 'with' statement, writes some text to it, and automatically closes the file.
# The 'with' statement is preferred as it ensures that the file is closed properly even if an error occurs during file operations.  