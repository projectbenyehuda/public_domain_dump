import os
import shutil

with open("not_seported.txt", "r", encoding="utf-8") as ff:
    list_tags = ff.read().splitlines()
    
    for i in list_tags:
        with open(f"tag path//{i}.txt", "r", encoding="utf-8") as f:
            list_file = f.read().splitlines()
            
            for path in list_file:
                dest_folder = os.path.join(i, os.path.dirname(path))
                dest = os.path.join(i, path)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.copy(path, dest)
