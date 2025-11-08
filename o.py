# Write a function repeatElements which accepts two parameters, a list and an int, numRepeats. It modifies the list so that is has numRepeats of each element.

#  Note: You may assume numRepeats is a positive integer.
def repeatElements(aList, nums):
    i = 0
    while i < len(aList):
        item = aList[i]
        for j in range(nums - 1):
            aList.insert(i + j + 1, item)
        i += nums