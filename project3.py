print("Welcome to the Student Collection ")

print("Select an option:\n")
print("1. Add student")
print("2. Display all students")
print("3. update Student Information")
print("4. Delete student")
print("5. Display Subject offered")
print("6. Exit")

students = {}
while True:
    choice=int(input("Enter your choice: "))
    if choice == 1:
        print("Enter student details:")
        S_id=input("Student ID:id ")
        name=input("Name: ")
        age=int(input("Age: "))
        grade=input("Grade: ")
        date_of_birth=input("Date of Birth: ")
        subject=input("Subject (comma-separated): ")

        students[S_id] = {
            "Name": name,  
            "Age": age,
            "Grade": grade,
            "Date of Birth": date_of_birth,
            "Subject": subject
        }

    elif choice == 2:
        print("Displaying all students")
        if not students:
            print("No students in the collection.\n")
        else:                       
            print("Student Collection:")
            for S_id, details in students.items():
                print(f"ID: {S_id}, Name: {details['Name']}, Age: {details['Age']}, Grade: {details['Grade']}, Date of Birth: {details['Date of Birth']}, Subject: {details['Subject']}")
            print()

    elif choice == 3:
        name=input("Enter the Student Name to update: ")
        if name in students:
            students[name]["Age"] = int(input("Enter new age: "))
            print("Information updated!")
        else:
            print("Student name not found.")

    elif choice == 4:
        name=input("Enter the Student Name to delete:")
        if name in students:
            del students[name]
            print("Student deleted!")
        else:
            print("Student name not found.\n")  

    elif choice == 5:
        print("Subjects Offered: Os,Oops,Ds,Python,Java,Web Development\n") 

    elif choice == 6:
        print("Exit the program. Good bye!")
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the Student Collection program!")