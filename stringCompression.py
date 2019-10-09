def compress(s): 
    current = ""
    charArray = []
    returnStr = ""
    for c in s: 
        if (c != current): 
            current = c 
            charArray.append({"character" : c , "count" : 1})
        else: 
            charArray[-1]["count"] += 1
    for c in charArray: 
        if (c["count"] > 1):
            returnStr = returnStr + c["character"] + str(c["count"])
        else:
            returnStr = returnStr +c["character"]
    return returnStr

        