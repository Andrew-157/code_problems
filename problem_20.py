
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'{': '}', '[': ']', '(': ')'}

        stack = []

        for char in s:
            if char in brackets.keys():
                stack.append(char)
            elif char in brackets.values():
                if len(stack) == 0:
                    return False
                bracket = stack.pop()
                if not brackets[bracket] == char:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False


sol = Solution()
print(sol.isValid(s='()'))
print(sol.isValid(s="()[]{}"))
print(sol.isValid(s="(]"))
print(sol.isValid(s="{[]}"))
