sp = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ':', ';', "'", '"', '<', '>', ',', '.', '?', '/']
caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("******YOUR PASSWORD MUST CONTAIN AT LEAST ONE SPECIAL CHARACTER, ONE NUMBER, ONE UPPER CASE LETTER, AND ONE LOWER CASE LETTER*******\n")

password = input('Enter your password: ')

special_char = any(char in sp for char in password)
upper_case = any(char in caps for char in password)
lower_case = any(char in small for char in password)
number = any(char in nums for char in password)

if special_char and upper_case and lower_case and number:
    print("Your password is strong!")
    print("Your password is 100% stronger.")
elif special_char and upper_case and lower_case:
    print("Your password is stronger!")
    print("Your password is 75% stronger.")
elif special_char and upper_case and number:
    print("Your password is stronger!")
    print("Your password is 75% stronger.")
elif special_char and lower_case and number:
    print("Your password is stronger!")
    print("Your password is 75% stronger.")
elif upper_case and lower_case and number:
    print("Your password is stronger!")
    print("Your password is 75% stronger.")
elif special_char and upper_case:
    print("Your password is weak!")
    print("Your password is 50% stronger.")
elif special_char and lower_case:
    print("Your password is weak!")
    print("Your password is 50% stronger.")
elif special_char and number:
    print("Your password is weak!")
    print("Your password is 50% stronger.")
elif upper_case and lower_case:
    print("Your password is weak!")
    print("Your password is 50% stronger.")
elif upper_case and number:
    print("Your password is weak!")
    print("Your password is 50% stronger.")
elif lower_case and number:
    print("Your password is weak!")
    print("Your password is 50% stronger.")
else:
    print("Your password is weak! Please include special characters, numbers, upper case, and lower case letters.")


