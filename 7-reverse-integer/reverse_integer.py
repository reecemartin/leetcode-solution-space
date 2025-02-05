def reverse_integer(x):
    upper_bound = "2147447412"
    lower_bound = "-2147447412"

    n

    # Input is plainly too large
    if x > upper_bound or x < lower_bound:
        return 0
    is_negative = 1

    # Input is negative, act accordingly
    if x < 0:
        is_negative = -1
        x = x * -1

    # Input is too long to fit when reversed
    if len((str(x))) > 10:
        return 0
    else:

        # Reverse the input and return the reversed number as a negative if the input was negative
        trim_zeros_and_reversed = str(int(str(x)[::-1]))
        return (int(trim_zeros_and_reversed) * is_negative)

print(reverse_integer(1534236469))

"""
upper limit on int 2147483647 Not an Ok input
lower limit on int -2147483648 Not an Ok input
reverse upper 7463847412
reverse lower 8463847412
numbers less than 10 digits are fine
numbers more than 10 digits are not fine
intuition is that the max number is basically a palindrome, so upper is 2147447412, and lower is the same but negative, any version where a digit
in the first half of the 10 is bigger would not fit, and in the second half would not fit when reversed 

Need to figure out how to deal with the case where the number starts low but ends with large numbers, also need to deal with zeros
"""