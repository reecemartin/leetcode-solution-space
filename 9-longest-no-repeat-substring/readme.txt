February 8, 2025 - Medium

Link: 
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Problem:
Given a string s, find the length of the longest
substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

Solution:
Initially was confused into thinking it was no repeats sequentially, not in the entire substring, but I can still use 
my code for checking if the character is a repeat, since repeats will be between any such substrings.

Turned out I was wrong, trying to adapt the code didn't make sense so I tried to rewrite it to simplify, and eventually
I got it working, albeit with 5% runtime and 11% memory performance, not good! I will try and optimize. Second version beats
47% on memory and about 10% on runtime.