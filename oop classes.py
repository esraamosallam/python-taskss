# classes
class Subject:
    def __init__(self, name: str, passing_grade: float, student_grade: float):
        self.name = name 
        self.passing_grade = passing_grade
        self.student_grade = student_grade

class Student:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.subjects = [] 
    def add_subject(self, subject):
        try:
            subject.passing_grade = float(subject.passing_grade)
            if subject.passing_grade == 0:
                raise ValueError("Passing grade cannot be 0")
        except ValueError as e:
            print("Error:", e)
        else:
            self.subjects.append(subject)
            print("Subject added successfully!!")
    def success_or_fail(self, subject):
        if subject.student_grade < subject.passing_grade and subject.passing_grade != 0:
            print(f"{self.name} failed {subject.name} unfortunately")
        elif (subject.student_grade > subject.passing_grade or subject.student_grade == subject.passing_grade) and subject.passing_grade != 0:
            print(f"{self.name} passed {subject.name} congrats")   

sub1 = Subject('OOP', 80, 80)
#sub2 = Subject('English', 50, 10)

stud1 = Student('Zahra', 'zahra@gmail.com')
stud2 = Student('Arwa', 'arwa@gmail.com')
stud1.add_subject(sub1)  
#st1.add_subject(sub2)  

stud1.success_or_fail(sub1)
#st2.success_or_fail(sub2)
