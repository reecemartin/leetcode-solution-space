pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {

        // Validated: Takes a vector and returns the index of the middle number of an odd length vector, or the left of middle in an even length vector
        fn find_middle(nums: Vec<i32>) -> i32 {
            if nums.len() % 2 == 0 {
                (nums.len() / 2) as i32 - 1
            } else {
                (nums.len() - 1) as i32 / 2
            }
        }

        // Validated: Takes a vector and a target number and returns a vector containing the the index (index after the number it should appear 
        // after if not found) and 1 if found, 0 if not found
        fn find_index( nums: Vec<i32>, target: i32) -> Vec<usize> {
            // Didn't want to implement binary search so I used code from here: https://spin.atomicobject.com/learning-rust-binary-search/
            // Add to my todo list to implement binary search
            let length = nums.len();
            let mut half = length / 2;
            let mut hind = length - 1;
            let mut lind = 0;
            let mut current = nums[half];

            while lind <= hind { match current.cmp(&target) { 
                        std::cmp::Ordering::Equal => return vec![half, 1],
                        std::cmp::Ordering::Less => lind = half + 1,
                        std::cmp::Ordering::Greater => hind = half - 1,
                    }
                    half = (hind + lind) / 2;
                    current = nums[half];
            }
            return vec![lind - 1, 0];
        }

        // Validated: Takes a vector, an index, and whether to consider that index in the count and returns a vector where the first number is the 
        // number of values in front of that index and the second is the number of values behind that index
        fn find_greater_and_less_than(nums: Vec<i32>, index: i32, in_nums: bool) -> Vec<i32> {
            if in_nums {
                vec![index, (nums.len() - (index + 1) as usize) as i32]
            } else {
                vec![index + 1, (nums.len() - (index + 1) as usize) as i32]
            }      
        } 


        let nums1_middle = find_middle(nums1.clone());

        print!("Middle of Nums 1: {}\n", nums1[nums1_middle as usize]);

        let loc_in_nums2 = find_index(nums2.clone(), nums1[nums1_middle as usize]);

        print!("{:?}\n", loc_in_nums2);

        let g_l1 = find_greater_and_less_than(nums1.clone(), nums1_middle, true);
        let g_l2 = find_greater_and_less_than(nums2, loc_in_nums2[0] as i32, loc_in_nums2[1] == 1);
        print!("{:?}\n", g_l1);
        print!("{:?}\n", g_l2);
        if g_l1[0] + g_l2[0] - g_l1[1] + g_l2[1] >= 1 {
            return nums1[nums1_middle as usize]
        } 
        
        return -1


}

fn main() {
    let mut vec1 = vec![1, 2, 3, 4, 5];
    let mut vec2 = vec![1, 2, 4, 5];

    print!("Vector 1: {:?}\n", vec1);
    print!("Vector 2: {:?}\n", vec2);

    print!("Result: {:?}", find_median_sorted_arrays(vec1, vec2))
}
