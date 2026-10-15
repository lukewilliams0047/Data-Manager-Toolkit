class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(name)

    def add_many(self, names):
        self.students.extend(names)

    def insert_student(self, index, name):
        self.students.insert(index, name)

    def remove_last(self):
        if len(self.students) > 0:
            return self.students.pop()
        return None

    def find_student(self, name):
        if name in self.students:
            return self.students.index(name)
        return -1

    def count_student(self, name):
        return self.students.count(name)

    def total_students(self):
        return len(self.students)

    def exists(self, name):
        return name in self.students


roster = StudentList()

while True:
    print("\n===== STUDENT LIST MENU =====")
    print("1. Add student")
    print("2. Add multiple students")
    print("3. Insert student")
    print("4. Remove last student")
    print("5. Find student index")
    print("6. Count student name")
    print("7. Show total students")
    print("8. Check if student exists")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roster.add_student(name)
        print("Student added!")
        print("Current students:", roster.students)

    elif choice == "2":
        names = input("Enter student names separated by commas: ")
        names = names.split(",")
        names = [name.strip() for name in names]
        roster.add_many(names)
        print("Students added!")
        print("Current students:", roster.students)

    elif choice == "3":
        name = input("Enter student name: ")
        index = int(input("Enter the index: "))
        roster.insert_student(index, name)
        print("Student inserted!")
        print("Current students:", roster.students)

    elif choice == "4":
        removed = roster.remove_last()
        if removed is not None:
            print("Removed student:", removed)
        else:
            print("The student list is empty.")
        print("Current students:", roster.students)

    elif choice == "5":
        name = input("Enter student name to find: ")
        index = roster.find_student(name)
        if index != -1:
            print(name, "is at index", index)
        else:
            print(name, "was not found.")

    elif choice == "6":
        name = input("Enter student name to count: ")
        count = roster.count_student(name)
        print(name, "appears", count, "time(s).")

    elif choice == "7":
        print("Total students:", roster.total_students())

    elif choice == "8":
        name = input("Enter student name to check: ")
        if roster.exists(name):
            print(name, "exists in the list.")
        else:
            print(name, "does not exist in the list.")

    elif choice == "9":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 9.")
