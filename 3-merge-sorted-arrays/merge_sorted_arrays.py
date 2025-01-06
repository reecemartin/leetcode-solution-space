def merge_1_without_prints(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        pos_m = m - 1
        pos_n = n - 1
        if nums1 and nums2:
            for index in reversed(range(m + n)):
                if (nums1[pos_m] > nums2[pos_n] or pos_n < 0) and pos_m > -1:
                        nums1[index] = nums1[pos_m]
                        pos_m -= 1
                else:
                        nums1[index] = nums2[pos_n]
                        pos_n -= 1
        elif not nums1:
            nums1 = nums2

def merge_1(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        pos_m = m - 1
        pos_n = n - 1
        for index in reversed(range(m + n)):
            if (nums1[pos_m] > nums2[pos_n] or pos_n < 0) and pos_m > -1:
                print(pos_n)
                print(pos_m)
                print(nums1)
                print(nums2)
                nums1[index] = nums1[pos_m]
                pos_m -= 1
                print("first array larger")
                print(index)
                print("\n")
            else:
                print(pos_n)
                print(pos_m)
                #print(nums1[pos_m])
                #print(nums2[pos_n])
                print(nums1)
                print(nums2)
                nums1[index] = nums2[pos_n]
                pos_n -= 1
                print("second array larger")
                print(index)
                print("\n")
        print(nums1)

merge([1,3,4,5,0,0,0],4,[2,6,7],3)
