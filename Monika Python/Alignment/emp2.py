class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

students = []

def insert_student():
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    students.append(Student(roll, name, marks))
    print("Student Inserted Successfully!\n")

def display_students():
    if not students:
        print("No Records Found!\n")
        return
    
    print("\n{:<10}{:<15}{:>10}".format("Roll","Name","Marks"))
    print("-" * 35)
    for s in students:
        print("{:<10}{:<15}{:>10.2f}".format(s.roll, s.name, s.marks))
    print()

def update_student():
    roll = int(input("Enter Roll No to Update: "))
    for s in students:
        if s.roll == roll:
            s.name = input("Enter New Name: ")
            s.marks = float(input("Enter New Marks: "))
            print("Record Updated Successfully!\n")
            return
    print("Student Not Found!\n")

def delete_student():
    roll = int(input("Enter Roll No to Delete: "))
    for s in students:
        if s.roll == roll:
            students.remove(s)
            print("Record Deleted Successfully!\n")
            return
    print("Student Not Found!\n")

# Menu Driven Loop
while True:
    print("------ Student Menu ------")
    print("1. Insert")
    print("2. Display")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")
    
    choice = int(input("Enter Choice: "))
    
    if choice == 1:
        insert_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        print("Program Ended!")
        break
    else:
        print("Invalid Choice!\n")