students = {
    "Anil": {"marks": 89, "grade": "A"},
    "Rahul": {"marks": 76, "grade": "B"},
    "Priya": {"marks": 95, "grade": "A+"},
    "Sita": {"marks": 82, "grade": "A"},
    "Kiran": {"marks": 68, "grade": "B"}
}

print("Student Details:")

for name, details in students.items():
    print("Name:", name)
    print("Marks:", details["marks"])
    print("Grade:", details["grade"])
    print()


highest_student = max(
    students,
    key=lambda name: students[name]["marks"]
)

print("Student with highest marks:", highest_student)
print("Highest Marks:", students[highest_student]["marks"])