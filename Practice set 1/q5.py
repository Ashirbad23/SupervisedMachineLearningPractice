days = {0:"Sunday",
        1:"Monday", 
        2:"Teusday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday"}
print(days)
a = int(input("Enter today's day: "))
b = int(input("Enter number of days elapsed since today: "))
if(a+b > 6):
    exit()
print(f"Today is {days[a]} and the future day is {days[a+b]}")