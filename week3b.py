#menu 1. Add Student 2. View Students 3. Exit
#int(input("Enter your choice: "))
#input("Enter student name: ")
#input("Enter student score: ")
#when finished 
#print("Student has been added.")

#When choice 2 selected print student data
#when choice 3 selected
#print("Data saved. Thank you, have a great day!")

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 65:
        return "D"
    else:
        return "F"

def load_students():
    students = []
    try:
        with open("students.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                name = parts[0]
                score = int(parts[1])
                grade = parts[2]
                students.append({"name": name, "score": score, "grade": grade})
    except:
        students = []
    return students

def save_students(students):
    with open("students.txt", "w") as f:
        for student in students:
            f.write(f"{student['name']},{student['score']},{student['grade']}\n")

students = load_students()

while True:
    print("\n--- Menu ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Remove Student")
    print("4. Exit")
    choice = input("Select an option: ").strip()
    print("------------------------")
    print()

    if choice == "1":
        added_count = 0
        while True:
            name = input("Enter student name: ")
            score = int(input("Enter student score: "))
            print()
            grade = get_grade(score)
            students.append({"name": name, "score": score, "grade": grade})
            added_count = added_count + 1
            another = input("Add another student? (yes/no): ").strip().lower()
            if another == "yes":
                print("--")
            if another != "yes":
                break
        print("---------------------------")
        print(f"{added_count} student(s) added.")

    elif choice == "2":
        if len(students) == 0:
            print("No students on record.")
        else:
            print("\nStudent Records")
            print("---------------------------")
            for student in students:
                result = "Pass" if student["score"] >= 65 else "Fail"
                print(f"{student['name']} - {student['score']} {student['grade']} - {result}")

    elif choice == "3":
        if len(students) == 0:
            print("No students on record.")
        else:
            print("\nStudent Records")
            print("---------------------------")
            for i, student in enumerate(students):
                print(f"{i + 1}. {student['name']}: {student['score']} {student['grade']}")
            print()
            remove_choice = int(input("Enter the number of the student to remove: "))
            if 1 <= remove_choice <= len(students):
                removed = students.pop(remove_choice - 1)
                print(f"\n{removed['name']} has been removed.")
            else:
                print("Invalid number, please try again.")

    elif choice == "4":
        save_students(students)
        print("Data saved. Thank you, have a great day!")
        break

    else:
        print("Invalid option, please select 1, 2, 3, or 4.")