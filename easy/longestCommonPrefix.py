def longestCommonPrefix(strs):
    if not strs:
        return ""
    common = ""
    first = strs[0]
    for i in range(len(first)):
        char = first[i]
        for word in strs[1:]:
            if i >= len(word) or word[i] != char:
                return common
        common += char
    return common
print(longestCommonPrefix(["flower","flow","flight"]))