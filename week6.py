class Student():
    count = 0
    def __init__(self,gpa,major,level, minor=" "):
        self.gpa = gpa
        self.major = major
        self.level = level
        self.minor = minor
        self.courses = []
        
Eve = Student(3, 'biology', 'sophmore', "fashion")
Kisha = Student(3, 'nursing', 'junior')
Sarai = Student(3, 'scientist', 'freshman')


students = [Eve,Kisha,Sarai]
print(students)


for s in students:
    print(s)
    s.minor = 'Dance'
 
class Course():
    def __init__(self,course_id):
        self.course_id = course_id
        self.max_students = 30
        self.current_students = 0

programming101 = Course(458)
python = Course(123)

Eve.courses = [programming101.course_id, python.course_id]
print(Eve.courses)

python.current_students = 2
programming101.current_students = 1

total_enrolled = python.current_students + programming101.current_students

