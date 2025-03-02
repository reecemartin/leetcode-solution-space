class Solution:


def maxAreaFail1(height: list[int]) -> int:
    max_area = 0
    iterations = 0
    for i in range(len(height)):
        delta = 0
        for j in range(i+1, len(height)):
            iterations += 1
            area = min(height[i], height[j]) * (j-i)
            if area > max_area:
                print("Left: ", height[i], "Right: ",
                      height[j], "Area: ", area)
                max_area = area

    print(iterations)
    return max_area


def maxAreaFail2(height: list[int]) -> int:
    max_indices = [0, len(height)-1]
    current_area = min(height[0], height[len(height)-1]) * (len(height)-1)

    # Find the two tallest walls
    for i in range(len(height)):
        if height[i] > height[max_indices[0]]:
            max_indices[1] = max_indices[0]
            max_indices[0] = i
        elif height[i] > height[max_indices[1]]:
            max_indices[1] = i

    current_y = min(height[max_indices[0]], height[max_indices[1]])
    current_x = abs(max_indices[1] - max_indices[0])
    if current_area < current_y * current_x:
        current_area = current_y * current_x

    right_wall = max(max_indices[0], max_indices[1])
    left_wall = min(max_indices[0], max_indices[1])

    # Try moving the right Wall
    for i in range(right_wall + 1, len(height)):
        if (current_x + i - right_wall) * min(current_y, height[i]) > current_area:
            current_area = (current_x + i - right_wall) * \
                min(current_y, height[i])
            max_indices.remove(right_wall)
            right_wall = i
            max_indices.append(right_wall)
            current_y = min(height[max_indices[0]], height[max_indices[1]])
            current_x = abs(max_indices[1] - max_indices[0])

    # Try moving the left Wall
    for i in range(0, left_wall):
        if (current_x + (left_wall - i)) * min(current_y, height[i]) > current_area:
            current_area = (current_x + (left_wall - i)) * \
                min(current_y, height[i])
            max_indices.remove(left_wall)
            left_wall = i
            max_indices.append(left_wall)
            current_y = min(height[max_indices[0]], height[max_indices[1]])
            current_x = abs(max_indices[1] - max_indices[0])

    return current_area


def maxAreaFail3(height: list[int]) -> int:

    def area_of(height: list[int], left: int, right: int):
        return min(height[left], height[right]) * (right - left)

    left_wall = 0
    right_wall = len(height) - 1
    max_area = area_of(height, left_wall, right_wall)

    print(iterations)
    return max_area


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
