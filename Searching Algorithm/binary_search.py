nums=[4,5,6,7,8,9,10,15,16,18]
target=9
def Binary_search(nums,target):
    left=0
    right=len(nums)
    while left<=right:
        mid=left+(right-left)//2
        if nums[mid]==target:
            return mid
        elif target>nums[mid]:
            left=mid+1
        else:
            right=mid-1
print(Binary_search(nums,target))