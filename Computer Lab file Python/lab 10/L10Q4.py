print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
import os
import shutil

# Define source file and target directory
source_file = 'source_dir/sample.txt'          # Path to the source file
target_dir = 'destination_dir/subfolder'       # Subdirectory you want to create

# Create the destination subdirectory if it doesn't exist
os.makedirs(target_dir, exist_ok=True)

# Define destination file path
destination_file = os.path.join(target_dir, os.path.basename(source_file))

# Copy the file
shutil.copy2(source_file, destination_file)

print(f"✅ File copied to: {destination_file}")
