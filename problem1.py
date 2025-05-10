#check if a number is divided by 7
def divided():
    n=int(input("enter the number of n"))
    for i in range(n):
        if i%7==0:
            print("the value",i)
            
divided()