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
    except requests.RequestException as e:
        print(f"Error fetching TODO data: {e}")
        sys.exit(1)


def export_to_json_all_employees(emp_data):
    '''
     Exports task data for all employees to a JSON file.
     '''
    data = {}
    for emp_id, emp_name in emp_data.items():
        tasks = fetch_todo_data(emp_id)
        task_list = []

        for task in tasks:
            task_data = {
                    "username": emp_name,
                    "task": task['title'],
                    "completed": task['completed']
                    }
            task_list.append(task_data)

            data[emp_id] = task_list

            file_name = "todo_all_employees.json"
            with open(file_name, 'w') as file:
                json.dump(data, file)


def fetch_all_employees_data():
    '''
    Fetches data for all employees from a specified URL.
    '''
    base_url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(base_url)
        employees_data = {user['id']: user['username'] for user in
                          response.json()}
        return employees_data
    except requests.RequestException as e:
        print(f"Error fetching all employees data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    ''' Entry point '''
    all_employees_data = fetch_all_employees_data()
    export_to_json_all_employees(all_employees_data)
