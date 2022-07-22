# def functionPrint(a, b, c, d):
#     print(a, b, c, d)


def functionPrint(*items, **kwargs):
    for item in items:
        print(item)

    for key, value in kwargs.items():
        print(key, value)


lst = ["Sufiyaan", "Harry", "Bill", "Steve"]
kw = {
    "HTML": "Web",
    "GUI": "C#",
    "All": "Python"
}
functionPrint(*lst, **kw)
