import pandas as pd
from fileinput import close
import os
######################################################################################################

current_directory = os.getcwd()
print("Current working directory:", current_directory)

#current directory
current_directory = os.getcwd()
input_file_path = os.path.join(current_directory, "input.txt")
output_file_path = os.path.join(current_directory, "TextOutput.txt")
######################################################################################################
#1
# Read the Excel file
exfile = pd.read_excel("F23P1-M013-Group1.xlsx", engine="openpyxl", dtype=str)

# Create a list of binary values
binary = list(exfile["Binary"])

# Create a list of characters, fixing the "\\n" to "\n"
characters = list(exfile["Characters"])
correction = characters.index("\\n")
characters[correction] = "\n"
######################################################################################################
#2
def load_character_mapping(excel_file_path):
    df = pd.read_excel(excel_file_path, dtype=str)
    character_mapping = dict(zip(df["Characters"], df["Binary"]))
    return character_mapping

def get_binary_value(input_string, character_mapping):
    determined_character = ""

    for character in character_mapping:
        if input_string.startswith(character):
            determined_character = character
            break
    else:
        determined_character = input_string[0]

    binary_value = character_mapping.get(determined_character, "")
    string_without_character = input_string[len(determined_character):]

    return binary_value, string_without_character

#usage:
excel_file_path = "F23P1-M013-Group1.xlsx"
character_mapping = load_character_mapping(excel_file_path)
input_string = "the dog"
binary_value, remaining = get_binary_value(input_string, character_mapping)
print("Character:", binary_value)
print("Remaining String:", remaining)
# ######################################################################################################
#3
def text_to_binary():
    message = input("Enter a message: ")
    binary = " ".join(format(ord(c), "08b") for c in message)
    print("Binary representation:", binary)

def binary_to_text():
    binaryText = input("Enter the binary text: ")
    normal = "".join(chr(int(c, 2)) for c in binaryText.split(" "))
    print("Text representation:", normal)

def main():
    choice = input("Choose an option:\n1. Convert text to binary\n2. Convert binary to text\nEnter 1 or 2: ")
    if choice == "1":
        text_to_binary()
    elif choice == "2":
        binary_to_text()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
# ######################################################################################################
#4
def text_to_binary(message):
    binary = " ".join(format(ord(c), "08b") for c in message)
    print("Binary representation:", binary)
    return binary

def txt2Binary(inputFile):
    try:
        with open(inputFile, 'r') as input_file:
            text_content = input_file.read()
        num_bytes = len(text_content)  # Calculate the number of characters
        num_bits = num_bytes * 8  # Calculate the number of bits needed for the byte count

        binary_content = text_to_binary(text_content)

        outputFile = "BinOutput.txt"  # Output file name

        # Write the binary values to the output file in the specified format
        with open(outputFile, 'w') as output_file:
            output_file.write(f"{num_bits}.{binary_content}")

        # Print the total number of bytes
        print(f"Total number of bytes: {num_bits // 8}")
        print(f"Binary conversion complete. Saved to {outputFile}")
    except FileNotFoundError:
        print(f"Error: File '{inputFile}' not found.")

txt2Binary("input.txt")



# ######################################################################################################
# #5
# def Binary2txt(input_filename="BinOutput.txt"):
#     try:
#         with open(input_filename, 'r') as input_file:
#             input_data = input_file.read()

#         # Split the input string
#         num_bits, binary_content = input_data.split('.')

#         # Convert the binary content back to the original text
#         decoded_text = ""
#         while binary_content:
#             character = ""
#             for i in range(int(num_bits)):
#                 character += binary_content[i]
#                 #character_mapping from task2
#                 if character in character_mapping.values():
#                     decoded_text += next(char for char, bin_val in character_mapping.items() if bin_val == character)
#                     binary_content = binary_content[int(num_bits):]
#                     break

#         # Create the output filename
#         output_filename = "TextOutput.txt"

#         # Write the decoded text to the output file
#         with open(output_filename, 'w') as output_file:
#             output_file.write(decoded_text)

#         print(f"Text decoding complete. Saved to {output_filename}")
#     except FileNotFoundError:
#         print(f"Error: File '{input_filename}' not found.")
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")

# # Example usage:
# Binary2txt("BinOutput.txt")

# ######################################################################################################
# #6
# def are_files_identical(file1_path, file2_path="TextOutput.txt"):
#     try:
#         with open(file1_path, "r") as file1:
#             content1 = file1.read()

#         with open(file2_path, "r") as file2:
#             content2 = file2.read()

#         return content1 == content2
#     except FileNotFoundError:
#         return False
