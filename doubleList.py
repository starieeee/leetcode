def doubleList(aList):
    newList = []
    for item in aList:
        newList.append(item)
        newList.append(item)
    return newList
# Example usage:
# print(doubleList([1, 2, 3]))  # Output: [1, 1, 2, 2, 3, 3]