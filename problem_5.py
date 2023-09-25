
def longest_palindrome(s: str):
    longest = ''

    for char in s:
        s = s[1:]
        substring = char
        for j in s:
            substring = substring + j
            if substring == substring[::-1] and len(substring) > len(longest):
                longest = substring

    return longest


def longest_palindrome(s: str):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    ans = [0, 0]

    for i in range(n):
        dp[i][i] = True

    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            ans = [i, i+1]

    for diff in range(2, n):
        for i in range(n-diff):
            j = i + diff


# print(longest_palindrome("babad"))
# print(longest_palindrome("cbbd"))
# print(longest_palindrome("v"))
# print(longest_palindrome('ac'))


length = 6

a = [[False] * length for _ in range(length)]
print(a)
