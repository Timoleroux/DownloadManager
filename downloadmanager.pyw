from pathlib import Path
from time import sleep
import os

FOLDER_WAY = Path("C:/Users/timol/Downloads/")

SORTER = {
    ".png": "images/",
    ".jpg": "images/",
    ".jpeg": "images/",
    ".gif": "images/",
    ".bmp": "images/",
    ".tiff": "images/",
    ".psd": "images/",
    ".webp": "images/",
    ".svg": "images/",
    ".ico": "images/",
    ".heic": "images/",
    ".mov": "videos/",
    ".mp4": "videos/",
    ".avi": "videos/",
    ".mkv": "videos/",
    ".py": "developpement/",
    ".html": "developpement/",
    ".htm": "developpement/",
    ".css": "developpement/",
    ".js": "developpement/",
    ".php": "developpement/",
    ".rb": "developpement/",
    ".cpp": "developpement/",
    ".c": "developpement/",
    ".swift": "developpement/",
    ".tex": "developpement/",
    ".cls": "developpement/",
    ".doc": "bureautique/",
    ".docx": "bureautique/",
    ".pps": "bureautique/",
    ".ppsx": "bureautique/",
    ".ppt": "bureautique/",
    ".pptx": "bureautique/",
    ".xls": "bureautique/",
    ".xlsx": "bureautique/",
    ".odt": "bureautique/",
    ".ods": "bureautique/",
    ".odp": "bureautique/",
    ".pdf": "bureautique/",
    ".txt": "bureautique/",
    ".zip": "installer/",
    ".rar": "installer/",
    ".exe": "installer/",
    ".iso": "installer/",
    ".msi": "installer/",
}

EXEPTION = [".tmp"]


def sortFiles():
        while True:

            FILES = [f for f in FOLDER_WAY.iterdir() if f.is_file()]

            # List the files ending with .tmp 
            files_to_remove = []
            for i in range(0, len(FILES)):
                if str(FILES[i].suffix) == ".tmp":
                    files_to_remove.append(FILES[i])

            # Remove files ending with .tmp
            for i in files_to_remove:
                FILES.remove(i)
            print("----- FICHIERS -----", FILES)

            try:
                # Move files to their respective folders
                print("----- SORTING -----")
                print("----- FILES AFTER SORTING -----", FILES)
                if len(FILES) != 0:
                    for f in FILES:
                        output_sorter = FOLDER_WAY / SORTER.get(f.suffix, "autre/")
                        output_sorter.mkdir(exist_ok=True)
                        f.rename(output_sorter / f.name)
                    sleep(1)

            except FileExistsError:
                
                print("File",  str(f),  "already exists")

                i = 0
                newname = f.name

                while os.path.exists(FOLDER_WAY / newname):
                    i += 1
                    newname = f.name.split(".")
                    newname = newname[0] + "_." + newname[1]

                f.rename(FOLDER_WAY / newname)
                newname = Path(newname)
                output_sorter = FOLDER_WAY / SORTER.get(f.suffix, "autre/")
                output_sorter.mkdir(exist_ok=True)
                newname.rename(output_sorter / newname)

            sleep(1)
                
sortFiles()