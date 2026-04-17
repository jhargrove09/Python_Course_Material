import boto3
from botocore.exceptions import ClientError, NoCredentialsError, BotoCoreError
import os

students = []

FILE_NAME = "wk4teststudents.txt"
BUCKET_NAME = "finalproject-test-1"
S3_KEY = "student-tracker/wk4teststudents.txt"


def load_students_from_file():
    students.clear()

    if not os.path.exists(FILE_NAME):
        print("No local file found.")
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            if len(parts) != 2:
                print(f"Skipping invalid line: {line}")
                continue

            name, score = parts

            try:
                student = {
                    "name": name,
                    "score": int(score)
                }
                students.append(student)
            except ValueError:
                print(f"Skipping line with invalid score: {line}")


def save_students_to_file():
    with open(FILE_NAME, "w") as file:
        for student in students:
            file.write(f"{student['name']},{student['score']}\n")


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


def download_file_from_s3():
    s3 = boto3.client("s3")

    try:
        s3.download_file(BUCKET_NAME, S3_KEY, FILE_NAME)
        print("File downloaded from S3 successfully.")
    except NoCredentialsError:
        print("AWS credentials not configured.")
    except (ClientError, BotoCoreError) as e:
        print(f"Download failed: {e}")


def add_student():
    name = input("Enter student name: ").strip()

    try:
        score = int(input("Enter student score: ").strip())
    except ValueError:
        print("Invalid score. Please enter a whole number.")
        return

    student = {
        "name": name,
        "score": score
    }

    students.append(student)
    print("Student added.")


def view_students():
    if not students:
        print("No student records available.")
        return

    print("\nStudent Records")
    print("----------------")

    for student in students:
        status = "Passed" if student["score"] >= 60 else "Failed"
        print(f"{student['name']} - {student['score']} - {status}")


def main():
    load_students_from_file()

    while True:
        print("\nMenu")
        print("1. Add Student")
        print("2. View Students")
        print("3. Save Locally")
        print("4. Upload File to S3")
        print("5. Download File from S3")
        print("6. Reload Local File")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            save_students_to_file()
            print("Data saved locally.")
        elif choice == "4":
            save_students_to_file()
            upload_file_to_s3()
        elif choice == "5":
            download_file_from_s3()
        elif choice == "6":
            load_students_from_file()
            print("Local file reloaded.")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
