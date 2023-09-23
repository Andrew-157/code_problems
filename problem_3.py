
def length_of_longest_substring(s: str) -> int:
    longest = ''
    while s:
        substring = ''
        for char in s:
            if char in substring:
                break
            else:
                substring += char
        if len(substring) > len(longest):
            longest = substring
        s = s.replace(s[0], '')
    print(longest)
    return len(longest)


# print(length_of_longest_substring(s="abcabcbb"))
# print(length_of_longest_substring(s="bbbbb"))
# print(length_of_longest_substring(s="pwwkew"))
# print(length_of_longest_substring(s="dvdf"))


def length_of_longest_substring(s: str):
    longest = ''

    for char in s:
        s = s[1:]
        substring = char
        for j in s:
            if j in substring:
                break
            else:
                substring += j
        if len(substring) > len(longest):
            longest = substring

    return len(longest)


print(length_of_longest_substring(s="abcabcbb"))
print(length_of_longest_substring(s="bbbbb"))
print(length_of_longest_substring(s="pwwkew"))
print(length_of_longest_substring(s="dvdf"))
