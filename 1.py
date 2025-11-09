import os


def convert_file_size(size: int):
    names = ["B", "KB", "MB", "GB", "TB"]
    order = 0
    while size // 1024 >= 1 and order < len(names):
        size /= 1024
        order += 1
    return f"{round(size)}{names[order]}"


def get_file_sizes(files_dir=None):
    if not files_dir:
        files_dir = os.getcwd()
    result = []
    for name in os.listdir(files_dir):
        path = os.path.join(files_dir, name)
        if os.path.isfile(path):
            size = convert_file_size(os.path.getsize(path))
            result.append(f"{name} {size}")
    return "\n".join(result)


print(get_file_sizes())
