January 9, 2025 - Easy

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

As a beginning to get ramped up into Rust I am going to try and solve this problem again, but this time using Rust. My god rust is difficult to get
ramped up in, but I feel my brain expanding already, the language is very much explicit about everything you are doing. 

I finally solved the problem after like 2 hours of work, and my solution is great on time complexity and WAY less memory hungry than with Python, 
that being said my code seems to have a LOT of jank in it so it really is just a first attempt.