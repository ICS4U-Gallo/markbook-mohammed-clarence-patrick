"""
Markbook Application
Group members: Patrick Wu, Clarence Corpuz, Mohammed Tarek 
"""
from typing import Dict, Callable
import json


def create_assignment(name: str, due: str, points: int) -> Dict:        #Clarence
    """Creates an assignment represented as a dictionary"""
    assignment = {
    "name" : name, 
    "due" : due, 
    "points" : points}           
    return assignment


def add_assignment_to_classroom(assignment : dict, classroom : dict): 
  """Adds assignment to a classroom
  Args:
      student: Assignment dict
      classroom: The classroom to add the student to
  """
  classroom["assignment_list"].append(assignment)
  return classroom
    

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


def remove_classroom(classroom : dict, class_list : list):
  class_list.remove(classroom)
  return class_list


def add_student_to_classroom(student: Dict, classroom: Dict):       # Mohammad
    """Adds student to a classroom
    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """
    classroom["student_list"].append(student)
    return classroom


def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom
    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """   
    classroom["student_list"].remove(student)
    return classroom


def edit_student(student: Dict, **kwargs: Dict):        # Clarence
    """Edits the student's info with the provided key/value pairs
    Args:
        student: The student whose data needs to be updated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    student.update(**kwargs)
    return student


def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""
    mark_sum = 0
    for i in student["marks"]:
      mark_sum += i
    return mark_sum / len(student["marks"])


def report_card(student_list: list, order_greatest: bool):
    marks_list = []
    for student in student_list:
        average = calculate_average_mark(student) 
        marks_list.append(average)
    if order_greatest:
        marks_list = sorted(marks_list, reverse=True)
        return marks_list
    else:
        return marks_list

    
def load(filePath="database.json"): # Patrick
  with open(filePath, "r") as file:
    return json.loads(file.read())


def save(due_to_save, filePath="database.json"):
  with open(filePath, "w") as file:
    file.write(json.dumps(due_to_save))

