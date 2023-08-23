# script to remove all files ending in Zone.Identifier in dataset sub directories


import os


for root, dirs, files in os.walk("dataset"):
    for file in files:
        print(file)
        if file.endswith("Zone.Identifier"):
            print(os.path.join(root, file))
            os.remove(os.path.join(root, file))


