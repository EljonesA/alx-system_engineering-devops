#!/usr/bin/python3
''' script using the JSON dummy API, for a given employee ID,
    returns information about his/her TODO list progress.
'''
import requests
import sys


def fetch_emp_data(emp_id):
    '''
         Fetches user data for a given employee ID from the
         JSONPlaceholder API.
         Args:
             emp_id: ID of employee whose data is to be rretrieved
         Returns: user data as a dictionary
    '''
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = f'{base_url}/{emp_id}'

    try:
        # fetch user data from API
        user_response = requests.get(user_url)
        user_data = user_response.json()
        return user_data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)


def fetch_todo_data(emp_id):
    '''
    Fetches TODO list data for a given employee ID from the
    JSONPlaceholder API.
    '''
    base_url = "https://jsonplaceholder.typicode.com/todos"
    todos_url = f"{base_url}?userId={emp_id}"

    try:
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()
        return todos_data
    except requests.RequestException as e:
        print(f"Error fetching TODO data: {e}")
        sys.exit(1)


def display_todo_progress(emp_id):
    '''
     Displays the progress of TODO list for a given employee ID.
    '''
    user_data = fetch_emp_data(emp_id)
    todos_data = fetch_todo_data(emp_id)

    emp_name = user_data['name']
    completed_tasks = [task for task in todos_data if task['completed']]
    total_tasks = todos_data

    print(f"Employee {emp_name} is done with tasks "
          f"({len(completed_tasks)}/{len(total_tasks)}):")

    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    ''' Program entry point '''
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    emp_id = sys.argv[1]
    display_todo_progress(emp_id)
