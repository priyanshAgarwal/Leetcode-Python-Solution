# cook your dish here

"""

"""

s='122231.67'
# s='1111111'
# print(compressString(s=s))

def largestNumber(s:str)->int:

	if isinstance(s,str)==True and s.isdigit()==True:
		# s=int(s)
		s=sorted(s,reverse=True)
	else:
		return -1

	return "".join(s)

print(largestNumber(s))

books = {
    "To Kill a Mockingbird": ["Classics", "Historical"],
    "1984": ["Classics", "Dystopia"],
    "Harry Potter and the Philosopher's Stone": ["Fantasy", "Adventure"],
    "The Great Gatsby": ["Classics", "Fiction"],
    "The Hobbit": ["Fantasy", "Adventure"],
    "Pride and Prejudice": ["Classics", "Romance"],
    "The Catcher in the Rye": ["Classics", "Young Adult"],
}
