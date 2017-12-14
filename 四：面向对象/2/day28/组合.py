class Teacher:
    def __init__(self,name,sex,course):
        self.name=name
        self.sex=sex
        self.course=course
class Student:
    def __init__(self,name,sex,course):
        self.name=name
        self.sex=sex
        self.course=course
class Course:
    def __init__(self,name,price,peroid):
        self.name=name
        self.price=price
        self.period=peroid
python_obj=Course('python',15800,'7m')
t1=Teacher('egon','male',python_obj)
s1=Student('cobila','male',python_obj)

print(s1.course.name)
print(t1.course.name)





class Teacher:
    def __init__(self,name,sex,course_name,course_price,course_period):
        self.name=name
        self.sex=sex
        self.course_name=course_name
        self.course_price=course_price
        self.course_period=course_period


class Student:
    def __init__(self,name,sex,course_name,course_price,course_period):
        self.name=name
        self.sex=sex
        self.course_name=course_name
        self.course_price=course_price
        self.course_period=course_period

t1=Teacher('egon','male','python',15800,'7m')
s1=Student('cobila','male','python',15800,'7m')

print(s1.course.name)
print(t1.course.name)




#老师、学生与课程
#老师、学生与生日
#学生与分数
