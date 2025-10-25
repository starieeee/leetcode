def replaceElement(arr):
    maxSoFar = -1
    for i in range(len(arr) - 1, -1, -1):
        current = arr[i]
        arr[i] = maxSoFar 
        if current > maxSoFar:
            maxSoFar = current
    return arr