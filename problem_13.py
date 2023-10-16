
class Solution:
    def romanToInt(self, s: str) -> int:
        matches = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }

        numbers = []

        index = 0

        while index != len(s):
            if index != len(s) - 1:
                comb = s[index] + s[index + 1]
                if comb in matches:
                    numbers.append(matches[comb])
                    index += 2
                else:
                    numbers.append(matches[s[index]])
                    index += 1
            else:
                numbers.append(matches[s[index]])
                index += 1

        return sum(numbers)


sol = Solution()
print(sol.romanToInt("III"))
print(sol.romanToInt("LVIII"))
print(sol.romanToInt("MCMXCIV"))
