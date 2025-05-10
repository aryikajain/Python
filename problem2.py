#check weather the number are odd 
def evenorodd():
    n=int(input("enter the number"))
    for i in range(n):
        if i%2==0:
            print(i,"its even")
        else:
            print(i,"its odd")
evenorodd()