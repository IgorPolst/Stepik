from zipfile import ZipFile


def convert_bytes(size):
    """Конвертер байт в большие единицы"""
    if size < 1000:
        return f"{size} B"
    elif 1000 <= size < 1000000:
        return f"{round(size / 1024)} KB"
    elif 1000000 <= size < 1000000000:
        return f"{round(size / 1048576)} MB"
    else:
        return f"{round(size / 1073741824)} GB"


with ZipFile("Level_profi\Work_with_file\ZIP\step_10\desktop.zip", "r") as file:
    data = file.infolist()


for file in data:
    indent = len(file.filename.split("/")) - 2
    if file.is_dir():
        print(f"{'  '*indent}{file.filename.split('/')[-2]}")
    else:
        print(
            f"{'  '*(indent+1)}{file.filename.split('/')[-1]} {convert_bytes(file.file_size)}"
        )
