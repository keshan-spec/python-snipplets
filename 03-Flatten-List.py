# Flatten a 2D list

myList = [1, 3, 2, [4, 5], 9]


def flatten(param):
    newList = []
    for i in param:
        if i not in newList:
            if hasattr(i, '__iter__'):
                newList.extend(i)
            else:
                newList.append(i)

    print(f"Old List:{myList}\nNew list:{newList}")


flatten(myList)
