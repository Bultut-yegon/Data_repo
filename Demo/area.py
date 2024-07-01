# import math
# def calculate_area(shape,length=None,width=None,height=None,radius=None,diameter=None,slant_height=None,base=None,
#                    diagonal1=None,diagonal2=None):
#     if shape=='square':
#         return length**2
#     elif shape=='rectangle':
#         if width is None :
#             raise ValueError('width is required for rectangle')
#         return length*width
#     elif shape == 'circle':
#         return math.pi*(pow(radius,2))
#     elif shape=='triangle':
#         if height is None:
#             raise ValueError('height is required for triangle')
#         return 0.5*length*height
#     elif shape=='parallelogram':
        
#         return length*width
#     elif shape=='trapezium':
#         if slant_height is None or base is None:
#             raise ValueError('slant_height and base are required for trapezium')
#         return 0.5*(slant_height+base)*length
#     elif shape=='rhombus':
#         if diagonal1 is None or diagonal2 is None:
#             raise ValueError('diagonal1 and diagonal2 are required for rhombus')
#         return 0.5*diagonal1*diagonal2
#         # return 0.5*length*width
#     elif shape=='cone':
#         if slant_height is None or radius is None:
#             raise ValueError('slant_height and radius are required for cone')
#         return math.pi * (radius*slant_height + radius**2)
#     else:
#         raise ValueError('Invalid shape')
# area_of_circle=calculate_area('circle',5)
# print(area_of_circle)

# def factorial(x):
#     if x==1 or x==0:
#         return 1
#     else:
#         return x * factorial(x-1)
    
# factorial_number=factorial(7)
# print(factorial_number)
# iden=factorial_number
# print(id(iden))
# print(id(factorial_number))
# # def check_factorial(iden, factorial_number):
# #     global factorial_number
# #     if id(iden) == id(factorial_number):
# #         return True
# #     else:
#         return False

# def calculate_area(length, width):
#     """
#     Calculates the area of a rectangle.

#     Args:
#         length (float): The length of the rectangle.
#         width (float): The width of the rectangle.

#     Returns:
#         float: The area of the rectangle.
#     """
#     return length * width
# print(calculate_area.__doc__)


# def student_grades(student_data):
#     """
#     This function takes a dictionary of student data as input and returns a new dictionary
#     with the student's final grade calculated based on their assignment and exam scores.

#     The input dictionary should have the following structure:
#     {
#         'student_name': {
#             'assignments': [score1, score2, score3],
#             'exams': [score1, score2]
#         }
#     }

#     The final grade is calculated as:
#     - Assignments: 60% of the total grade
#     - Exams: 40% of the total grade
#     """
#     final_grades = {student_data.values()}

#     for student, data in student_data.items():
#         assignments = data['assignments']
#         exams = data['exams']

#         assignment_average = sum(assignments) / len(assignments)
#         exam_average = sum(exams) / len(exams)

#         final_grade = (assignment_average * 0.6) + (exam_average * 0.4)
#         final_grades[student] = final_grade

#     return final_grades

# # Example usage
# student_data = {
#     'John Doe': {
#         'assignments': [85, 92, 78],
#         'exams': [90, 85]
#     },
#     'Jane Smith': {
#         'assignments': [82, 91, 80],
#         'exams': [88, 92]
#     },
#     'Michael Johnson': {
#         'assignments': [90, 85, 92],
#         'exams': [82, 88]
#     }
# }


def get_data():
    students = {}
    
    num_students = int(input("Enter the number of students: "))
    
    for _ in range(num_students):
        name = input("Enter student's name: ").capitalize()
        
        assignment_marks = []
        print(f"Enter 3 assignment marks for {name}:")
        for i in range(3):
            mark = float(input(f"Assignment {i} mark: "))
            assignment_marks.append(mark)
        
        exam_marks = []
        print(f"Enter 2 exam marks for {name}:")
        for i in range(2):
            mark = float(input(f"Exam {i} mark: "))
            exam_marks.append(mark)
        
        students[name] = {
            'assignment_marks': assignment_marks,
            'exam_marks': exam_marks
        }
    
    return students

def Display_results(students):    
    """This function takes dictionary students which have been returned by the 'get_data' function
    Printing the dictionary
    name: represents the key
    marks: represents the value in students assignments and marks
    """
    for name, marks in students.items():
        """We use f-string to allow variables to be passed using curly braces '{}' """
        print(f"Student: {name}, Assignment Marks: {marks['assignment_marks']}, Exam Marks: {marks['exam_marks']}")
        print()
        """The purpose of this print() is to separate the students information by printing empty line. Acts like a space"""

# students variable will contain the student data, in dictionary format
#Display_results is the function that is being called and the dictionary is passed to it
students = get_data()
Display_results(students)
