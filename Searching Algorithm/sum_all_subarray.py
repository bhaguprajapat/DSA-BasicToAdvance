nums = [4, 5, 6, 7, 8]

def sum_subarray(nums):
    for i in range(len(nums)):
        count = 0
        for j in range(i+1, len(nums)+1):
            sub = nums[i:j]
            count = sum(sub)
            print(f"Subarray: {sub}, Sum: {count}")

sum_subarray(nums)
