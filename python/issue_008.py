

def check_guess(secret_number, guess):

        if guess > secret_number:
           return "lower"
           
        elif guess < secret_number :
            return "higher"
        else:
            return "correct"
    
                             
secret_number= 16            
is_correct= False

while not is_correct :
    guess= int(input("Enter a number: "))
    result= check_guess(secret_number,guess)
    print(result)
    if result == "correct":
        is_correct = True
