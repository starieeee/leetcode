def mySqrt(x):
    if x == 0 or x == 1:
        return x
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    return right