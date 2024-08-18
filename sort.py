import os
from bs4 import BeautifulSoup
from collections import defaultdict

def extract_tags_from_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, "html.parser")
    tags = {tag.name for tag in soup.find_all(True)}
    return tags

def scan_folder_for_html(folder_path):
    tag_paths = defaultdict(list)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                tags = extract_tags_from_html(file_path)
                for tag in tags:
                    tag_paths[tag].append(file_path)
    return tag_paths

def write_paths_to_tag_files(tag_paths, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    for tag, paths in tag_paths.items():
        tag_file_path = os.path.join(output_folder, f"{tag}.txt")
        with open(tag_file_path, "w", encoding="utf-8") as file:
            for path in paths:
                file.write(f"{path}\n")

# Specify the folder containing the HTML files and the output folder
folder_path = "html"
output_folder = "tag path"

# Scan the folder and write the file paths to separate files for each tag
tag_paths = scan_folder_for_html(folder_path)
write_paths_to_tag_files(tag_paths, output_folder)

print(f"Tag files have been created in {output_folder}")
