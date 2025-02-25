February 24, 2025 - Medium

Link: 
https://leetcode.com/problems/permutations/submissions/1554392190/

Problem:
Given an array nums of distinct integers, return all the possible

. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

 

Constraints:

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.


Solution:
This problem was not terrible, doing it recursively made a lot of sense. The only thing that was annoying was dealing with accidentally modifying, the 
common parent lists, and so a lot of copying went on.

Solution beats 100% on speed and 33% on memory.