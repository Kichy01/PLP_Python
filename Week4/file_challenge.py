# File Read & Write Challenge 🖋️
# This program reads a file and writes a modified version to a new file.

try:
    # Try to open input.txt for reading
    with open("input.txt", "r") as infile:
        content = infile.read()

except FileNotFoundError:
    # If input.txt is missing, create it with default text
    print("INFO: input.txt not found. Creating it with sample text...")
    with open("input.txt", "w") as infile:
        infile.write("Hello World\nThis is a sample file created automatically.\nPython is Great!\n")
    # Re-open it for reading
    with open("input.txt", "r") as infile:
        content = infile.read()

# Modify the content (e.g., convert to uppercase)
modified_content = content.upper()

# Write modified content to a new file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print(" SUCCESS: File has been read and modified version written to output.txt")
