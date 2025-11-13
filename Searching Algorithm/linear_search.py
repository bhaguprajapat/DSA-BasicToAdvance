nums=[2,5,1,6,8,7]
target=6
def linearsearch(nums,target):
    for i in range(len(nums)):
        if(target==nums[i]):
            return i
    return -1
print(linearsearch(nums,target))