#Create a program that reads a file and writes a modified version to a new file.
#Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
#Use the with statement to open files and ensure they are properly closed after use.

file = input("Enter the filename to read: ")
try:
    with open(file, 'r') as f:
        content = f.read()
        print("File content read successfully.")
except FileNotFoundError:
    print(f"Error: The file '{file}' does not exist.")