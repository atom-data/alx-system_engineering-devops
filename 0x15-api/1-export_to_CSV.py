#!/usr/bin/python3
"""
Export todo list info to csv
"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    if len(sys.argv) < 2:
        exit()
    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        exit()
    url = "https://jsonplaceholder.typicode.com/"
    users_url = url + "users?id={}".format(user_id)
    todos_url = url + "todos?userId={}".format(user_id)

    # json output
    def response_json(input_url):
        try:
            input_response = requests.get(input_url, verify=False)
            input_response.raise_for_status()
            return input_response.json()
        except requests.exceptions.RequestException as e:
            print(e)
        except IndexError:
            print("Error: No employee found with ID {}".format(
                user_id))

    # Get employee details
    employee_details = response_json(users_url)
    user_name = employee_details[0].get('username')

    # employee todo tasks
    todos_details = response_json(todos_url)

    # combine the data
    combined_data = []
    for todos_data in todos_details:
        combined_entry = {"userName": user_name}
        combined_entry.update(todos_data)
        combined_data.append(combined_entry)

    # csv file name
    csv_file = "{}.csv".format(user_id)

    # write csv
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for line in combined_data:
            writer.writerow([line.get("userId"), line.get(
                "userName"), line.get("completed"), line.get("title")])
