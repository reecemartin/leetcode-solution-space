def longest_no_repeat_substring(s):
    substrings = {}
    max_size_set = 0
    keys_to_remove = []
    
    # For every character in the string create a new substring in our dictionary which is the one starting from that index
    for index, character in enumerate(s):
        
        substrings[index] = {""}
        
        # For all our substrings, if they don't have the current character add it, if they are shorter than the max length subset remove them
        for x in substrings:
            # print("Inner Loop")
            # print(character)
            # print(substrings)
            # print(x)
            # print(character not in substrings[x])
            
            if character not in substrings[x]:
                substrings[x].add(character)
                if "" in substrings[x]:
                    substrings[x].remove("")
            else:
                if len(substrings[x]) > max_size_set:
                    max_size_set = len(substrings[x])
                keys_to_remove.append(x)
                
        for key in keys_to_remove:
            substrings.pop(key)
        keys_to_remove.clear()
        
        # print("Outer Loop \n")
        # print(substrings)
                
    # print("Break")
    # print(substrings)
    for x in substrings:
        if len(substrings[x]) < max_size_set:
            keys_to_remove.append(x)
        else:
            max_size_set = len(substrings[x])
            
    return max_size_set

def longest_no_repeat_substring_2(s):
    substrings = {}
    max_size_set = 0
    keys_to_remove = []
    
    # For every character in the string create a new substring in our dictionary which is the one starting from that index
    for index, character in enumerate(s):
        
        substrings[index] = set()
        
        # For all our substrings, if they don't have the current character add it, if they are shorter than the max length subset remove them
        for x in substrings:
            
            if character not in substrings[x]:
                substrings[x].add(character)
            else:
                if len(substrings[x]) > max_size_set:
                    max_size_set = len(substrings[x])
                keys_to_remove.append(x)
                
        for key in keys_to_remove:
            substrings.pop(key)
        keys_to_remove.clear()
        
        print(substrings)
                
    for x in substrings:
        if len(substrings[x]) > max_size_set:
            max_size_set = len(substrings[x])
            
    return max_size_set


print(longest_no_repeat_substring_2("abcabcbb"))