# WAP to generate sereis 2, 5, 10, 17 .... nth
# WAP to generate prime series between 1 and 100
for num in range(1, 101):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
