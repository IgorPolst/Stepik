from zipfile import ZipFile

with ZipFile("Level_profi/Work_with_file/ZIP/workbook.zip", mode="r") as file:
    file_size = sum(f.file_size  for f in file.infolist())
    compress_file = sum(f.compress_size  for f in file.infolist())

print(f"Объем исходных файлов: {file_size} байт(а)\nОбъем сжатых файлов: {compress_file} байт(а)")