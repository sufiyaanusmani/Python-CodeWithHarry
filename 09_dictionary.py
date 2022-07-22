# {}
# key-value pairs

d1 = {}
print(type(d1))

d2 = {
    "Web": "HTML, CSS, JS",
    "DS": "Python",
    "Desktop": {
        "Low": "C",
        "High": "Java"
    }
}

print(d2["DS"])
print(d2["Desktop"]["High"])
d2["GUI"] = ".NET"
print(d2)
del d2["Web"]
print(d2)
d3 = d2     # shallow copy
d3 = d2.copy()  # deep copy
