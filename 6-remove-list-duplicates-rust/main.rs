mod remove_duplicates {
    use std::collections::HashSet;
    use std::convert::TryInto;

    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut numbers_seen: HashSet<i32> = HashSet::new();
        let vec_of_numbers: Vec<i32> = nums.to_vec();
        let mut count = vec_of_numbers.len();
        for i in vec_of_numbers.into_iter().rev() {
            if numbers_seen.contains(&i) {
                nums.remove(count);
                nums.push(0);
                count -= 1;
            } else {
                numbers_seen.insert(i);
                count -= 1;
            }
        }
        return numbers_seen.len().try_into().unwrap();
    }

    pub fn remove_duplicates_2(nums: &mut Vec<i32>) -> i32 {
        let mut last_unique_number = -101;
        let mut last_duplicate_index = 1;
        let vec_of_numbers: Vec<i32> = nums.to_vec();
        let mut loop_count = 0;
        let mut unique_count = 0;
        for i in vec_of_numbers {
            if i > last_unique_number {
                last_unique_number = i;
                if loop_count != 0 {
                    nums[last_duplicate_index] = last_unique_number;
                    last_duplicate_index += 1;
                }
                loop_count += 1;
                unique_count += 1;
            } else {
                last_duplicate_index = unique_count;
                loop_count += 1;
            }
        }
        return unique_count.try_into().unwrap();
    }
}

fn main() {
    use remove_duplicates::remove_duplicates_2;
    let mut vec_of_numbers: Vec<i32> = Vec::<i32>::new();
    vec_of_numbers.push(1);
    vec_of_numbers.push(2);
    // vec_of_numbers.push(2);
    // vec_of_numbers.push(2);
    // vec_of_numbers.push(3);
    // vec_of_numbers.push(3);
    println!("{}", remove_duplicates_2(&mut vec_of_numbers));
    print!("{:?}", vec_of_numbers)
    // Try switching the above to drop the 0 and see that indexing works properly
}
