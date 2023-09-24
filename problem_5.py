
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


print(longest_palindrome(s="babad"))
print(longest_palindrome("cbbd"))
