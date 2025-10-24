def isPalindrome(x):
    if x < 0:
        return False
    x = str(x)
    return x == x[::-1]
print(isPalindrome(121))