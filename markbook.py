"""
Markbook Application
Group members: Patrick Wu, Clarence Corpuz, Mohammed Tarek """
from typing import Dict, Callable
import json


# Made by Clarence
def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary"""
    assignment = {
        "name": name,
        "due": due,
        "points": points}
    return assignment


# Made by Clarence
def add_assignment_to_classroom(assignment: dict, classroom: dict):
    """Adds assignment to a classroom
    Args:
        student: Assignment dict
        classroom: The classroom to add the student to
  """
    classroom["assignment_list"].append(assignment)
    return classroom


# Made by Patrick
def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""
    classroom = {
        "course_code": course_code,
        "course_name": course_name,
        "period": period,
        "teacher": teacher,
        "student_list": [],
        "assignment_list": []}
    return classroom


# Made by Patrick
def remove_classroom(classroom: dict, class_list: list):
    class_list.remove(classroom)
    return class_list


# Made by Mohammed
def add_student_to_classroom(student: Dict, classroom: Dict):       
    """Adds student to a classroom
    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """
    classroom["student_list"].append(student)
    return classroom


# Made by Mohammed
def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom
    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    classroom["student_list"].remove(student)
    return classroom


# Made by Mohammed
def edit_student(student: Dict, **kwargs: Dict):        
    """Edits the student's info with the provided key/value pairs
    Args:
        student: The student whose data needs to be updated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    student.update(**kwargs)
    return student


# Made by Mohammed
def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""
    mark_sum = 0
    for i in student["marks"]:
        mark_sum += i
    return mark_sum / len(student["marks"])


# Made by Clarence
def report_card(student_list: list, order_greatest: bool):
    marks_list = []
    for student in student_list:
        average = calculate_average_mark(student)
        student_first_name = student["first_name"]
        student_last_name = student["last_name"]
        student_and_mark = f"{student_first_name} {student_last_name} | {average} |"
        marks_list.append(student_and_mark)
    if order_greatest:
        marks_list = sorted(marks_list, reverse=True)
        return marks_list
    else:
        return marks_list


# Made by Patrick
def load(file_path="database.json"): 
    with open(file_path, "r") as file:
        return json.loads(file.read())


# Made by Patrick
def save(due_to_save, file_path="database.json"):
    with open(file_path, "w") as file:
        file.write(json.dumps(due_to_save))
