

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
