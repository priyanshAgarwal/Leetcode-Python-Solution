# cook your dish here

"""
Prime Number
"""

def check_prime(n):
    if_prime=True
    for i in range(2,n):
        if n%i==0:
            if_prime=False
            break
    return if_prime

print(check_prime(243535317))