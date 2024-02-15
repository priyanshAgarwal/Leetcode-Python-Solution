# cook your dish here

"""

"""
s ="]"

array_para=[]

dict_para ={
    '(':')',
    '{':'}',
    '[':']'
}


for bracket in s:
    if bracket in dict_para.keys():
        array_para.append(bracket)
    elif dict_para.get(array_para.pop())==bracket:
        array_para.pop()

