"""
Markbook Application
Group members: 
"""
from typing import Dict


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



print("====== Welcome To the Markbook ======")
print("Command List")
print("Enter 1 to add student")
print("Enter 3 to remove student")
def input_classroom():
    print("Enter class details")
    course_code = input("Enter course code: ")
    course_name = input("Enter course name: ")
    period = int(input("Enter period: "))
    teacher_name = input("Enter teacher name: ")
    classroom = create_classroom(course_code, course_name, period, teacher_name)
    return classroom


def create_options(option_dict : dict, indent : int, clear_page: bool): #Contribution log: Made by Patrick
  """Prints out a list of options depending on option_dict. Selecting an option will call a function.

    Args:
        option_dict: 
            -option_dict's keys are the thing to be 'pressed' to select an option. 
            -option_dict's values are the functions that are called when an option is selected.
        indent: 
            -The higher the number, the farther right everything will appear.
        clear_page:
            -Will create_options clear the console before a function is called?
    """
  single_space = " " * indent

  print()
  for keys, values in option_dict.items():
    function_name = values.__name__.replace("_", " ")
    print(f"{single_space}[{keys}]", {function_name})

  user_choice = str(input(f"\n{single_space}Your choice: "))

  try:
    if clear_page:
      os.system('clear')
    return option_dict[user_choice]()
  except:
    return False
