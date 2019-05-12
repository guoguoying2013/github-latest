import sys
import json
import requests
from datetime import datetime

# Use Like python githubber.py JASchilz


def list_of_events(user_name):
    """
    it returned a list of events that this user_name has done.
    """
    address='https://api.github.com/users/{}/events'.format(user_name)
    response = requests.get(address)
    return response.json()

def time_stampe_of_the_first_event(user_name):
    """
    Print out the time stamp associated with the first event in event list
    """
    lst_events = list_of_events(user_name)
    first_event = lst_events[0]
    time_string = first_event['created_at']
    datetime_object = datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%SZ")
    timestamp = datetime.timestamp(datetime_object)
    return timestamp

if __name__ == "__main__":
    username = sys.argv[1]
    # 1. Retrieve a list of "events" associated with the given user name
    print(f"this is the list of events done by user {username}")
    lst = list_of_events(username)
    for i in lst:
        print(i['type'])
    # 2. Print out the time stamp associated with the first event in that list.
    print("the time stamp associated with the first event in that list is below:")
    print(time_stampe_of_the_first_event(username))



