def  disappeared_list(arr):
    dis_list =[]
    set_nums = set(arr)
    for i in range(1,len(set_nums)+1):
        if i not in set_nums:
            dis_list.append(i)

    return dis_list
arr = [4,3,2,1,7,2,8]
print(max(arr))
print(disappeared_list(arr))
