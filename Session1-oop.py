class Student:
  def --init--(self, name, student_id, major):
    self.name = name
    self.student_id = student_id
    self.major = major

  def display_info(self):
    print("Name:",self.name)
    print("Student_id:",self.student_id)
    print("Major:",self.major)

student1 = Student("Ali", 123, "AI")
student2 = Student("Sara", 456, "Computer")

student1.display_info()
student2.display_info()
