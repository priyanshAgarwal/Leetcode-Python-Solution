# cook your dish here

"""

"""

ages = {
    'Matt': 30,
    'Katie': 29,
    'Nik': 31,
    'Jack': 43,
    'Jill': 43,
    'Alison': 32,
    'Kevin': 38
}
max_keys = [key for key, value in ages.items() if value == max(ages.values())]
print(max_keys)
