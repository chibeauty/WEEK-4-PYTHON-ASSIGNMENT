# README

## File Read & Write Challenge 🖋️

This Python script provides two main functionalities:

1. **Read and Modify File**  
   The [`read_and_modify_file`](script.py) function reads the contents of an input file, modifies it (by converting all text to uppercase), and writes the modified content to a new output file. It includes error handling for missing files and other exceptions.

2. **Error Handling Lab 🧪**  
   The [`get_filename`](script.py) function prompts the user to enter a filename and checks if the file exists and can be read. If the file is not found or cannot be read, it asks the user to try again.

## Usage

1. Place your input file in the same directory as [script.py](script.py).
2. Run the script:
   ```sh
   python script.py
   ```
3. Use the functions as needed:
   - Call `read_and_modify_file('input.txt', 'output.txt')` to read and modify a file.
   - Use `get_filename()` to safely prompt for a filename.

## Example

```python
from script import read_and_modify_file, get_filename

input_file = get_filename()
output_file = "modified_" + input_file
read_and_modify_file(input_file, output_file)
```

## Error Handling

- If the input file does not exist, a message is displayed.
- Other file read/write errors are caught and reported.

