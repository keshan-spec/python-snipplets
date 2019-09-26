import json

students = []


def add_dict(**value):
    global students
    student = {}

    for key, val in value.items():
        student[key] = val
    students.append(student)


for _ in range(2):
    sub_list = {}

    name = input('Enter name : ')
    age = int(input('Enter age : '))
    for _ in range(int(input('Enter subject count : '))):
        a = input('Enter (subject name) (marks) : ').split()
        if len(a) == 2:
            sub_list[a[0]] = int(a[-1])
        elif len(a) > 2:
            sub_list[' '.join(a[0:(len(a)-1)])] = int(a[-1])

    add_dict(Name=name, Age=age, Subjects=sub_list)

print(json.dumps(students, indent=2))
