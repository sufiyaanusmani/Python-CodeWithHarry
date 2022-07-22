import time

initial = time.time()
# print(initial)

for i in range(45):
    print("This is text")

print(time.time() - initial)

initial = time.time()
k = 0
while k < 45:
    print("This is text")
    k += 1

print(time.time() - initial)

print(time.asctime(time.localtime(time.time())))
