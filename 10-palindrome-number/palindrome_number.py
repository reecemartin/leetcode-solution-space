class Solution:
    def isPalindrome(self, x: int) -> bool:
        import math
        
        stack = []
        
        if x < 0:
            return False
        if x < 10: 
            return True
        number_of_digits = math.floor(math.log(x, 10) + 1)
        if number_of_digits % 2 == 0:
            # print("X has even digits")
            # print(number_of_digits)
            for i in range(number_of_digits):
                if(i < number_of_digits / 2):
                    stack.append(x % 10)
                    # print(stack)
                else:
                    if(stack.pop() != x % 10):
                        return False
                x = x // 10
        else:
             # print("X has odd digits")
             for i in range(number_of_digits):
                # print(number_of_digits // 2 - 1)
                if(i < number_of_digits // 2):
                    stack.append(x % 10)
                    # print(stack)
                elif(i == number_of_digits // 2):
                    pass
                else:
                    # print(x % 10)
                    if(stack.pop() != x % 10):
                        return False
                x = x // 10
        return True
    
    # Least Memory
    def isPalindrome2(self, x: int) -> bool:
        import math
        
        stack = []
        
        if x < 0:
            return False
        if x < 10: 
            return True
        number_of_digits = math.floor(math.log(x, 10) + 1)
        for i in range(number_of_digits):
            if(i < number_of_digits // 2):
                stack.append(x % 10)
            elif(number_of_digits % 2 != 0 and i == number_of_digits // 2):
                pass
            else:
                if(stack.pop() != x % 10):
                    return False
            x = x // 10
        return True
    
    # Fastest
    def isPalindrome3(self, x: int) -> bool:
        import math
        
        stack = []
        
        if x < 0:
            return False
        if x < 10: 
            return True
        number_of_digits = math.floor(math.log(x, 10) + 1)
        for i in range(number_of_digits // 2):
            if(i < number_of_digits // 2):
                if(x % 10 != (x // 10 ** (number_of_digits - 2 * i - 1)) % 10):
                    return False
            x = x // 10
        return True
            
            
print(Solution.isPalindromeFast(Solution, 51215))