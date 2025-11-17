"""
Leetcode problem :- https://leetcode.com/problems/majority-element/description/
The problem is :- Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
"""
class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        ans=nums[0]
        freq=0
        for i in range(len(nums)):
            if ans==nums[i]:
                freq+=1
            if freq>len(nums)//2:
                return nums[i]
            ans=nums[i]
        return ans
        

sl=Solution()
nums = [2,2,1,1,1,2,2]
print(sl.majorityElement(nums))