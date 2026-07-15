

def is_valid_password(password):
    if len(password)>=8 :
        return True
    else: 
        return False

passWord= input("Introduzca una contraseña")

if is_valid_password(passWord):
    print("Password accepted")
else:
    print("Password rejected.")