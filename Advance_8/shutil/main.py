import shutil

# 1. copy() — Copy a file
shutil.copy("source.txt", "destination.txt")

# 2. copy2() — Copy a file with metadata
shutil.copy2("source.txt", "destination.txt")

# 3. copytree() — Copy a directory tree
shutil.copytree("source_dir", "destination_dir")

# 4. move() — Move a file or directory
shutil.move("source.txt", "destination.txt")

# 5. rmtree() — Remove a directory tree
shutil.rmtree("directory_to_remove")