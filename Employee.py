from tabulate import tabulate #require install: go to command write "pip install tabulate"

Employees = []

hour = 0
salary = 0
ot_rate = 0
ot_hour = 0
ot_salary = 0
bonus = 0
depreciation = 0

def getValid_hour_input():
    while True:
        try:
            hour = float(input("Enter Hour: "))
            return hour
        except ValueError:
            print("Please input freaking hour as number you idiot!!")

def get_valid_input(get_valid):
    while True:
        try:
            x = float(input(f"Eneter {get_valid}: "))
            return x
        except ValueError:
            print("Please input freaking salary as number you idiot!!")

n = int(input("Enter number of employee: "))

for i in range(n):
    id = input("Enter Id: ")
    name = input("Enter Name: ")
    gender = input("Enter Gender: ")
    hour = getValid_hour_input()
    if hour >= 170:
        salary = get_valid_input("Salary")
        bonus = get_valid_input("Bonus")
        ot_hour = hour - 170
        ot_rate = get_valid_input("Rate")
        ot_salary = ot_hour * ot_rate
        salary_in_month = salary + ot_salary + bonus
    elif 160 <= hour <= 170:
        salary = get_valid_input("Salary")
        salary_in_month = salary
    elif hour < 160:
        salary = get_valid_input("Salary")
        depreciation = get_valid_input("Depreciation")
        salary_in_month = salary - depreciation
    
    Employee = {
        "Id": id, "Name": name, "Gender": gender, "Hour": hour,"Salary": salary, "Bonus": bonus,
        "Depreciation": depreciation, "OT_Hour": ot_hour, 
        "OT_Rate": ot_rate, "OT_Salary": ot_salary, "Salary_In_Month": salary_in_month
    }
    Employees.append(Employee)
    
table = []
headers = ["Id", "Name", "Gender", "Hour", "Salary", "Bonus", "Depreciation", "OT Hour", 
           "OT Rate", "OT Salary", "Salary in month"]    

for Employee in Employees:
    row = [
        Employee["Id"],
        Employee["Name"],
        Employee["Gender"],
        Employee["Hour"],
        Employee["Salary"],
        Employee["Bonus"],
        Employee["Depreciation"],
        Employee["OT_Hour"],
        Employee["OT_Rate"],
        Employee["OT_Salary"],
        Employee["Salary_In_Month"]
    ]
    table.append(row)
print(tabulate(table, headers = headers, tablefmt = "grid"))
