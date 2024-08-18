import os
import shutil 

with open("not_seported.txt", "r", encoding = "utf-8") as ff:
	list_tags = ff.read().splitlines()
	for i in list_tags:
		with open(f"tag path//{i}.txt", "r", encoding = "utf-8") as f:
			list_file = f.read().splitlines()
			for path in list_file:
				src = os.path.join("html", path)
				dest = os.path.join(i, path)
				folder = os.path.join(list_file(os.path.split(dest)[:-1]))

				os.mkdir(folder, exist_ok=True)
				shutil.copy(src, dest)
