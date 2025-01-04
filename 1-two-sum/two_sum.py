def two_sum_3(nums, target):
    search = set()
    for x, item_1 in enumerate(nums):
        if (target - item_1) in search:
            return [nums.index(target - item_1), x]
        else:
            search.add(item_1)

def two_sum_2(nums, target):
    search = {}
    for x, item_1 in enumerate(nums):
        if (target - item_1) in search:
            return [search[(target - item_1)], x]
        else:
            search[item_1] = [x]

def two_sum_1(nums, target):
    for x, item_1 in enumerate(nums):
        for y, item_2 in enumerate(nums[x + 1:]):
            print(item_1, item_2)
            if (item_1 + item_2 == target):
                return [x, x + y + 1]