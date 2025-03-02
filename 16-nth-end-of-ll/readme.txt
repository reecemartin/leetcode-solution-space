March 1, 2025 - Medium

Link: 
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Problem:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

 

Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

 

Follow up: Could you do this in one pass?

Solution:
This one wasn't too hard, it required a bit of debugging and playing around with corner cases on short lists but I did it fairly quickly.
The "challenge" was doing it in one pass, and I did that no problem, but my solution using a list is probably needlessly memory hungry. Want
to fix this by just using two pointers, which seems obvious in retrospect.

Solution beats 100% on speed and 13% on memory.