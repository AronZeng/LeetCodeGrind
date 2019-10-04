def checkPalindrome (s1):
    charDictionary = {}
    for s in s1: 
        if (s in charDictionary):
            charDictionary[s] += 1
        else:
            charDictionary[s] = 1
    numOddChars = 0
    for c in charDictionary:
        if ((charDictionary[c] % 2) == 1):
            numOddChars += 1
            if (numOddChars > 1):
                return False
    return True