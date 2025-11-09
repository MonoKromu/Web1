import os.path
from zipfile import ZipFile


def convert_file_size(size: int):
    names = ["B", "KB", "MB", "GB", "TB"]
    order = 0
    while size // 1024 >= 1 and order < len(names):
        size /= 1024
        order += 1
    return f"{round(size)}{names[order]}"


def get_file_tree(arch_path: str):
    directories = {}
    with ZipFile(arch_path) as archive:
        for info in archive.infolist():
            path = info.filename
            directory = os.path.dirname(path)
            if directories.get(directory) is None:
                directories[directory] = []
            if not path.endswith("/"):
                name = os.path.basename(path)
                size = convert_file_size(info.file_size)
                directories.get(directory).append(f"{name} {size}")

    result = []
    for directory, files in sorted(directories.items()):
        depth = len(directory.split("/")) - (2 if len(directory) == 0 else 1)
        result.append(f"{'  ' * depth}{os.path.basename(directory)}")
        for file in files:
            result.append(f"{'  ' * (depth + 1)}{file}")
    return "\n".join(result)


print(get_file_tree("files/2.zip"))
