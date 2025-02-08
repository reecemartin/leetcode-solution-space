def longest_no_repeat_substring(s):
    longest_count = 0
    current_count = 0
    
    last_character = ''
    for i in s:
        if i == last_character:
            print ("first active")
            if current_count > longest_count:
                print("second active")
                longest_count = current_count
            current_count = 1
        else:
            print ("third active")
            current_count += 1
            last_character = i
    return longest_count

print(longest_no_repeat_substring("abcabcbb"))