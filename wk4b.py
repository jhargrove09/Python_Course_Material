import boto3
from botocore.exceptions import ClientError, NoCredentialsError, BotoCoreError
import os

# s3 config
FILE_NAME = "students4b.txt"
BUCKET_NAME = "finalproject-test-1"
S3_KEY = "student-tracker/students4b.txt"

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

# load from file
def load_students():
    students = []
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    continue
                students.append({"name": parts[0], "score": int(parts[1]), "grade": parts[2]})
    except:
        students = []
    return students

# save to file
def save_students(students):
    with open(FILE_NAME, "w") as f:
        for student in students:
            f.write(f"{student['name']},{student['score']},{student['grade']}\n")

# upload to s3
def upload_file_to_s3():
    s3 = boto3.client("s3")
    try:
        s3.upload_file(FILE_NAME, BUCKET_NAME, S3_KEY)
        print("File uploaded to S3 successfully.")
    except FileNotFoundError:
        print("Local file not found. Nothing to upload.")
    except NoCredentialsError:
        print("AWS credentials not configured.")
    except (ClientError, BotoCoreError) as e:
        print(f"Upload failed: {e}")

# download from s3
def download_file_from_s3():
    s3 = boto3.client("s3")
    try:
        s3.download_file(BUCKET_NAME, S3_KEY, FILE_NAME)
        print("File downloaded from S3 successfully.")
    except NoCredentialsError:
        print("AWS credentials not configured.")
    except (ClientError, BotoCoreError) as e:
        print(f"Download failed: {e}")

# delete local file
def delete_local_file():
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
        print(f"{FILE_NAME} has been deleted locally.")
    else:
        print("No local file found to delete.")

# delete from s3
def delete_from_s3():
    s3 = boto3.client("s3")
    try:
        s3.delete_object(Bucket=BUCKET_NAME, Key=S3_KEY)
        print(f"File deleted from S3 successfully.")
    except NoCredentialsError:
        print("AWS credentials not configured.")
    except (ClientError, BotoCoreError) as e:
        print(f"Delete from S3 failed: {e}")

# delete menu
def delete_menu(students):
    print("\n--- Delete Options ---")
    print("1. Delete local file only")
    print("2. Delete from S3 only")
    print("3. Delete both local and S3")
    print("4. Go back to main menu")
    delete_choice = input("Select an option: ").strip()
    print()

    if delete_choice == "1":
        students.clear()
        delete_local_file()
    elif delete_choice == "2":
        delete_from_s3()
    elif delete_choice == "3":
        students.clear()
        delete_local_file()
        delete_from_s3()
    else:
        print("Going back to main menu.")

# check dup names
def is_duplicate(students, name):
    for student in students:
        if student["name"].lower() == name.lower():
            return True
    return False

# add student
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
            save_students(students)  # save immediately after adding
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
            # numbered list with exit option at bottom
            print("\nStudent Records")
            print("---------------------------")
            for i, student in enumerate(students):
                print(f"{i + 1}. {student['name']}: {student['score']} {student['grade']}")
            print(f"{len(students) + 1}. Exit to menu")
            print()

            remove_choice = int(input("Enter the number of the student to remove: "))

            # exit to menu
            if remove_choice == len(students) + 1:
                break

            if 1 <= remove_choice <= len(students):
                removed = students.pop(remove_choice - 1)
                save_students(students)  # save immediately after removing
                print(f"\n{removed['name']} has been removed.")
            else:
                print("Invalid number, please try again.")
                continue

            # if no students left exit automatically
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
                save_students(students)  # save after clearing all
                print("All students have been removed.")
                break
            else:
                break

# menu
def display_menu():
    print("\n--- Menu ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Remove Student")
    print("4. Upload to S3")
    print("5. Download from S3")
    print("6. Delete File")
    print("7. Exit")

# main program
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
        upload_file_to_s3()
    elif choice == "5":
        download_file_from_s3()
        students = load_students()
        print("Students loaded from S3.")
    elif choice == "6":
        delete_menu(students)
    elif choice == "7":
        save_students(students)
        print("Data saved. Thank you, have a great day!")
        break
    else:
        print("Invalid option, please select 1 through 7.")