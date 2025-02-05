February 2, 2025 - Medium

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

That ^ turned out to be the wrong approach, the right approach was just breaking it into cases. If the value equaled the bound it was bad,
if the value was too long, it was bad, then I needed to do a digit by digit comparison with the bound as a string, where our reversed, number
could only have larger digits if there was an earlier digit which was smaller to "offset" it. Dealing with the leading 0's was not an issue,
because Python drops those when going from String -> Int.

My solution once I trimmed extraneous case checking beats 80% on runtime and 70% on memory.


Notes I wrote in my code initially:
upper limit on int 2147483647 Not an Ok input
lower limit on int -2147483648 Not an Ok input
reverse upper 7463847412
reverse lower 8463847412
numbers less than 10 digits are fine
numbers more than 10 digits are not fine
intuition is that the max number is basically a palindrome, so upper is 2147447412, and lower is the same but negative, any version where a digit
in the first half of the 10 is bigger would not fit, and in the second half would not fit when reversed 
