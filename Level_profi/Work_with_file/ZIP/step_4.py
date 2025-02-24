from zipfile import ZipFile

with ZipFile("Level_profi/Work_with_file/ZIP/workbook.zip", mode="r") as file:
    files = file.infolist()

files = filter(lambda f: f.date_time > (2021, 11, 30, 14, 22, 0) and not f.is_dir(), files)
files_name = sorted([f.filename.split('/')[-1] for f in files])
print (*files_name, sep="\n")