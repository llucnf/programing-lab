user_num = int(input("Enter a number: "))

if user_num == 0:
    print("The number is zero.")
elif user_num > 0:
    print(f"{user_num} is positive.")
else:
    print(f"{user_num} is negative.")