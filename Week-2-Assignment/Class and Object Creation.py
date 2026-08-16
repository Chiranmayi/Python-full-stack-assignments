class Student:
    def display_details(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)


student1 = Student()
student1.name = "Anil"
student1.roll_number = 101
student1.marks = 89

student2 = Student()
student2.name = "Rahul"
student2.roll_number = 102
student2.marks = 92

student1.display_details()
student2.display_details()