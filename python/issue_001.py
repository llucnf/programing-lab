
i=0
while i>=0:
    print("Introduzca su nombre")
    uName=  input()
    print("Introduzca su edad")
    uAge=  int(input())
    uAgeToDays= uAge * 365
    if uAgeToDays>=11315 :
        print("Que viejo...Zombie")
    else :
        i +=1
        break
print(f"Hello {uName}")
print(f"You are {uAge} years old")
print("Welcome to Programing Lab")