grades = { "Joe": [100, 0],
           "Dan": [100, 95]
          }

while True:
    user_input_1 = input("Enter action (add_student / add_grade / remove_student / report / quit): ").strip()

    if user_input_1 == "add_student":                   # adds a student to grades dictionary
        name = input("Enter Student name: ").strip()    #.strip() removes spaces at beginning and end of input NOT middle
        grades[name] = []

    elif user_input_1 == "add_grade":                   #adds grade to student ALREADY in dictionary
        name = input("Enter Student name: ").strip()
        grade = int(input("Enter Student grade: "))
        if name in grades:
            grades[name].append(grade)
        else:
            print("No Student with that name")

    elif user_input_1 == "remove_student":              # Removes a student from grades
         name = input("Enter Student name: ").strip()
         grades.pop(name, None)                         # Why couldnt't grades.pop(name) work?

    elif user_input_1 == "report":
        for student, scores in grades.items():                              # can loop through keys and values with .items()
            report_card = sum(scores) / len(scores)
            print(f"{student}: {report_card}")

    elif user_input_1 == "quit":
        break

    else:
        print("Incorrect Command...")


