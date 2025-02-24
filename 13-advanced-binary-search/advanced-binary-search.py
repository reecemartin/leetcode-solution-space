import math

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) - 1
        middle = math.floor((right_index - left_index) / 2)

        if nums[right_index] == target:
            return right_index
        elif nums[left_index] == target:
            return left_index
        elif nums[right_index] < target:
            return right_index + 1
        elif nums[left_index] > target:
            return left_index

        while right_index - left_index > 1:
            #print("Left: " + str(left_index))
            #print("Right: " + str(right_index))
            #print("Middle: " + str(middle))
            if nums[middle] > target:
                right_index = middle
            elif nums[middle] == target:
                return middle
            else:
                #print("active")
                left_index = middle
            middle = math.floor((right_index - left_index) / 2) + left_index
            #print(middle)
        return middle + 1