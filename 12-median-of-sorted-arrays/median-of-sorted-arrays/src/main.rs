// Attempt 1
pub fn find_median_sorted_arrays_bad(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
    // Validated: Takes a vector and returns the index of the middle number of an odd length vector, or the left of middle in an even length vector, starting
    // at start and stopping before stop
    fn find_middle(start: i32, stop: i32) -> i32 {
        if (stop - start) % 2 == 0 {
            ((stop - start) / 2) as i32 - 1 + start
        } else {
            (stop - start - 1) as i32 / 2 + start
        }
    }

    // Validated: Takes a vector and a target number and returns a vector containing the the index (index after the number it should appear
    // after if not found) and 1 if found, 0 if not found
    fn find_index(nums: Vec<i32>, target: i32) -> Vec<usize> {
        // Didn't want to implement binary search so I used code from here: https://spin.atomicobject.com/learning-rust-binary-search/
        // Add to my todo list to implement binary search

        if nums.len() == 1 {
            let correct_value = if nums[0] == target { 1 } else { 0 };
            let index = if nums[0] > target { 0 } else { 1 };
            return vec![index, correct_value];
        }

        if nums.len() == 2 {
            if nums[0] == target {
                return vec![0, 1];
            }
            if nums[1] == target {
                return vec![1, 1];
            }
            if target < nums[0] {
                return vec![0, 0];
            }
            if target > nums[0] && target < nums[1] {
                return vec![1, 0];
            }
            return vec![2, 0];
        }

        let length = nums.len();
        let mut half: usize = length / 2;
        let mut hind: usize = length - 1;
        let mut lind = 0;
        let mut current = nums[half];

        while lind <= hind {
            match current.cmp(&target) {
                std::cmp::Ordering::Equal => return vec![half, 1],
                std::cmp::Ordering::Less => lind = half + 1,
                std::cmp::Ordering::Greater => hind = half - 1,
            }
            half = (hind + lind) / 2;
            current = nums[half];
        }
        return vec![lind, 0];
    }

    // Validated: Takes a vector, an index, and whether to consider that index in the count and returns a vector where the first number is the
    // number of values in front of that index and the second is the number of values behind that index
    fn find_greater_and_less_than(nums: Vec<i32>, index: i32, in_nums: bool) -> Vec<i32> {
        if in_nums {
            vec![index, (nums.len() - (index + 1) as usize) as i32]
        } else {
            vec![index, (nums.len() - (index) as usize) as i32]
        }
    }

    let mut nums1_start = 0;
    let mut nums2_start = 0;
    let mut nums1_stop = nums1.len();
    let mut nums2_stop = nums2.len();

    loop {
        let nums1_middle_index = find_middle(nums1_start, nums1_stop as i32);

        print!("Middle of Nums 1: {}\n", nums1[nums1_middle_index as usize]); // REMOVE ME

        let loc_in_nums2 = find_index(nums2.clone(), nums1[nums1_middle_index as usize]);

        print!("Located in Nums2: {:?}\n", loc_in_nums2); // REMOVE ME

        let g_l1 = find_greater_and_less_than(nums1.clone(), nums1_middle_index, true);
        let g_l2 =
            find_greater_and_less_than(nums2.clone(), loc_in_nums2[0] as i32, loc_in_nums2[1] == 1);
        print!("{:?}\n", g_l1); // REMOVE ME
        print!("{:?}\n", g_l2); // REMOVE ME
        print!("{:?}\n", g_l1[0] + g_l2[0] - (g_l1[1] + g_l2[1]));
        if (g_l1[0] + g_l2[0] - (g_l1[1] + g_l2[1])).abs() <= 1 {
            return nums1[nums1_middle_index as usize];
        }

        let nums2_middle_index = find_middle(nums2_start, nums2_stop as i32);

        print!("Middle of Nums 2: {}\n", nums2[nums2_middle_index as usize]); // REMOVE ME

        let loc_in_nums1 = find_index(nums1.clone(), nums2[nums2_middle_index as usize]);

        print!("Located in Nums1: {:?}\n", loc_in_nums1); // REMOVE ME

        let g_l1 = find_greater_and_less_than(nums2.clone(), nums2_middle_index, true);
        let g_l2 =
            find_greater_and_less_than(nums1.clone(), loc_in_nums1[0] as i32, loc_in_nums1[1] == 1);
        print!("{:?}\n", g_l1); // REMOVE ME
        print!("{:?}\n", g_l2); // REMOVE ME
        if (g_l1[0] + g_l2[0] - (g_l1[1] + g_l2[1])).abs() <= 1 {
            return nums2[nums2_middle_index as usize];
        }

        // Probably can use whether the above is negative to do the adjustments for where we are looking

        print!("\n\n CHECK"); // REMOVE ME
        print!("{}\n", loc_in_nums2[0]); // REMOVE ME
        print!("{}", nums2_middle_index as usize); // REMOVE ME
        print!("\n\n"); // REMOVE ME

        if loc_in_nums2[0] - 1 < nums2[nums2_middle_index as usize] as usize {
            nums1_start = nums1_middle_index;
        } else {
            nums1_stop = nums1_middle_index as usize;
        }

        if loc_in_nums1[0] - 1 < nums1[nums1_middle_index as usize] as usize {
            nums2_start = nums2_middle_index;
        } else {
            nums2_stop = nums2_middle_index as usize;
        }

        print!("\n\n"); // REMOVE ME
        print!("{}\n", nums1_start); // REMOVE ME
        print!("{}", nums1_stop); // REMOVE ME
        print!("\n\n"); // REMOVE ME
    }
}

