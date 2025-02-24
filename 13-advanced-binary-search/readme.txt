February 23, 2025 - Easy

Link: 
https://leetcode.com/problems/search-insert-position/

Problem:
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

 

Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104

Solution:
Solving this wasn't too bad! I was nervous beacuse of annoying edge cases, and they were there, but most were related to the special (if not in list) condition
as opposed to binary search itself, which I got working in about 15 minutes consistently. I only really needed an edge case for the search for the final element
since the "middle" was arrived at by rounding *down* as opposed to up.

Solution beats 100% on speed and 5% on memory.