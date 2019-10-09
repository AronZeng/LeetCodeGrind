#in this solution, I assumed our input will be a string

def prices(s):
  nVal = s[0] #this is reading our n value 
  nDict = {} #initialize our dictionary to store the outputs
  lastIndex = 1
  for n in range(nVal):
    newIndex = s[lastIndex:].find('\n')
    newEntry = s[lastIndex: lastIndex+newIndex]
    commaIndex = newEntry.find(',')
    city = newEntry[0 : commaIndex]
    if (city in nDict):
      nDict[city].append(newEntry)
    else:
      nDict[city] = []
      nDict[city].append(newEntry)
    lastIndex += newIndex
  #by now our nDict has all the entries that come after the n value
  #next we shall read our Q values 
  
  qVal = s[lastIndex + 1]
  qArray = []
  lastIndex += 1
  #extract our queries after the q value first and store them in qArray
  for q in range(qVal):
    newIndex = s[lastIndex:].find('\n')
    newEntry = s[lastIndex : lastIndex+newIndex]
    qArray.append(newEntry)
    lastIndex += newIndex
  #by now our qArray has all the entires that come after the q value
  
  resultDict = {}
  for q in qArray: 
    commaIndex = q.find(',')
    city = q[0 : commaIndex]
    days = q[commaIndex + 1 :]
    for entry in nDict[city]:
      firstComma = entry.find(',')
      secondComma = firstComma + 2
      supplier = entry[firstComma + 1]
      price = float(entry[secondComma + 1 :])
      if (supplier == "A" and days == 1):
        if (city in resultDict):
          resultDict[city].push(price * 1.5)
        else: 
          resultDict[city] = []
          resultDict[city].push(price * 1.5)
      elif (supplier == "A"): 
        if (city in resultDict):
          resultDict[city].push(price)
        else: 
          resultDict[city] = []
          resultDict[city].push(price)
      elif (supplier == "B"):
        if(days > 3):
          if(city in resultDict):
            resultDict[city].push(price)
          else: 
            resultDict[city] = []
            resultDict[city].push(price)
        else: 
          if(city in resultDict):
            resultDict[city].push('None')
          else: 
            resultDict[city] = []
            resultDict[city].push('None')
      elif (supplier == "C" and days > 7):
        if (city in resultDict):
          resultDict[city].push(price * 0.9)
        else: 
          resultDict[city] = []
          resultDict[city].push(price * 0.9)
      elif(supplier == "C"):
        if (city in resultDict):
          resultDict[city].push(price)
        else: 
          resultDict[city] = [] 
          resultDict[city].push(price)
      elif(supplier == "D" and days < 7):
        if (city in resultDict):
          resultDict[city].push(price * 1.1)
        else: 
          resultDict[city] = [] 
          resultDict[city].push(price * 1.1)
      elif(supplier == "D"):
        if (city in resultDict):
          resultDict[city].push(price)
        else: 
          resultDict[city] = [] 
          resultDict[city].push(price)
    
    print(price(""))
        
    
    
    
    
    
    
    
    
    
    
    
  