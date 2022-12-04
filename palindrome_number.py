def is_palindrome(x: int) -> bool:
    """
    :param x: number to check for palindrome
    :return: bool; true if number is a palindrome
    """
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False


print(is_palindrome(21412))
