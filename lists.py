# List Examples
# functions: https://www.w3schools.com/python/python_ref_list.asp

students = ["Matthew Poon", "Matthew Ji"]


def print_students():
    print("\nStudents:", students, "\n")


def register_student(name):
    if students.count(name) != 0:
        print(name, "is already registered in school btw")
        students.append(name)
    else:
        students.append(name)
        print(name, "is successfully registered")


def expell_student(name):
    students.remove(name)
    print("Expelled", name)


def main():
    print_students()

    print("Second Student to be enrolled is:", students[1], "\n")

    register_student("Matthew Ho")
    register_student("Matthew Law")
    register_student("Matthew Poon")

    print_students()

    expell_student("Matthew Ji")

    print_students()


main()
