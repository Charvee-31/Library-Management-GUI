import os
file_path = os.path.abspath("employee_file.txt")  # Get absolute path
file=open(file_path,"r")
print(file.readable())
file.close()


# print("Current working directory:", os.getcwd())
# print("Files in directory:", os.listdir())  # List all files in the directory

