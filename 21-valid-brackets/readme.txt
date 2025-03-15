March 14, 2025 - Easy

Link: 
https://leetcode.com/problems/valid-parentheses/submissions/1574034082/

Problem:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

Solution:
Another easy one, just use a stack and to handle different types of brackets we just use different cases, if the stack is empty everything
is closed and so next bracket must be opening.

Solution beats 100% on speed and 10% on memory.