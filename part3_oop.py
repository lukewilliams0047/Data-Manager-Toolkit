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
        return self.students.pop()

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


# Create a StudentList object
roster = StudentList()

# 1. Add 5 students using add_student()
roster.add_student("Alice")
roster.add_student("Bob")
roster.add_student("Carlos")
roster.add_student("Diana")
roster.add_student("Emma")

print("After adding 5 students:", roster.students)

# 2. Add 3 more using add_many()
roster.add_many(["Frank", "Grace", "Hannah"])

print("After adding 3 more students:", roster.students)

# 3. Insert a student at index 2
roster.insert_student(2, "Isaac")

print("After inserting Isaac at index 2:", roster.students)

# 4. Remove the last student
removed_student = roster.remove_last()

print("Removed student:", removed_student)
print("After removing the last student:", roster.students)

# 5. Search for a student
print("Index of Carlos:", roster.find_student("Carlos"))

# 6. Count occurrences of a name
print("Number of times Alice appears:", roster.count_student("Alice"))

# 7. Print total number of students
print("Total number of students:", roster.total_students())

# 8. Check whether Bob exists
print("Does Bob exist?", roster.exists("Bob"))
