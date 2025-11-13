"""
Problem is:- find max sum of subaarray like a have an array [1,2,3,-5,-7]
all sub array and their sum is like:=
sub array                         sum
[1]                                1
[1,2]                              3
[1,2,3]=                           6
[1,2,3,-5]                         1
[1,2,3,-5,-7]                     -6
[2]                                2
[2,3]                              5
[2,3,-5]                           0
[2,3,-5,-7]                       -7
[3]                                3
[3,-5]                            -2
[3,-5,-7]                         -9
[-5]                               5
[-5,-7]                           -12
[-7]                              -7
here is our rsult is 6 that is sum of [1,2,3] subarray

approuch:-
first of all inilitize the max_sum=nums[0]then  we run the outer loop till length of array
for i in range(len(nums))
then for getting all subarrray we run the same inner loop from i+1 to length of nums
here we sum the all sub array in currn_sum=sum(nums[i:j])
then check is max_sum<currn_sum then change the value of max_sum with curr_sum 
after the loop exit return the max_sum
time complexity Outer loop → runs n times

Inner loop → runs approximately n - i times

Inside inner loop, sum(nums[i:j]) takes O(j - i) time.
✅ Time Complexity = O(n³)
space compexity O(n) becouse there don't take extra space
"""
nums=[1,-2,6,-1,3]
def max_sum_subbarray(nums):
    max_sum=nums[0]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)+1):
            curr_sum=sum(nums[i:j])
            if max_sum<curr_sum:
                max_sum=curr_sum

    return max_sum
print(max_sum_subbarray(nums))


"""
Now we solve the same problem with best time and space complexity  here we use kanddans algoritham
first of all inilitiaze max_sum=curr_sum=nums[0]
then trigger all array
get max of current sum
and get max of max_sum from curr_sum and max_sum
at the end return max_sum
time complexity o(n) here we run only one loop that run the nth time
space complexity o(1) we don't use extra space
"""
nums=[-1,-2.6,-1,3]
def kadans_algo(nums):
    max_sum=curr_sum=nums[0]
    for num in nums[1:]:
        curr_sum=max(num,curr_sum+num)
        max_sum=max(curr_sum,max_sum)
    return max_sum