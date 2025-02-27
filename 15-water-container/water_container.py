class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        def areaOf(height, left_wall, right_wall):
            return min(height[left_wall], height[right_wall]) * (right_wall - left_wall)

        left_wall = 0
        right_wall = len(height) - 1
        max_area = areaOf(height, left_wall, right_wall)

        while left_wall != right_wall:
            if areaOf(height, left_wall, right_wall) > max_area:
                max_area = areaOf(height, left_wall, right_wall)
            if height[left_wall] > height[right_wall]:
                right_wall -= 1
            elif height[left_wall] < height[right_wall]:
                left_wall += 1
            else:
                left_wall += 1
                if left_wall == right_wall:
                    break
                right_wall -= 1
        
        return max_area