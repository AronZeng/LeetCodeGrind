
def twoSum (array , target):
    currentIndex = 0
    for i in array:
        if i < target:
            remainder = target - i
            if remainder in array[currentIndex : ] : 
               remainderIndex = array.index(remainder)
               return([currentIndex , remainderIndex])
            else: 
                currentIndex += 1     