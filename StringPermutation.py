def checkPermutation(s1 , s2): 
    charCount = {}
    if (len(s1) != len(s2)):
        return False
    for s in s1: 
        if (s in charCount):
            charCount[s]+= 1
        else: 
            charCount[s] = 1
    for s in s2: 
        if (s in charCount):
            if (charCount[s] > 0 ):
                charCount[s]-= 1
            else: 
                return False
        else: 
            return False
    return True
