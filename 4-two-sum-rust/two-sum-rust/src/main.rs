mod two_sum{
    use std::collections::HashMap;
    use std::convert::TryInto;

    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        
        let mut seen_numbers: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut result: Vec<Vec<i32>> = Vec::new();

        // print!("function running");
        for (index, element) in nums.into_iter().enumerate() {
            let search_for = target - element;
            // print!("{:?}", seen_numbers);
            if seen_numbers.contains_key(&search_for) {
                result.push(vec![index.try_into().unwrap(), element]);
                result.push(vec![seen_numbers.get(&search_for).unwrap()[0],seen_numbers.get(&search_for).unwrap()[1]])
            } else {
                // print!("\n Else running ");
                seen_numbers.insert(element, vec![index.try_into().unwrap(), element]);
            }

        }

        return vec![result[0][0], result[1][0]];
    }

}

fn main() {
    use crate::two_sum::two_sum;
    // print!("hello!");
    let vec1 = vec![1, 2, 11, 4, 5];
    print!("{:?}", two_sum(vec1, 7));
}