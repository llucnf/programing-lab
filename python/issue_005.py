
value= int(input("Introduzca un número:")) 
def is_even(value): 
    if value%2:
        
        return False
    else:
        return True

if is_even(value):
    print("The number is even.")
else:
    print("The number is odd.")