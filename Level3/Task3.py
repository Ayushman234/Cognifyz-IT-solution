import os
import shutil

source_folder = input("Enter folder path: ")

if not os.path.exists(source_folder):
    print("Folder does not exist.")
    exit()

extensions = {
    ".jpg": "Images",
    ".png": "Images",
    ".jpeg": "Images",
    ".pdf": "PDF",
    ".docx": "Documents",
    ".txt": "Text Files",
    ".mp4": "Videos",
    ".mp3": "Audio"
}

for file in os.listdir(source_folder):

    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):

        extension = os.path.splitext(file)[1].lower()

        folder_name = extensions.get(extension, "Others")

        destination = os.path.join(source_folder, folder_name)

        os.makedirs(destination, exist_ok=True)

        shutil.move(file_path, os.path.join(destination, file))

print("Files organized successfully.")