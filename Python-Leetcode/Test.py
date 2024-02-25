# cook your dish here

"""

"""

a=[2,4,3,5,2,6,3] 


num_dict=dict()


for i in range(0,len(a)):
    num_dict[a[i]]=num_dict.get(a[i],0)+1 


max_key = max(num_dict, key=num_dict.get)

result=[]
for key, value in num_dict.items():
    if value==max_key:
        result.append(key)

print(result)