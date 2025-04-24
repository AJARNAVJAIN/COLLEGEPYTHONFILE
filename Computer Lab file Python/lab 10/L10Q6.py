print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
def merge_alternate_lines(file1, file2, output_file):
    try:
        # Open all files
        with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
            lines1 = f1.readlines()
            lines2 = f2.readlines()

            max_len = max(len(lines1), len(lines2))

            for i in range(max_len):
                if i < len(lines1):
                    out.write(lines1[i])
                if i < len(lines2):
                    out.write(lines2[i])

        print(f"✅ Lines merged into '{output_file}' successfully.")
    
    except FileNotFoundError as e:
        print(f"❌ File not found: {e.filename}")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

# Example usage
merge_alternate_lines('file1.txt', 'file2.txt', 'merged_output.txt')
