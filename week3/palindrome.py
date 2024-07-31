def palindrome(string):
    return string == string[::-1]:

string = input("Enter the string: ")
if palindrome(string):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
