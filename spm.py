def spm(arr):
    upper_row =0
    lower_row =len(arr)-1
    left_column =0
    right_column =len(arr[0])-1
   # rows, cols = 4, 4
   # matrix = [[0 for _ in range(cols)] for _ in range(rows)]  # 4×4 matrix filled with zeros
   # print(matrix)
    size = len(arr) * len(arr[0])
    arr_result = [0] * size
    k=0
    while(k<size):
        i = upper_row
        for j in range(left_column,right_column+1):
            arr_result[k] = arr[i][j]
            k +=1
        upper_row +=1
        i=right_column
        for j in range(upper_row,lower_row+1):
            arr_result[k] = arr[j][i]
            k +=1
        right_column -=1
        i = lower_row
        for j in range(right_column,left_column-1,-1):
            arr_result[k] =arr[i][j]
            k +=1
        lower_row -=1
        i = left_column
        for j in range(lower_row,upper_row-1,-1):
            arr_result[k] = arr[j][i]
            k +=1

        left_column +=1
    return arr_result

arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(spm(arr))

