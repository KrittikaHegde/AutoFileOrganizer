import os
import shutil

# Define file type categories
FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Documents": [".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "PDFs": [".pdf"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".java", ".cpp"],
    "Others": []
}

FOLDER_PATH = r"D:\Mini projects\TestDownloads"
def create_folders(path, categories):
    for folder in categories:
        folder_path = os.path.join(path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def organize_files(path, categories):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            moved = False
            for category, extensions in categories.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(path, category, file))
                    moved = True
                    break
            if not moved:
                shutil.move(file_path, os.path.join(path, "Others", file))
# Ensure the script is run in the correct directory
if __name__ == "__main__":
    create_folders(FOLDER_PATH, FILE_TYPES)
    organize_files(FOLDER_PATH, FILE_TYPES)
    print("✅ Files organized successfully!")