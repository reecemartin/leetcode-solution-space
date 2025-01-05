def removeListDuplicates_3(nums):
    uni_count = 1
    for index in range(1, len(nums)):
        if nums[index - 1] != nums[index]:
            nums[uni_count] = nums[index]
            uni_count += 1
    return uni_count

def removeListDuplicates_2(nums):
    uni_count = 0
    last_number = -101
    for index in range(len(nums)):
        if nums[index] != last_number:
            nums[uni_count] = nums[index]
            uni_count += 1
            last_number = nums[index]
    return uni_count

def removeListDuplicates_1(nums):
    uni_count = 0
    last_number = -101
    for index, item in enumerate(nums):
        if nums[index] != last_number:
            nums[uni_count] = item
            uni_count += 1
            last_number = nums[index]
    return uni_count

print(removeListDuplicates_3([1,1,1,1,2,2,3,3,3,4,5]))