# Stores unique values

s = set()
print(type(s))

sFromList = set([1, 2, 3, 4])
print(sFromList)
print(type(sFromList))

s.add(2)
s.add(3)
s.add(3)
print(s)

s1 = s.union({1, 2, 3})
print(s, s1)
s1 = s.intersection({1, 2, 3})
print(s, s1)
print(len(s))
