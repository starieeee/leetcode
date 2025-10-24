def isAnagram(s, n):
    if len(s) != len(n):
        return False
    return sorted(s) == sorted(n)