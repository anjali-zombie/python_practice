def less_count(arr,num):
    count =0
    for i in range(len(arr)):
        if num > arr[i]:
            count = count+1
    return count

arr =[8,3,2,1,4,5]
out =[]
for i in range(len(arr)):
    number =less_count(arr,arr[i])
    out.append(number)
print(f"{out}")
