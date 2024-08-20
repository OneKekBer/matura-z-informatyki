def func(array):
    l = 0
    
    maxAnswer = []
    currentAnswer = []
    isUpping = True
    isLowering = False
    for r in range(len(array)):
        item = array[r]
        
        if(len(currentAnswer) == 0):
            currentAnswer.append(item)
            continue
        
        if currentAnswer[len(currentAnswer) - 1] <= item and isLowering is False:
            isUpping = True
            currentAnswer.append(item)
            continue
        
        if currentAnswer[len(currentAnswer) - 1] >= item and isUpping is True:
            l =r 
            isUpping = False
            isLowering = True
            
        while l < len(array) and currentAnswer[len(currentAnswer) - 1] >= array[l]:
            currentAnswer.append(array[l])
            l += 1
            continue
        
        isUpping = True
        isLowering = False
        
        if(len(maxAnswer) < len(currentAnswer)):
            maxAnswer = currentAnswer
        currentAnswer = []
            
    return maxAnswer
    
print(func([1,1,2,3,4,5,4,3,3,2,1,6,5,88,43,2,3,6,1,1,5,3,1]))


#пиздатая функция 