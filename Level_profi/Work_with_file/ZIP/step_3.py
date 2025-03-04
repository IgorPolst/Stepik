from zipfile import ZipFile

with ZipFile("Level_profi/Work_with_file/ZIP/workbook.zip", mode="r") as file:
    files = file.infolist()

files = sorted(
    [f for f in files if f.file_size != 0],
    key=lambda f: 1 - (f.compress_size / f.file_size),
    reverse=True,
)


print(files[0].filename.split("/")[-1])
