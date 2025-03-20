class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled = []
        for i in range(len(nums) // 2):
            shuffled.append(nums[i])
            shuffled.append(nums[n + i])
        return shuffled