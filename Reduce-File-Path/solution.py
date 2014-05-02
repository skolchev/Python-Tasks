def reduce_file_path(path):
    # remove all multiple forwardslashes
    newPath = path.replace("//", "/")
    while newPath.find("//") != -1:
        newPath = newPath.replace("//", "/")

    # remove all current directories('.')
    directories = newPath.split("/")
    directories = [x for x in directories if x != "."]

    # remove '..' and go one level up
    # in directory sturcture
    while ".." in directories:
        index = directories.index("..")
        del directories[index]
        if index > 1:
            del directories[index - 1]

    # remove last forwardslash
    newPath = "/".join(directories)
    length = len(newPath)
    if length > 1 and newPath[length - 1] == '/':
        newPath = newPath[:length - 1]

    return newPath
