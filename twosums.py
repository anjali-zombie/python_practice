def twosum(arr,target):
    twosum_list =[]
    for i in range(0,len(arr)):
        ele = abs(arr[i]-target)
        if ele in arr:
            if arr[i] != ele :
                if arr[i]+ele == target :
                    twosum_list.append(arr[i])
    return twosum_list

arr =[2,7,11,3,5]
target =14
print(twosum(arr,target))

