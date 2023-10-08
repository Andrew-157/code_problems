
def is_palindrome(x: int):

    if x < 0:
        return False


def is_palindrome(x: int):

    if x < 0:
        return False

    reverse = 0
    temp = x

    while temp != 0:
        reverse = (reverse * 10) + (temp % 10)
        temp = temp // 10

    return reverse == x


print(is_palindrome(-121))
