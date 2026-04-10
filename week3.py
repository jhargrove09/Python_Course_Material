#students directory
#input name and score
#scores directory
#add directorys to list
#display student records
#show pass/fail
#calculate class average

students = []
while True:
    name = input("Enter student name: ")
    score = int(input("What was the student's score?: "))
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 65:
        grade = "D"
    else:
        grade = "F"
    
    students.append({"name": name, "score": score, "grade": grade})
    
    another = input("Add another student? (yes/no): ").strip().lower()
    if another != "yes":
        break

print("\nStudent Records")
print("---------------------------")
for student in students:
    result = "Pass" if student["score"] >= 65 else "Fail"
    print(f"{student['name']} - {student['score']} {student['grade']} - {result}")

passed_count = 0
for student in students:
    if student["score"] >= 65:
        passed_count = passed_count + 1
print()
print(passed_count, "students passed this test.")

total = 0
for student in students:
    total = total + student["score"]
average = total / len(students)
print(f"Class average: {average:.1f}")