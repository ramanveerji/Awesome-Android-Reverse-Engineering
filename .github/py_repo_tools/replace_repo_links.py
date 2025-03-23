# Python program to read
# json file
  
  
import json

with open('.github/py_repo_tools/repo_config.json') as f:
    # returns JSON object as 
    # a dictionary
    config = json.load(f)


    # Define the filename here you want to replace content in
    FileName = "README.md"

    Text_To_Replace = config['Text_To_Replace']

    Text_To_Replace_With = config['Text_To_Replace_With']

# Open the File
with open(FileName, 'r') as f:
    # Read the file contents
    contents = f.read()
    # Replace the file contents
    contents = contents.replace(Text_To_Replace, Text_To_Replace_With)

# Write the file out    
with open(FileName, 'w') as f:
    # Write the updated contents
    f.write(contents)  
