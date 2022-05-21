# cook your dish here

"""

"""

num = -5

if num > 1:
    for i in range(2, num, 1):
        if num % i == 0:
            print(f"{num} is not prime, {num} is divisible by {i} and output is {num/i}")
            break
    else:
        print(f"{num} is a prime number")
else: print(f"{num} is not a prime number")
