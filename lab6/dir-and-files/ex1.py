import os
def list_files_and_dirs(path):
    files = []
    dirs = []
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            dirs.append(item)
        else:
            files.append(item)
    print(f"Директории: {dirs}\nФайлы: {files}")
    return {"directories": dirs, "files": files}