from collections import Counter
def unique(arr):
    counts = Counter(arr)
    unique_num = [num for num,count in counts.items() if count ==1]
    return unique_num
    
arr =[1,1,2,2,3,4,5,5]
print(unique(arr))

