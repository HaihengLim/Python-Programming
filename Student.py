from tabulate import tabulate # it require to instal: go to command and type "pip install tabulate
students = []

n = int(input("Enter number of student: "))

for i in range(n):
    id = input("Enter Id: ")
    name = input("Enter Name: ")
    gender = input("Enter Gender: ")
    def get_Valid_input(subject):
        while True:
            try:
                score = float(input(f"Enter {subject} score: "))
                if 0 <= score <= 100:
                    return score
                else:
                    print("input score between 0 to 100!")
            except ValueError:
                print("score have to input as number!!, try again!!")
            
    ca = get_Valid_input("Computer Architecture")
    dc = get_Valid_input("Data Communication")
    ds = get_Valid_input("Data Structure")
    
    totalScore = ca + dc + ds
    avg = totalScore / 3
    if avg >= 90:
        grade = 'A'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade = 'D'
    elif avg >= 50:
        grade = 'E'
    else:
        grade = 'F'
        
    student = {
        "Id": id, "Name": name, "Gender": gender, "CA": ca, "DC": dc, "DS": ds,
            "TotalScore": totalScore, "Average": avg, "Grade": grade
    }
    students.append(student)
  
table = []  
headers = [
    "Id", "Name", "Gender", "Computer Architecture", "Data Communication",
        "Data Structure", "Total Score", "Average", "Grade"
]
    
for student in students:
    row = [
        student['Id'],
        student['Name'],
        student['Gender'],
        student['CA'],
        student['DC'],
        student['DS'],
        student['TotalScore'],
        student['Average'],
        student['Grade']
    ]
    table.append(row)
print(tabulate(table, headers = headers, tablefmt = "grid"))
