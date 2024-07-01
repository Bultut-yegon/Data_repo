class Student:
    def __init__(self,marks) -> None:
        self.__marks=marks
    def get_marks(self):
        return self.__marks
    def set_marks(self,new_marks):
        if not isinstance(new_marks,int):
            raise ValueError('Marks must be an integer')
        if new_marks<0 or new_marks<=100:
            # raise ValueError('Marks must be between 0 and 100')
            return new_marks
        else:
            raise ValueError("Invalid marks")
    def Marks(self):
        return self.__marks
        
student=Student(90)
print(student.set_marks(20))
print(student.get_marks())
print(student.Marks())