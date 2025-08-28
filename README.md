# 📂 Python File Handling Challenges

This project contains simple Python programs that demonstrate **file handling** and **error handling** concepts.  
You’ll learn how to read, write, process, and safely handle files using Python.

---

## 🖋️ Challenge 1: File Read & Write

### 📌 Description
A program that reads the contents of an input file, processes it, and writes the modified version to a new file.  
The modification applied in this example is **reversing each line of text**.

### 🚀 How It Works
1. Reads `input.txt`
2. Reverses the text of each line
3. Writes the modified content to `output.txt`
4. Displays a success message


---

## 🧪 Challenge 2: Error Handling Lab

### 📌 Description
A program that asks the user for a filename and tries to read it.  
It gracefully handles errors such as missing files, permission issues, or unexpected problems.

### 🚀 How It Works
1. Prompts the user for a filename
2. Reads and prints the file content if successful
3. Handles errors:
   - **FileNotFoundError** → File does not exist
   - **PermissionError** → No permission to access the file
   - **Other Exceptions** → Any other unexpected error


