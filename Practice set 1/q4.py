age1 = int(input("Enter your age Rahul: "))
age2 = int(input("Enter your age Ayush: "))
age3 = int(input("Enter your age Ajay: "))

if(age1>age2):
    if(age1>age3):
        print("Rahul")
    else:
        print("Ajay")
else:
    if(age2>age3):
        print("Ayush")
    else: 
        print("Ajay")