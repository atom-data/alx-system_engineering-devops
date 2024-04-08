#!/usr/bin/python3
"""
Export employee todo data to json
"""

if __name__ == "__main__":
    import json
    import requests

    url = "https://jsonplaceholder.typicode.com/"
    users_url = url + "users"

    # json output
    def response_json(input_url):
        try:
            input_response = requests.get(input_url, verify=False)
            input_response.raise_for_status()
            return input_response.json()
        except requests.exceptions.RequestException as e:
            print(e)

    # users information
    users_data = response_json(users_url)

    employee_todo_json = dict()
    for user in users_data:
        user_id = user.get("id")
        user_name = user.get("username")
        # todos information
        todos_url = url + "todos?userId={}".format(user_id)
        todos_data = response_json(todos_url)
        employee_todo_json[user_id] = list()
        for todo in todos_data:
            task = todo.get("title")
            completed = todo.get("completed")
            data = {"username": user_name,
                    "task": task, "completed": completed}
            employee_todo_json.get(user_id).append(data)

    with open("todo_all_employees.json", 'w') as f:
        json.dump(employee_todo_json, f)
