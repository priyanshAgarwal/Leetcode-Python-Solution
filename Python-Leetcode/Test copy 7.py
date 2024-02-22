import random
import string

length=12

letters = string.ascii_lowercase 
result_str = ''.join(random.choice(letters) for i in range(length))

aa=''

for i in range(length):
    aa+=random.choice(letters)

print(aa)