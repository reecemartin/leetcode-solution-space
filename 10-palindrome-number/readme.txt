February 17, 2025 - Easy

Link: 
https://leetcode.com/problems/palindrome-number/description/

Problem:
Given an integer x, return true if x is a
palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 

Constraints:

    -231 <= x <= 231 - 1

 
Follow up: Could you solve it without converting the integer to a string?

Solution:
I am going to try to solve this immediately without converting to a string - which seems to be the extended version of the problem. There is a trivial
case where the number is less than 0 and then the question determines it is not a palindrome by default because it only has a negative sign on one, 
side. Meanwhile any number less than 10 is a palindrome by default For remaining numbers we have two cases, one where there are an even number of 
digits, the other where the number is odd. In one case we ignore the middle number, in the other there is not a middle number to ignore. To solve the
problem I used a list a stack.

I got this working properly but the result only beats 5% on time and 20% on memory, so it is time to optimize. The first thing I did was remove my 
prints and change the two cases into a single case with an if in the middle in case the number is odd in number of digits, this now beats 80% on
memory. 

I wrote one more version which simultaneously works from outside in to validate whether the number is a palindrome and this now beats 37% on time, and 
60% on memory. Most better performers seem to use strings.