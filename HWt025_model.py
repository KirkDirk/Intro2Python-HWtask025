import csv
import json
from pathlib import Path

def read_csv() -> list:
    employees = []
    with open('HWtask025\database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp["id"] = int(row[0])
            temp["last_name"] = row[1]
            temp["first_name"] = row[2]
            temp["position"] = row[3]
            temp["phone_number"] = row[4]
            temp["salary"] = float(row[5])
            employees.append(temp)
    return employees

def get_key(key):
    list_key = ["id", "last_name", "first_name", "position", "phone_number", "salary"]
    return list_key[key]

def find_employee(employees, key, search_data):
    for employee in employees:
        if search_data in employee[key]:
            return employee

# def read_json() -> list:
#     employee = []
#     with open(Path.cwd() / 'database02.json', 'r', encoding='utf-8') as fin:
#         for line in fin:
#             temp = json.loads(line.strip())
#             employee.append(temp)
#     return employee

def write_csv(employees: list):
    with open(Path.cwd() / 'database.csv', 'w', encoding='utf-8') as fout:
        csv_writer = csv.writer(fout)
        for employee in employees:
            csv_writer.writerow(employee.values())

def write_json(employees: list):
    with open(Path.cwd() / 'database02.json', 'w', encoding='utf-8') as fout:
        for employee in employees:
            fout.write(json.dumps(employee) + '\n')


