# write your code here
def palindrome(string):
    return string == string[::-1]


print(palindrome("radar"))
print(palindrome("car"))
print(palindrome("tenacious"))
print(palindrome("sas sas"))