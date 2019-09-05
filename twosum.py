
    def twoSum ( array , target):
        currentIndex = 0
        for i in array[ : (len(array)) - 1 ]:
            if i < target:
                remainder = target - i
                if remainder in array[currentIndex + 1 : ] : 
                   remainderIndex = array[currentIndex + 1 : ].index(remainder) + currentIndex + 1
                   return([currentIndex , remainderIndex])
                else: 
                    currentIndex += 1    
        return[] 
