# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.

def read_and_modify_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()
            # Modify the content (for example, convert to uppercase)
            modified_content = content.upper()
            with open(output_file, 'w') as outfile:
                outfile.write(modified_content)
            print("File has been read and modified successfully.")
    except FileNotFoundError:
        print("Error: The input file was not found.")
    except Exception as e:
        print("Error: Could not read or write to the file.")
        print("Details:", e)




# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

def get_filename():
    while True:
        filename = input("Enter the filename: ")
        try:
            with open(filename, 'r') as file:
                return filename
        except FileNotFoundError:
            print("File not found. Please try again.")
        except Exception as e:
            print("Error:", e)