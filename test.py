import os
from bs4 import BeautifulSoup

def extract_tags_from_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, "html.parser")
    tags = {tag.name for tag in soup.find_all(True)}
    return tags

def scan_folder_for_html(folder_path):
    all_tags = set()
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                tags = extract_tags_from_html(file_path)
                all_tags.update(tags)
    return all_tags

def write_tags_to_file(tags, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        for tag in sorted(tags):
            if tag.startswith("h") and len(tag) == 2 and tag[1].isdigit():  # Checks for h1, h2, h3, etc.
                file.write(f"{tag}\n")
            else:
                file.write(f"{tag}\n")

# Specify the folder containing the HTML files and the output text file
folder_path = "html"
output_file = "output_tags.txt"

# Scan the folder and write the unique tags to the output file
tags = scan_folder_for_html(folder_path)
write_tags_to_file(tags, output_file)

print(f"Tags have been written to {output_file}")
