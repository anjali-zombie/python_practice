from collections import Counter
def removeDuplicates(arr):
     num_count=Counter(nums)
     ans =0
     for num , count in num_count.items():
         if count <= 2:
             ans += count
         elif count > 2:
             ans +=2
     return ans

nums = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(nums))
