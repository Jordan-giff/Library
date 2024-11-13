#[V00710262] [Jordan] [McDowell]

ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS = "0123456789"

def is_alpha(s: str) -> bool:
    for char in s:
        if char not in ASCII_LOWERCASE and char not in ASCII_UPPERCASE:
            return False
    return True

def is_digit(s: str) -> bool:
    for char in s:
        if char not in DECIMAL_DIGITS:
            return False
    return True

def to_lower(s: str) -> str:
    result = ""
    for char in s:
        if char in ASCII_UPPERCASE:
            index = ASCII_UPPERCASE.index(char)
            result += ASCII_LOWERCASE[index]
        else:
            result += char
    return result
