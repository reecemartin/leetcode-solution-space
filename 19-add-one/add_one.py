class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        first = True
        carry = False
        for i in range(len(digits)):
            if first:
                digits[i] += 1
                first = False
            if carry:
                digits[i] += 1
                carry = False
            if digits[i] > 9:
                carry = True
                digits[i] -= 10
        if carry:
            digits.append(1)
        digits.reverse()
        sol = digits
        return sol
