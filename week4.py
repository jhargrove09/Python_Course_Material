
# grade calc
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

# load student
def load_students():
    students = []
    try:
        with open("wk4students.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                students.append({"name": parts[0], "score": int(parts[1]), "grade": parts[2]})
    except:
        students = []
    return students

# save student
def save_students(students):
    with open("wk4students.txt", "w") as f:
        for student in students:
            f.write(f"{student['name']},{student['score']},{student['grade']}\n")

# check dup names
def is_duplicate(students, name):
    for student in students:
        if student["name"].lower() == name.lower():
            return True
    return False

# add students
def add_student(students):
    added_count = 0
    while True:
        name = input("Enter student name: ")

        if is_duplicate(students, name):
            print(f"\n{name} is already active in this system. Please view by selecting #2 from the main menu.")
            print()
        else:
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

    if added_count > 0:
        print("---------------------------")
        print(f"{added_count} student(s) added.")

# view students
def view_students(students):
    if len(students) == 0:
        print("No students on record.")
    else:
        print("\nStudent Records")
        print("---------------------------")
        for student in students:
            result = "Pass" if student["score"] >= 65 else "Fail"
            print(f"{student['name']}: {student['score']} {student['grade']} - {result}")

# remove student
def remove_student(students):
    if len(students) == 0:
        print("No students on record.")
    else:
        while True:
            # print numbered list of students with exit option at bottom
            print("\nStudent Records")
            print("---------------------------")
            for i, student in enumerate(students):
                print(f"{i + 1}. {student['name']}: {student['score']} {student['grade']}")
            print(f"{len(students) + 1}. Exit to menu")
            print()

            remove_choice = int(input("Enter the number of the student to remove: "))

            # exit to menu option
            if remove_choice == len(students) + 1:
                break

            if 1 <= remove_choice <= len(students):
                removed = students.pop(remove_choice - 1)
                print(f"\n{removed['name']} has been removed.")
            else:
                print("Invalid number, please try again.")
                continue

            # if no students left, exit automatically
            if len(students) == 0:
                print("All students have been removed.")
                break

            # prompt after removal
            print("-----------------------------")
            print()
            print("Choose one below:")
            print("\n1. Remove another student")
            print("2. Remove all students")
            print("3. Go back to main menu")
            follow_up = input("Select an option: ").strip()

            if follow_up == "1":
                continue
            elif follow_up == "2":
                students.clear()
                print("All students have been removed.")
                break
            else:
                break

# Menu
def display_menu():
    print("\n--- Menu ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Remove Student")
    print("4. Exit")

# Main Program
students = load_students()

while True:
    display_menu()
    choice = input("Select an option: ").strip()
    print("------------------------")
    print()

    if choice == "1":
        add_student(students)
    elif choice == "2":
        view_students(students)
    elif choice == "3":
        remove_student(students)
    elif choice == "4":
        save_students(students)
        print("Data saved. Thank you, have a great day!")
        break
    else:
        print("Invalid option, please select 1, 2, 3, or 4.")