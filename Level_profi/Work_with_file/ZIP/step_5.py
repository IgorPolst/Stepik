from zipfile import ZipFile
from datetime import datetime

with ZipFile("Level_profi/Work_with_file/ZIP/workbook.zip", mode="r") as file:
    files = sorted(
        filter(lambda f: not f.is_dir(), file.infolist()),
        key=lambda f: f.filename.split("/")[-1],
    )

for f in files:
    print(f.filename.split("/")[-1])
    print(f"  Дата модификации файла: {datetime(*f.date_time)}")
    print(f"  Объем исходного файла: {f.file_size} байт(а)")
    print(f"  Объем сжатого файла: {f.compress_size} байт(а)\n")
