class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        slide_over = 0
        k = 0
        for i in range(len(nums)):
            print(nums[i])
            if nums[i] == val:
                slide_over += 1
            else:
                k += 1
                if slide_over > 0:
                    nums[i - slide_over] = nums[i]
                    # slide_over -= 1
        return k
    
l = [0,1,2,2,3,0,4,2]
print(Solution.removeElement(Solution, l, 2))
print(l)
        
                
                