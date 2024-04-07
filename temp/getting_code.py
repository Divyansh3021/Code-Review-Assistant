import os
from getting_vul import get_vul

def get_folder_paths(directory = "E:/Code Assisstant/"):
    folder_paths = []
    for root, dirs, files in os.walk(directory):
        if '.git' in dirs:
            # Skip the directory if a .git folder is found
            dirs.remove('.git') 
        for dir_name in dirs:
            folder_paths.append(os.path.join(root, dir_name))
    return folder_paths

directory_paths = get_folder_paths()
print("directory_paths: ", directory_paths)

files = []
vulnerabilities = ""

for directory_path in directory_paths:
    for filename in os.listdir(directory_path):
        if filename.endswith((".py",".js", ".ts")):
            filepath = os.path.join(directory_path, filename)
            with open(filepath, "r", encoding='utf-8') as file:
                files.append(filepath)
                code = file.read()
                vulnerabilities += f"File: {filepath}\n\n"
                vulnerabilities += get_vul(code).text

print(vulnerabilities)