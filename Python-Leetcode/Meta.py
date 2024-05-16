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
    "The Night Circus": ["Fantasy", "Romance", "Historical"],
    "The Martian": ["Science Fiction", "Adventure"],
    "Educated": ["Memoir", "Biography"],
    "Circe": ["Fantasy", "Mythology"],
    "Where the Crawdads Sing": ["Mystery", "Romance"],
    "The Goldfinch": ["Fiction", "Drama"],
    "Becoming": ["Memoir", "Autobiography"],
    "Little Fires Everywhere": ["Fiction", "Family Drama"],
    "The Silent Patient": ["Thriller", "Psychological"],
    "Normal People": ["Fiction", "Romance"],
}

# print(type(books))

def mostPopular(books:list)->str:
	
    popular_dict = {}
    for _, genres in books.items():
	    for genre in genres:
		    popular_dict[genre]=popular_dict.get(genre,0)+1
    unique_numbers = sorted(set(popular_dict.values()))
    
    # print(unique_numbers)
    # popular_dict=sorted(popular_dict.items(), key= lambda x:x[1], reverse=True)
    """
    [('Classics', 5), ('Fantasy', 2), ('Adventure', 2), ('Historical', 1), ('Dystopia', 1), ('Fiction', 1), ('Romance', 1), ('Young Adult', 1)]
    """	
    if len(unique_numbers)>1:
        max_element = unique_numbers[-1]

    result = []

    for key, value in popular_dict.items():
        if value==max_element:
            result.append(key)


    # print(type(popular_dict[0]))
	# print(sorted(popular_dict, key=popular_dict.get)[-2])


    return result

	    
print(mostPopular(books))		


# Eg. "I am back." should become "i1 2a2m1b1c1k1.1"

def compressString(s:str)->str:
	s=s.lower()
	word_dict = {}
	for word in s:
		leter = word.lower()
		word_dict[leter]=word_dict.get(leter,0)+1
	result = ''
	for word in s:
		if word not in result:
			value=word_dict.get(word)
			result+=word
			result+=str(value)
	return result
s="I am back." 
# print(compressString(s))


def generate_substrings(s):
    substrings = []
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            substrings.append(s[i:j])
    return substrings

# Test the function
s = "hello"
# print(generate_substrings(s))  # Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']


# 