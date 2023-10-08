

class Solution:
    def myAtoi(self, s: str) -> int:
        result = ''

        s = s.strip()

        if not s:
            return 0

        if len(s) == 1:
            if not s[0].isdigit():
                return 0
            return int(s[0])

        for i in range(0, len(s)):
            if i == len(s) - 1:
                element = s[i]
                if element.isdigit():
                    result += element
            else:
                element = s[i]

                if element.isdigit() and not s[i+1].isdigit():
                    result += element
                    break
                result += element

        new_result = ''

        for i in range(len(result)):

            if i == len(result) - 1:
                element = result[i]
                if element.isdigit():
                    new_result += element
            else:
                element = result[i]
                if element in "+-" or element.isdigit():
                    new_result += element
                elif (element not in "+-" or not element.isdigit()) and result[i+1].isdigit():
                    return 0

        if "+-" in result or "-+" in new_result:
            return 0

        try:
            new_result = int(new_result)
        except ValueError:
            return 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if new_result > INT_MAX:
            return INT_MAX

        if new_result < INT_MIN:
            return INT_MIN

        return new_result


solution = Solution()
print(solution.myAtoi("42"))
print(solution.myAtoi("  -42"))
print(solution.myAtoi("4193 with words"))
print(solution.myAtoi("words and 987"))
print(solution.myAtoi("123 1234"))
print(solution.myAtoi(".1"))
