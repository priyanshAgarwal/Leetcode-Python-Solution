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
