try:
    f = open("does.txt")

except EOFError as a:
    print(a)

except Exception as e:
    print(e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway")

print("Important stuff")
