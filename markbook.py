"""
Markbook Application
Group members: 
"""
from typing import Dict

#API
def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary
    
    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    assignment = {
    "name" : name, 
    "due" : due, 
    "points" : points}           
    return assignment


def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""
    classroom = {
    "course_code" : course_code,
    "course_name" : course_name,
    "period" : period,
    "teacher" : teacher,
    "student_list" : [], 
    "assignment_list" : []}
    return classroom


def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""
    mark_sum = 0
    for i in student["marks"]:
      mark_sum += i
    return mark_sum / len(student["marks"])


def add_student_to_classroom(student: Dict, classroom: Dict):
    """Adds student to a classroom

    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """
    classroom["student_list"].append(student)


def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom

    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    classroom["student_list"].remove(student)


def edit_student(student: Dict, **kwargs: Dict):
    """Edits the student's info with the provided key/value pairs

    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    student.update(**kwargs)
    return student

#UI
def classes_page(class_list : list, indent : int, individual_class : Callable, add_class : Callable): #Contribution log: Made by Patrick
  print("""
  ====== Welcome To the Markbook ======

  Classes:""")

  class_option_indent = " " * indent

  for i in range(len(class_list)):
    print(f"\n{class_option_indent}[{i}]", {class_list[i]["course_name"]})
  print(f"\n{class_option_indent}[{len(class_list)}]", "Add class")

  user_choice = input(f"\n{class_option_indent}Your choice: ")

  try:
    os.system('clear')
    user_choice = int(user_choice)
    if user_choice == len(class_list):
      return add_class()
    return individual_class(*class_list[user_choice].values())
  except:
    print("INVALID OPTION")
    classes_page(class_list, indent, individual_class, add_class)

    
def input_classroom():
    print("Enter class details")
    course_code = input("Enter course code: ")
    course_name = input("Enter course name: ")
    period = int(input("Enter period: "))
    teacher_name = input("Enter teacher name: ")
    classroom = create_classroom(course_code, course_name, period, teacher_name)
    return classroom


def input_student():
    print("Enter student details")  
    first_name = input("Enter first name")
    last_name = input("Enter last name")
    gender = input("Enter gender")
    image = input("Enter image")
    student_number = input("Enter student number")
    grade = int(input("Enter grade"))
    email = input("Enter email")
    numMarks = int(input("How many marks do you want to enter"))
    marks = []
    for i in range(numMarks):
        mark = input("Enter marks: ")
        marks.append(mark)
    comments = input("Enter comments")
    student = {"first_name": first_name, "last_name": last_name, "gender": gender, "image": image, "student_number": student_number, "grade": grade, "email": email, "marks": marks, "comments": comments}
    return student


#print("Command List")
#print("Enter 1 to add student")
#print("Enter 3 to remove student")
