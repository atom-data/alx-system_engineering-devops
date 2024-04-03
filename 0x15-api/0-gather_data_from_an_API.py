#!/usr/bin/python3

"""
Find an employee's todo list progress
"""

if __name__ == "__main__":
        import requests
        import sys

        if len(sys.argv) < 2:
                exit()
        try:
                employee_id = int(sys.argv[1])
        except ValueError:
                print("Employee ID must be an integer.")
                exit()
        url = "https://jsonplaceholder.typicode.com/"
        users_url = url + "users?id={}".format(employee_id)
        todos_url = url + "todos?userId={}".format(employee_id)
        completed_url = todos_url + "&completed=true"

        # json output
        def response_json(input_url):
                try:
                        input_response = requests.get(input_url, verify=False)
                        input_response.raise_for_status()
                        return input_response.json()
                except requests.exceptions.RequestException as e:
                        print(e)

        # Get employee's details
        employee_details = response_json(users_url)
        employee_name = employee_details[0].get('name')

        # Total number of tasks todo
        todos_detail = response_json(todos_url)
        total_tasks_done = len(todos_detail)

        # Number of tasks done
        completed_tasks = response_json(completed_url)
        total_completed_tasks = len(completed_tasks)

        print("Employee {} is done with tasks ({}/{})".format(
            employee_name,
            total_completed_tasks,
            total_tasks_done))
        for task in completed_tasks:
            print("\t {}".format(task.get('title')))
