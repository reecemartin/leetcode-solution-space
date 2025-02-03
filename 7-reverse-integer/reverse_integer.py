def reverse_integer(num):
    boundary_upper = "2147483647"
    boundary_lower = "-2147483648"
    reversed = str(num)[::-1]
    trim_zeros = str(int(reversed))
    if len(trim_zeros) > 10:
        return 0
    else:
        if

    return int(reversed)

print(reverse_integer(11111111111))