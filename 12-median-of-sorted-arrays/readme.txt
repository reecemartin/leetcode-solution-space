February 21, 2025 - Hard

Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

Problem:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

 

Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

Solution:
This one is going to take some thinking *before* I dive into writing code. 

Merge can be done in m + n time, but we need log (m + n) so the approach needs to be smarter. The median is the middle number of the two arrays, if there
are repeats its still the middle. If there are an odd number its the average of the two middle elements.

First obvious question is, can the medians of the individual lists somehow be combined into the median of the merged?

I think based on the sort of implication that we should do some binary searches (log n time) that a good approach is to search for the median of one in 
the other. Ultimately we want to find the index in the two lists where roughly the same amount of numbers (across the two) are larger vs. smaller. For 
example, assume we have the lists [1,2,3,4,5] and [1,5,10,15] searching for the median of the first in the second tells us that the middle number of 
a 5 element list with two bigger and two smaller has 3 elements larger than it in a four element list. Since we are looking for the 5th number overall, 
that number must be the smaller of the next two elements between the two lists (this may not be the way we want to extend this algo).



If an odd number of elements:



If an even number of elements: