from typing import List


class Solution:

    def generate(self, left: int, right: int, comb: str, answer: List[str]):

        if left == 0 and right == 0:
            answer.append(comb)

        if left > right or left < 0 or right < 0:
            return None

        comb += '('
        self.generate(left - 1, right, comb, answer)
        comb = comb[:-1]
        comb += ')'
        self.generate(left, right - 1, comb, answer)
        comb = comb[:-1]

    def generateParenthesis(self, n: int) -> List[str]:
        combs: List[str] = []
        comb = ''
        left = right = n
        self.generate(left, right, comb, combs)
        return combs


sol = Solution()
print(sol.generateParenthesis(n=8))
