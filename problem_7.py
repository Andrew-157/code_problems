

def reverse(x: int):
    result: str = ''

    for i in str(x)[::-1]:
        if i == '-':
            continue
        result += i
        if not int(result).bit_count() <= 32:
            return 0

    if '-' in str(x):
        result = '-' + result

    return int(result)


a = 2147483651

print(a.bit_length())
