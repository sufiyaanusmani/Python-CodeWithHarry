import time


def searcher():
    book = "this is a book on python programming"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")


search = searcher()
next(search)
search.send("python")
search.send("java")
search.close()
