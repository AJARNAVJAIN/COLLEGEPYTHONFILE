print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
def copy_with_uppercase(source_file, destination_file):
    try:
        # Open the source file in read mode
        with open(source_file, 'r') as src:
            content = src.read()

        # Convert all lowercase characters to uppercase
        upper_content = content.upper()

        # Write the uppercase content to the destination file
        with open(destination_file, 'w') as dest:
            dest.write(upper_content)

        print(f"✅ File copied from '{source_file}' to '{destination_file}' with uppercase transformation.")
    
    except FileNotFoundError:
        print(f"❌ Source file '{source_file}' not found.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

# Example usage
copy_with_uppercase('input.txt', 'output.txt')
