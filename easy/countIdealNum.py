def countIdealNums(low, high):
    idealNums = set()
    a = 1
    while a <= high:
        b = a
        while b <= high:
            b *= 5
        a *= 3
    for num in idealNums:
        if low <= num <= high:
            idealNums.add(num)
    return len(idealNums)