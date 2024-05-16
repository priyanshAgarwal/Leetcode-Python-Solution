# cook your dish here

"""

"""

def findMaxAttendee(meetings):
    meetings = sorted(meetings, key=lambda x:x['start_time'])
    maxAttendee = 0
    right = 1
    for meeting in meetings:
        totalAttendee = meeting['attendees']
        while right<len(meetings) and meetings[right]['start_time']<meeting['end_time']:
            totalAttendee+=meetings[right]['attendees']
            right+=1
            maxAttendee = max(maxAttendee,totalAttendee)
    return maxAttendee






# Example data (replace with your actual data)
# meetings_data = [
#     {'start_time':'2024-05-10 01:00','end_time':'2024-05-10 05:00','attendees':10},
#     {'start_time':'2024-05-10 03:00','end_time':'2024-05-10 06:00','attendees':20},
#     {'start_time':'2024-05-10 05:00','end_time':'2024-05-10 09:00','attendees':30},
#     {'start_time':'2024-05-10 19:31','end_time':'2024-05-16 02:31','attendees':39}, 
#     {'start_time':'2024-05-10 00:56','end_time':'2024-05-15 06:56','attendees':38}, 
#     {'start_time':'2024-05-10 01:17','end_time':'2024-05-15 03:17','attendees':26}, 
#     {'start_time':'2024-05-10 01:23','end_time':'2024-05-15 06:23','attendees':14}, 
#     {'start_time':'2024-05-10 03:43','end_time':'2024-05-15 11:43','attendees':25}
# ]

# max_attendees = findMaxAttendee(meetings_data)
# print(f"Maximum attendees in any overlapping meeting: {max_attendees}")

def reverseParentheses(s: str) -> str:
    result = []
    reverse = []

    for i in s:

        if i == ')':
            while result[-1]!='(':
                reverse.append(result.pop())
            result.pop()
            result.extend(reverse)
            reverse=[]
        else:
            result.append(i)
            
    return "".join(result)

s = "(u(love)i)"

# print(reverseParentheses(s=s))

