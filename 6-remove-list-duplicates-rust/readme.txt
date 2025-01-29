January 25, 2025 - Easy

Link:
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Problem:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    Return k.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

 

Constraints:

    1 <= nums.length <= 3 * 104
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.

Solution:

Once again to try to keep moving forward in Rust, I am writing a Rust solution to the remove list duplicates problem I previously solved with Python. 
As with last time I was trying to write Rust code I am getting tons of errors, but they are indeed very useful and most were easy to solve. The only
problem which required any serious change was creating a copy of my input vec to iterate over while making actual changes to the other. 

In order to get things to work I ended up changing my code to iterate over and then have a counter to see where we were index wise. The time performance
was poor relative to the best solutions so I am going to see what I need to fix. I think the issue is I did a general solution instead of one that takes
advantage of the list being in ascending order.

In my updated code I start from the beginning and only keep track of the last unique number and the index of the last duplicate, basically doing
no extra work beyond what is required. This gave me time performance beating 100% and memory performance beating 85%!