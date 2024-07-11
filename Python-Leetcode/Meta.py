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


# cook your dish here

"""

"""

import heapq

def find_max_attendees(meetings):
    # Sort meetings by start time
    sorted_meetings = sorted(meetings, key=lambda x: x[0])

    # Initialize a min heap to track end times of active meetings
    active_end_times = []

    # Initialize the maximum attendee count
    max_attendees = 0

    for meeting in sorted_meetings:
        start_time, end_time, attendees = meeting

        # Remove meetings that have ended (end time <= current meeting start time)
        while active_end_times and active_end_times[0] <= start_time:
            heapq.heappop(active_end_times)

        # Add the current meeting's end time to active_end_times
        heapq.heappush(active_end_times, end_time)

        # Calculate the total attendees in active meetings
        total_attendees = len(active_end_times) * attendees

        # Update the maximum attendee count
        max_attendees = max(max_attendees, total_attendees)

    return max_attendees

# Example data (replace with your actual data)
meetings_data = [
    ('2024-05-10 01:00', '2024-05-10 05:00', 10),
    ('2024-05-10 03:00', '2024-05-10 06:00', 20),
    # Add more meetings...
]

max_attendees = find_max_attendees(meetings_data)
print(max_attendees)
