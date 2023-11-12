import json

# Employees JSON
with open("employees_info.json", 'r') as f:
    employees_dict = json.load(f)

print(employees_dict["1"])