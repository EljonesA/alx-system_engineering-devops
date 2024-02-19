#!/usr/bin/python3
''' Python script '''
import json
import requests
import sys


def fetch_emp_data(emp_id):
    '''
    Fetches user data for a given employee ID from the JSONPlaceholder API.
    '''
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = f'{base_url}/{emp_id}'

    try:
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
    except requests.RequestExcept as e:
        print(f"Error fetching TODO data: {e}")
        sys.exit(1)


def export_to_json(emp_id, emp_name, tasks):
    '''
    Exports task data to a JSON file for a specific employee.
    '''
    data = {emp_id: []}
    for task in tasks:
        task_data = {
                "task": task['title'],
                "completed": task['completed'],
                "username": emp_name
                }
        data[emp_id].append(task_data)

        file_name = f"{emp_id}.json"
        with open(file_name, 'w') as file:
            json.dump(data, file)


def display_todo_progress(emp_id):
    '''
    Fetches user data and TODO list data for a given employee ID,
    then exports the TODO list data to a JSON file.
    '''
    user_data = fetch_emp_data(emp_id)
    todos_data = fetch_todo_data(emp_id)

    emp_name = user_data['username']
    tasks = todos_data

    export_to_json(emp_id, emp_name, tasks)


if __name__ == "__main__":
    ''' Entry point '''
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    emp_id = sys.argv[1]
    display_todo_progress(emp_id)
