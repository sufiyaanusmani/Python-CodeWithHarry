if __name__ == "__main__":
    ls = [5, 4, 1]
    temp = ls[::]

    temp.reverse()
    print(temp)
    print(ls[::-1])

    temp2 = ls[::]
    for i in range(len(temp2) // 2):
        temp2[i], temp2[len(temp2) - i -
                        1] = temp2[len(temp2) - i - 1], temp2[i]

    print(temp2)
