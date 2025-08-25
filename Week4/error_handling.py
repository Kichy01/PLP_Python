# Error Handling Lab with input prompt
# Ask the user for a filename and open it safely

filename = input("Enter the filename you want to open (e.g., input.txt): ")

try:
    with open(filename, "r") as f:
        content = f.read()
    print("\n File opened successfully! Here is the content:\n")
    print(content)

except FileNotFoundError:
    print("WARNING: The file does not exist. Please check the filename and try again.")

except PermissionError:
    print("WARNING: You don’t have permission to read this file.")

except Exception as e:
    print(f"ERROR: An unexpected error occurred -> {e}")
