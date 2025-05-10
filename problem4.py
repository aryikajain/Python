# WAP to generate even numbers till the nth number

def evenno():
    n=int(input("enter the number"))
    for i in range(n):
        if i%2==0:
            print(i)
evenno()