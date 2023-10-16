# class Solution:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
#         if "" in strs or not strs:
#             return ""

#         prefix = strs[0]

#         for i in range(1, len(strs)):
#             word = strs[i]
#             index = 1
#             substr = prefix[0]
#             while substr in word:
#                 if substr == word:
#                     break
#                 elif index > len(prefix):
#                     break
#                 substr += prefix[index]
#                 index += 1
#             if not prefix:
#                 return ""

#         return prefix


# sol = Solution()
# print(sol.longestCommonPrefix(["flower", "flow", "flight"]))


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if "" in strs or not strs:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            word = strs[i]

            substr = ''
            index = 0

            while index < len(prefix) \
                    and index < len(word)\
                    and word[index] == prefix[index]:
                substr += word[index]
                index += 1

            if not substr:
                return ''

            prefix = substr

        return prefix


sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
print(sol.longestCommonPrefix(strs=["dog", "racecar", "car"]))
