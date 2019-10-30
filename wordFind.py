def findWord(s , n):
    listWords = s.split(' ')
    if (n <= len(listWords)):
        return listWords[n-1]
    else: 
        return "Index out of range"
