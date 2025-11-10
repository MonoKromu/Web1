import os


def cached_size():
    sizes = {}

    def get_file_size_cached(file: str):
        if file not in sizes:
            size = os.path.getsize(file)
            sizes[file] = size
        return sizes.get(file)

    def get_folder_size_cached(folder: str, rec=False):
        rec = int(rec)
        if folder not in sizes:
            sizes[folder] = [None, None]
        value = sizes.get(folder)
        if value[rec] is None:
            paths = [os.path.join(folder, name) for name in os.listdir(folder)]
            files_size = sum([get_file_size_cached(path) for path in paths if os.path.isfile(path)])
            if rec:
                folders_size = sum([get_folder_size_cached(path, rec=True) for path in paths if os.path.isdir(path)])
                files_size += folders_size
            value[rec] = files_size
        return value[rec]

    return get_file_size_cached, get_folder_size_cached


def get_all_folders(folder: str):
    paths = [os.path.join(folder, name) for name in os.listdir(folder)]
    folders = [path for path in paths if os.path.isdir(path)]
    all_folders = folders.copy()
    for folder in folders:
        all_folders.extend(get_all_folders(folder))
    return all_folders


def convert_size(size: int):
    names = ["B", "KB", "MB", "GB", "TB"]
    order = 0
    while size // 1024 >= 1 and order < len(names):
        size /= 1024
        order += 1
    return f"{round(size)}{names[order]}"


recursive = True
get_file_size, get_folder_size = cached_size()
folder_list = get_all_folders(os.getcwd())
size_list = [get_folder_size(folder, rec=recursive) for folder in folder_list]
folder_sizes = sorted(zip(size_list, folder_list), reverse=True)
for i in range(min(len(folder_list), 10)):
    print(f"{convert_size(folder_sizes[i][0]):<{6}} {folder_sizes[i][1]}")
