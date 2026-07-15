def is_valid_login(username, password):
    return len(username) >= 4 and len(password)>=8
         
    

username = input("Enter username: ")
password = input("Enter password: ")

if is_valid_login(username, password):
    print("Login accepted.")
else:
     print("Login rejected")