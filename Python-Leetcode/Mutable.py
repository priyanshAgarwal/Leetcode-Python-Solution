# cook your dish here

"""
Mutable List
"""


def is_primme(number)->list:
    num1 = []
    num2 = []
    
    arr_value=[0,0]
    x,y = 0,0
    for i in range(number):
        arr_value[0]+=i
        arr_value[1]+=i
        x=x+i
        y=y+i
        num1.append((arr_value))
        num2.append([x,y])
        print(num1)

    return num1
            

     


print(is_primme(15))