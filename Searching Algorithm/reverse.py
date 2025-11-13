nums=[4,5,6,7,8,9,10,15,16,18]
def reverse(nums):
    left,right=0,len(nums)-1
    while left<=right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    return nums
print(reverse(nums))