#!/usr/bin/python3
''' Python script '''
import csv
import requests
import sys


def fetch_user_data(emp_id):
    '''
    Fetches user data for a given employee ID from the JSONPlaceholder API.
    '''
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = f"{base_url}/{emp_id}"

    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()
        return user_data
    except requests.RequestException as e:
        print(f"Error fetching user data: {e}")
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


def export_to_csv(emp_id, emp_name, tasks):
    '''
    Exports task data to a CSV file for a specific employee.
    '''
    file_name = f"{emp_id}.csv"

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([emp_id, emp_name, str(task['completed']),
                             task['title']])


def display_todo_progress(emp_id):
    '''
    Fetches user data and TODO list data for a given employee ID,
    then exports the TODO list data to a CSV file.
    '''
    user_data = fetch_user_data(emp_id)
    todos_data = fetch_todo_data(emp_id)

    emp_name = user_data['name']
    tasks = todos_data

    export_to_csv(emp_id, emp_name, tasks)


if __name__ == "__main__":
    ''' Program entry point '''
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    emp_id = sys.argv[1]
    display_todo_progress(emp_id)