// Attempt 2
pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {

    // Validated: Takes a vector and returns the index of the middle number of an odd length vector, or the left of middle in an even length vector, starting
    // at start and stopping at stop inclusive 0 1 2 3 4
    fn find_middle_index_in_range(start: i32, stop: i32) -> i32 {
        if ((stop + 1) - (start)) % 2 == 0 {
            (((stop + 1) - (start)) / 2) - 1 + start
        } else {
            ((stop + 1) - (start) - 1) / 2 + start
        }
    }

    fn verify_overall_median(nums1: Vec<i32>, index1: i32, nums2: Vec<i32>, index2: i32) -> i32 {
        if (nums1.len() as i32 - (index1 + 1)) + (nums2.len() as i32 - (index2 + 1)) - (index1 - 1) + (index2 - 1) <= 1 {
            return nums1[index1 as usize]
        } else {
            return -1
        }
    }

    let mut nums1_start = 0;
    let mut nums1_end = (nums1.len() - 1) as i32;

    let mut nums2_start = 0;
    let mut nums2_end = (nums2.len() - 1) as i32;

    loop {
        let nums1_current_middle = find_middle_index_in_range(nums1_start, nums1_end);
        let nums2_current_middle = find_middle_index_in_range(nums2_start, nums2_end);

        print!("\n");
        print!("Nums1 Middle: {}\n", nums1_current_middle);
        print!("Nums2 Middle: {}\n", nums2_current_middle);
        print!("\n");

        if verify_overall_median(nums1.clone(), nums1_current_middle, nums2.clone(), nums2_current_middle) != -1 {
            return verify_overall_median(nums1, nums1_current_middle, nums2, nums2_current_middle)
        }

        if nums1[nums1_current_middle as usize] > nums2_current_middle {
            nums1_end = nums1_current_middle;
            nums2_start = nums2_current_middle;
        } else {
            nums1_start = nums1_current_middle;
            nums2_end = nums2_current_middle
        }
    }

    5

    // Function to validate median given two indices and two vecs
}

fn main() {
    // 1,3    2       -> 2
    // 1,2    3,4     -> 2.5

    let mut vec1 = vec![1, 3, 4, 5];
    let mut vec2 = vec![2, 4, 16, 32];

    print!("Vector 1: {:?}\n", vec1);
    print!("Vector 2: {:?}\n", vec2);

    print!("Result: {:?}", find_median_sorted_arrays(vec1, vec2))
}
