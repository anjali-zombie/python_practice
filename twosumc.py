def twosum(arr,target):
    resultant_list = {} #intialization of hash map
    # to acsess index and its value at same time use "enumerate"
    for i,num in enumerate(arr):
        ele = target - num
        if ele in resultant_list:
            #will return ele index(resultant_list[ele]) and current element index
            return [resultant_list[ele],i]
        resultant_list[num]= i

arr =[2,7,11,15]
target = 13
print(twosum(arr,target))
