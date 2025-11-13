nums=[4,5,6,7,8]
def pairs_array(nums):
    count=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            print(nums[i:j])
            count+=1
    return count
    
print(pairs_array(nums))