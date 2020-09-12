s = input("Please enter a string: ")
z = s[::-1]  #把输入的字符串s 进行倒序处理形成新的字符串z
if s == z:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")