class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(nums: list[int], cur_permutation: list[int], accumulate: list[list[int]]):
            if len(nums) == 1:
            #print("Final")
                cur_permutation.append(nums[0])
            #print(cur_permutation)
                accumulate.append(cur_permutation.copy())
            #cur_permutation.clear()
            #print(accumulate)
            else:
                for i in range(len(nums)):  
                    #print(cur_permutation)
                    current_element = nums[i]
                    new_cur_permutation = cur_permutation.copy()
                    new_cur_permutation.append(current_element)
                    helper(nums[:i] + nums[i+1:], new_cur_permutation, accumulate)
                    #new_cur_permutation.clear()

        accumulate = []
        helper(nums, [], accumulate)
        return accumulate