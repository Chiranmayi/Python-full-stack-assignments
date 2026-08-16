students = ["Anil", "Rahul", "Priya", "Sita", "Kiran"]

# Writing names into the file
with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")


# Reading names from the file
with open("students.txt", "r") as file:
    names = file.readlines()

print("Student Names:")

for name in names:
    print(name.strip())

print("Total Students:", len(names))