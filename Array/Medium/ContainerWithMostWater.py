"""
Container With Most Water
leetcode problem:- https://leetcode.com/problems/container-with-most-water/description/
the problem is :- You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


approach:-
first of all inilitaze left and right pointer for tracking all elements
then inilitaze max_water first set 0
Run while loop till left value less then right value
calculate width of the container that is right-left
the calculate height of the container that is min of from left and right value
the calculate water capacity of current container
then update the maxwater capacity if the current container holds more water
move the poiner with each othre
at the end return max_water


time complexity: O(n)
space compelexity o(1)


"""
def trapRainWater(height):
    left,right=0,len(height)-1
    max_water=0
    while left<=right:
        width=right-left
        min_height=min(height[left],height[right])
        curr_water_area=width*min_height
        max_water=max(curr_water_area,max_water)
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return max_water
height=[1,8,6,2,5,4,8,3,7]
print(trapRainWater(height))