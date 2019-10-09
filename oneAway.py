def oneAway (s1 , s2): 
    difference = len(s1) - len(s2)
    difference = abs(difference)
    if (difference > 1):
        return False 
    elif (s1 == s2):
        return True
    elif (difference == 1):
        return checkAddition(s1, s2)
    else:
        return checkReplace(s1, s2)

def checkAddition(s1 , s2):
    foundDifference = False
    if (len(s1) > len(s2)):
        for i in range(len(s1)):
            if (s1[i] == s2[i]):
                continue
            elif (s1[i] != s2[i] and foundDifference == True):
                return False
            else:
                if (i == len(s2) - 1):
                    return True
                if (i == 0):
                    s2 = s1[0] + s2
                    foundDifference = True
                else:
                    s2 = s2[:i] + s1[i] + s2[i+1 :]
                    foundDifference = True
        return True
    if (len(s1) < len(s2)):
        for i in range(len(s2)):
            if (s1[i] == s2[i]):
                continue
            elif (s2[i] != s1[i] and foundDifference == True):
                return False
            else:
                if (i == len(s2) - 1):
                    return True
                if (i == 0):
                    s1 = s2[0] + s1
                    foundDifference = True
                else:
                    s1 = s1[:i] + s2[i] + s1[i+1 :]
                    foundDifference = True
        return True

def checkReplace(s1 , s2):
    foundDifference = False
    for i in range(len(s1)):
        if (s1[i] != s2[i]):
            if (foundDifference == True):
                return False
            foundDifference = True
    return True