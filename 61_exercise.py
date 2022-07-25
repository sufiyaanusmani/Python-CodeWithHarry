import os


def soldier(path, file, format):
    os.chdir(path)
    ls = os.listdir(path)
    for item in ls:
        if os.path.isfile(item):
            fName = item.capitalize()
            os.rename(item, fName)


if __name__ == "__main__":
    soldier("D://Projects/Python/CodeWithHarry/that", "harry.txt", "jpg")
