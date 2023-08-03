def is_palindrome(string):
    return string==string[::-1]
txt = input("enter a sequence to check:")
if is_palindrome(txt):
    print(txt,"is a PALINDROME sequence")
else:
    print("it is NOT A PALINDROME sequence")