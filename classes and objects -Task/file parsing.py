import csv
def parse_csv_to_dict(filename):
    student_dict = {}
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)  
        for row in reader:
            student_dict[row['id']] = {
                "name": row['name'],
                "class": row['class'],
                "dob": row['dob']
            }
    return student_dict

students = parse_csv_to_dict("students.csv")
print(students)
