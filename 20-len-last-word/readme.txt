March 11, 2025 - Easy

Link: 
https://leetcode.com/problems/length-of-last-word/description/

Problem:
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal

consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

 

Constraints:

    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.

Solution:
This one was easy, turn the string into a list splitting on the spaces, find the first non-zero length element (could have stripped)
and return it's length! (Redid with a strip making it just two lines of code and improved memory significantly)

Solution beats 100% on speed and 88% on memory.