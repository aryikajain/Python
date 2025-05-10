# WAP to check if a number is armstrong number or not
# WAP to check if a number is a perfect square or not
# WAP to check if a number is digit palindrome or not
# WAP to find factorial of a given number
n=int(input("enter the value"))
temp=n
count=0
while temp>0:
    count+=1
    temp=temp//10
temp=n
sum_of_power = 0

while temp>0:
    digit = temp%10
    sum_of_power += digit**count
    temp= temp//10

if sum_of_power == n:
    print(n, "is an Armstrong number.")
else:
    print(n, "is not an Armstrong number.")

