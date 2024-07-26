def palindrome(data):
    return data == data[::-1]


print(palindrome("level"))  # True
print(palindrome("madaa"))  # False