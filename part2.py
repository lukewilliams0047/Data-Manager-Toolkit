grades = [88, 92, 75, 92, 100, 67, 88]

# 1. Count how many times 88 appears
print("Number of times 88 appears:", grades.count(88))

# 2. Insert a missing grade at index 2
grades.insert(2, 85)
print("After inserting 85 at index 2:", grades)

# 3. Append a new grade from user input
new_grade = int(input("Enter a new grade: "))
grades.append(new_grade)
print("After adding the new grade:", grades)

# 4. Remove the last grade using pop()
removed_grade = grades.pop()
print("Removed grade:", removed_grade)
print("After pop():", grades)

# 5. Check whether 100 exists
print("Does 100 exist?", 100 in grades)

# 6. Print the length of the list
print("Length of the list:", len(grades))

# 7. Print the index of the first 92
print("Index of the first 92:", grades.index(92))
