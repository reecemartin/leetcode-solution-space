January 11, 2025 - Medium

Link: 
https://leetcode.com/problems/add-two-numbers/description/

Problem: 
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

 

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.



Solution:

My initial solution lame as it seems is just to extract the numbers from two Linked Lists and then reconstuct a new one with their sum. (Note: I have
started just copying the headers from Leetcode, which is kind of cheating and I need to learn that formatting some other way.) I tried to append 
lists doing += [val] but it wasn't working so I switched to .append. I also got some issues due to being a dumbo regarding bedmas and exponentiation.
I decided to do this with nested functions since what I am effectively doing is a ll to int conversion and the reverse. I validated to ll to int
function first and then started debugging the int to ll function. Initially messed up because I was treating an int like a string before I had 
converted it. Annoyingly they want all three lists, both inputs and the outputs to be reversed, so I needed to add a reverse function to do this. 
After I completed the revere function I was able to pass all tests but only with performance beating 5% of submissions and 23% on memory, so I will
try to optimize. 

I ended up looking at how people were doing better, and as I guessed they are doing the additions in place and carrying values, which does make
sense with the lists being in reversed order. I think my solution is a little less confusing to write, but it is much slower so I will make my task 
for tomorrow be rewriting this the "right" way.