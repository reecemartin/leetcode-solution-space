def reverse_integer(x):
        upper_bound_raw = "2147483647"
        lower_bound_raw = "2147483648"
        bound_raw = ""
        is_negative = 1

        # Input is negative, act accordingly
        if x < 0:
            is_negative = -1
            x = x * -1
            bound_raw = lower_bound_raw
        else:
            bound_raw = upper_bound_raw

        trim_zeros_and_reversed = str(int(str(x)[::-1]))
        x_as_string = str(x)

        # Input is at the limit and invalid
        if x_as_string == bound_raw:
            return 0
        bigger_followed_by_smaller = True
        
        # Check the input digit by digit to make sure it is not too large when reversed, larger digits are ok, 
        # only if preceeded by smaller ones (higher place value)
        if len(x_as_string) == 10:
            bound_raw_reversed = bound_raw[::-1]
            for i, item in enumerate(bound_raw):
                if bound_raw_reversed[i] < x_as_string[i]:
                    bigger_followed_by_smaller = False
                elif bound_raw_reversed[i] > x_as_string[i]:
                    bigger_followed_by_smaller = True

        if not bigger_followed_by_smaller:
            return 0

        # If the input is not too long reverse, or out of bounds the input and return the reversed number 
        # as a negative if the input was negative
        return (int(trim_zeros_and_reversed) * is_negative)

print(reverse_integer(1563847412))
