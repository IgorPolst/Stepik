from zipfile import ZipFile
import os

file_names = [
    "how to prove.pdf",
    "fipi_demo_2022.pdf",
    "Hollow Knight Silksong.exe",
    "code.jpeg",
    "stepik.png",
    "readme.txt",
    "shopping_list.txt",
    "Alexandra Savior – Crying All the Time.mp3",
    "homework.py",
    "test.py",
]
with ZipFile("files.zip", mode="w") as file:
    for f in file_names:
        if os.path.getsize(f) <= 100:
            file.write(f, arcname=None)
