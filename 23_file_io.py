# from statistics import mode


# "r" - open file for reading (default)
# "w" - open file for writing
# "x" - creates file if not exists
# "a" - open file in append mode
# "t" - text mode (default)
# "b" - binary mode
# "+" - update(read + write)

def read():
    f = open("file.txt", "rt")
    content = f.read()
    # print(f.readline())
    # print(f.readlines())
    print(content)
    f.close()


def write():
    f = open("file.txt", "w")
    f.write("Python Programming\n")
    f.close()


def both():
    f = open("file.txt", "r+")
    print(f.read())
    f.write("Thankyou")
    f.close()


both()
