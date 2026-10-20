class Student:
    def init(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.scores = {}

    def add_score(self, course, score):
        if score < 0 or score > 20:
            print("Invalid score")
        else:
            self.scores[course] = score

    def average(self):
        if len(self.scores) == 0:
            return 0

        return sum(self.scores.values()) / len(self.scores)

    def best_course(self):
        if len(self.scores) == 0:
            return None

        return max(self.scores)#بپزسم از استاد

    def failed_courses(self):
        failed = []

        for course, score in self.scores.items():
            if grade < 10:
                failed.append(course)

        return failed

    def status(self):
        avg = self.average()

        if avg >= 17:
            return "Excellent"
        elif avg >= 14:
            return "Good"
        elif avg >= 12:
            return "Normal"
        else:
            return "not good"

    def report(self):
        print(f"Student: {self.name} (ID: {self.student_id})")

        for course, score in self.scores.items():
            print(f"{course}: {score}")

        print(f"Average: {self.average()}")
        print(f"Best course: {self.best_course()}")
        print(f"Failed courses: {self.failed_courses()}")
        print(f"Status: {self.status()}")


student1 = Student("Sara Ahmadi", "40312345")

student1.add_score("Math", 18)
student1.add_score("Physics", 9)
student1.add_score("Programming", 20)
student1.add_score("English", 15)

student2 = Student("Ali Rezaei", "40312346")

student2.add_score("Math", 12)
student2.add_score("Physics", 16)
student2.add_score("Programming", 14)
student2.add_score("English", 10)

student1.report()
student2.report()

student1.add_score("Chemistry", 25)
