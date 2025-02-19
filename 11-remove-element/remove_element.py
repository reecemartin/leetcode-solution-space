class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        slide_over, k = 0, 0
        for i in range(len(nums)):
            if nums[i] == val:
                slide_over += 1
            else:
                k += 1
                if slide_over > 0:
                    nums[i - slide_over] = nums[i]
        return k
    
l = [0,1,2,2,3,0,4,2]
print(Solution.removeElement(Solution, l, 2))
print(l)
        
                
                