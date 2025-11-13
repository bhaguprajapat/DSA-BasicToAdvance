nums=[2,5,1,6,8,7]
def find_large_num(nums):
    large_num=nums[0]
    for i in range(len(nums)):
        if(large_num<nums[i]):
            large_num=nums[i]
    return large_num
print(find_large_num(nums))