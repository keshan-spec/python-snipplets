student = {}
sub_list = {}


def add_dict(**value):
    global student

    for key, val in value.items():
        student[key] = val


name = input('Enter name : ')
age = int(input('Enter age : '))
for _ in range(int(input('Enter subject count : '))):
    a = input('Enter (subject name) (marks) : ').split()
    if len(a) == 2:
        sub_list[a[0]] = int(a[-1])
    elif len(a) > 2:
        sub_list[' '.join(a[0:(len(a)-1)])] = int(a[-1])

add_dict(name=name, age=age, subject=sub_list)

print(f'Dictionary made : {student}')
