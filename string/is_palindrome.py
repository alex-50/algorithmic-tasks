# input
string_1 = "123321"
string_2 = "1234321"
string_3 = "1234567"


def is_palindrome(string: str) -> bool:
    return (string == string[::-1])


print(is_palindrome(string_1))
print(is_palindrome(string_2))
print(is_palindrome(string_3))

# ouput
# True
# True
# False
