def isUnique (s): 
    if (len(s) > 26):
        return False
    charList = [None] * 26
    for char in s:
        lowerChar = char.lower()
        index = ord(lowerChar) - 97
        if (charList[index]):
            return False
        else:
            charList[index] = True
    return True

print(isUnique("Aaron"))