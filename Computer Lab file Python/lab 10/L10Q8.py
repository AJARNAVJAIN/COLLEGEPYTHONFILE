print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
import re

def remove_articles(input_file, output_file):
    # Regular expression to match 'a', 'an', 'the' as whole words, case-insensitive
    pattern = r'\b(a|an|the)\b'

    try:
        with open(input_file, 'r') as infile:
            content = infile.read()

        # Replace with blank space
        cleaned_content = re.sub(pattern, ' ', content, flags=re.IGNORECASE)

        # Replace multiple spaces with single space
        cleaned_content = re.sub(r'\s+', ' ', cleaned_content)

        with open(output_file, 'w') as outfile:
            outfile.write(cleaned_content.strip())

        print(f"✅ Cleaned content written to '{output_file}'")
    
    except FileNotFoundError:
        print(f"❌ File '{input_file}' not found.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

# Example usage
remove_articles('original.txt', 'cleaned.txt')
