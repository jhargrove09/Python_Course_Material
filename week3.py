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
    
    students.append({"name": name, "score": score})
    
    another = input("Add another student? (yes/no): ").strip().lower()
    if another != "yes":
        break

print("\nStudent Records")
print("---------------------------")
for student in students:
    result = "Pass" if student["score"] >= 65 else "Fail"
    print(f"{student['name']} - {student['score']} - {result}")    

#input("Woud you like to add another student?")
#print("Student Records/n", "-------------------/n",)
#print(student1, score, grade)