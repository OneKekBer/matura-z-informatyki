testList = [1,2,6,2,1,1,6,7,2,1,4,2,2,3,1]
def find_max_arr(arr):
    maxSum = 4 
    currentSum = 0
    maxVars = 0
    correctLists = []
    l = 0;
    for r in range(len(arr)):
        currentSum += arr[r]
        if(currentSum == maxSum):
                correctLists.append(arr[l:r])
                maxVars += 1
        while currentSum > maxSum: 
            currentSum -= arr[l]
            l+=1
        
        
    print(maxVars)
    print(correctLists)
    

find_max_arr(testList)