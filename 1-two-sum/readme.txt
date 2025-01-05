January 3, 2025

Link: 
https://leetcode.com/problems/two-sum/description/

Problem: 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

 

Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

Solution:

I began by just blindly running two for loops and looking for combos that worked. This does work, but does not meet all the conditions stipulated, so I changed the code so that the
inner loop only looks at the "rest" of the list. This required messing with the indices since the inner loop now has an artificially shrunken list. This works, but it is O(n^2) 
which is not great (it doesn't use lots of memory though!). To fix it we can use a single loop and a dictionary to save past values we have seen. This now gives us ~O(n) time complexity
which beats 53% of people, but our space complexity only beats 7% of people. Removing the silly lists in a dictionary thing gets me to 100% on time complexity and 10% on space complexity.
I messed around a bit more with space complexity, but it basically seems like we are either going to get one or the other so I will be done with my third iteration which uses a set 
instead of a dictionary.