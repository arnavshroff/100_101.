class Student(object):
    def __init__(self,name,age,level,grades=None):
        self.name = name
        self.age = age
        self.level = level
        self.grades = {}

    def setGrade(self,course,grades):
        self.grades[course]=grades
    
    def getGrade(self,course):
        return self.grades[course]

Arnav = Student("Arnav",13,8,{"Maths":100})
print(Arnav.getGrade({"Maths"}))

    



