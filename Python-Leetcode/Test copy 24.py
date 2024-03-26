# cook your dish here

"""

"""


def is_primme(num):
    
    for i in range(2,num):
        if num%i==0:
            return False

    return True 


print(is_primme(7))