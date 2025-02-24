from zipfile import ZipFile

with ZipFile("Level_profi/Work_with_file/ZIP/workbook.zip", mode="r") as file:
    data = [f  for f in file.infolist() if not f.is_dir()]

print(len(data))