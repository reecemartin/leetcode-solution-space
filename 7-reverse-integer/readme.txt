February 2, 2025 - 

Link:
https://leetcode.com/problems/reverse-integer/description/

Problem:
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

 

Constraints:

    -231 <= x <= 231 - 1

Solution:

This problem seems smart but so little is specified I feel like a lot is ambiguous. I could just do some testing on strings and
it seems pretty trivial, but it doesn't seem to respect the "spirit" of the question. A solution I think does and will work, is breaking
the input up if its over a certain size and testing the "chunks" sizes respectively.