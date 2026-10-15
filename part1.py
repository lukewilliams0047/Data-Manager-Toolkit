students = ["Alice", "Bob", "Carlos"]

students.append("Diana")
print("After append:", students)

students.extend(["Ethan", "Fatima", "George"])
print("After extend:", students)

students.insert(1, "Hannah")
print("After insert:", students)

removed_student = students.pop()
print("After pop:", students)
print("Removed:", removed_student)

print("Alice index:", students.index("Alice"))

print("Alice count:", students.count("Alice"))

print("Total students:", len(students))

print("Does Alice exist?", "Alice" in students)
