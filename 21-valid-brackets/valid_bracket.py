Ellen Chen


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False
        for bracket in s:
            if len(stack) == 0 and bracket in [')', '}', ']']:
                return False
            if bracket == '[' or bracket == '(' or bracket == '{':
                stack.append(bracket)
            else:
                if bracket == ']':
                    if stack[len(stack) - 1] == '[':
                        stack.pop()
                    else:
                        return False
                elif bracket == ')':
                    if stack[len(stack) - 1] == '(':
                        stack.pop()
                    else:
                        return False
                elif bracket == '}':
                    if stack[len(stack) - 1] == '{':
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0
