# 44) Palindrome numbers

original_number = int(input("Enter the number here: "))
n = original_number
reversed_num = 0
while original_number > 0:
    digit = original_number % 10
    reversed_num = reversed_num * 10 + digit
    original_number = original_number // 10
if n == reversed_num:
    print("The num is palindrome number.")
else:
    print("The num is not a palindrome number.")