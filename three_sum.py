def three_sum(arr,target):
    arr.sort()
    k = len(arr)-1
    j=1
    for  i in range(0,len(arr)):
        if j<k and j!=i and j!=k and k!=i and k!=j:
            th_sum = arr[i]+arr[j]+arr[k] 
            if th_sum < target:
                j = j+1
            elif th_sum > target:
                k = k-1
            elif th_sum == target:
                return [arr[i],arr[j],arr[k]]

arr = [1,3,2,4,0,5] #[0,1,2,3,4,5]
target = 9
print(three_sum(arr,target))

