# aabbcd -> abcba
# abb -> bab
# aabb -> abba
# abc -> a

# input
string_1 = "aabbcd"
string_2 = "abb"
string_3 = "aabb"
string_4 = "abc"


def smallest_palindrome(string: str) -> str:

    pairs = sorted([char for char in set(string) if string.count(char) >= 2])[::-1]
    ones = [char for char in set(string) if string.count(char) % 2 != 0]
    center = min(ones) if len(ones) else ""
    result = center

    for pair_char in pairs:
        for _ in range(string.count(pair_char) // 2):
            result = pair_char + result + pair_char

    return result


print(smallest_palindrome(string_1))
print(smallest_palindrome(string_2))
print(smallest_palindrome(string_3))
print(smallest_palindrome(string_4))

# output
# abcba
# bab
# abba
# a
