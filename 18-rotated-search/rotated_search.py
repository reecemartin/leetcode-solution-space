class Solution:
    def search(nums: list[int], target: int) -> int:
        print("First")
        front = 0
        back = len(nums) - 1
        while front < back - 1:
            middle = (back - front) // 2 + front
            print(front, middle, back)
            if nums[middle] > nums[back]:
                front = middle
            else:
                back = middle

        if nums[front] > nums[middle]:
            largest = front
            smallest = middle
        else:
            largest = middle
            smallest = back

        print("Largest:" + str(largest))
        print("Smallest:" + str(smallest))

        print("Second")
        front = 0
        back = largest
        print(front, back)
        if nums[front] == target:
            return front
        if nums[middle] == target:
            return middle
        if nums[back] == target:
            return back
        while front < back - 1:
            middle = (back - front) // 2 + front
            print(front, middle, back)
            if nums[front] == target:
                return front
            if nums[middle] == target:
                return middle
            if nums[back] == target:
                return back
            if nums[middle] > target:
                back = middle
            else:
                front = middle

        print("Third")
        front = smallest
        back = len(nums) - 1
        print(front, back)
        if nums[front] == target:
            return front
        if nums[middle] == target:
            return middle
        if nums[back] == target:
            return back
        while front < back - 1:
            middle = (back - front) // 2 + front
            print(front, middle, back)
            if nums[front] == target:
                return front
            if nums[middle] == target:
                return middle
            if nums[back] == target:
                return back
            if nums[middle] > target:
                back = middle
            else:
                front = middle
        return -1

# Removing with comments prints massively improved time performance, just removing those lines also seriously improved memory