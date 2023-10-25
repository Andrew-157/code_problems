from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        characters = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        if len(digits) == 0:
            return []

        result = []

        self.solve(digits=digits, characters=characters, result=result)

        return result

    def solve(self, digits, characters: dict, result: list, current_string="", current_level=0):
        if current_level == len(digits):
            result.append(current_string)
            return None
        for i in characters[digits[current_level]]:
            self.solve(digits, characters, result,
                       current_string + i, current_level + 1)


sol = Solution()
print(sol.letterCombinations("279"))
