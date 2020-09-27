"""
Markbook Application
Group members: Patrick Wu, Clarence Corpuz, Mohammed Tarek 
"""
from typing import Dict
from typing import Callable
import os

#Variables:
current_page = "classes_page"
class_list = []


#API
def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary"""
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


def remove_classroom(classroom : dict, class_list : list):
  class_list.remove(classroom)


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
    return classroom


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
        student: The student whose data needs to be updated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    student.update(**kwargs)
    return student


#User Interface


def classes_page(
  class_list : list, 
  add_class_loc : str, 
  self_loc : str, 
  indent : int): 
  #Contribution log: Made by Patrick
  print("""
  ====== Welcome To the Markbook ======

  Classes:""")

  class_option_indent = " " * indent

  for i in range(len(class_list)):
    print(f"\n{class_option_indent}[{i}]", {class_list[i]["course_name"]})
  print(f"\n{class_option_indent}[{len(class_list)}]", "Add class")

  user_choice = input(f"\n{class_option_indent}Your choice: ")

  try:
    user_choice = int(user_choice)
    if user_choice == len(class_list):
      return add_class_loc
    return class_list[user_choice]
  except:
    return self_loc


def input_classroom(back_loc : str):
    print("Enter class details")
    course_code = input("\nEnter course code: ")
    course_name = input("Enter course name: ")
    period = int(input("Enter period: "))
    teacher_name = input("Enter teacher name: ")
    classroom = create_classroom(course_code, course_name, period, teacher_name)
    return classroom, back_loc


def individual_class_page(
  class_list : list, 
  class_dict : dict,
  indent : int, 
  page_travel_options : list,
  page_travel_option_displayed : list): 
  #Contribution log: Made by Patrick
  class_option_indent = " " * indent

  for key, value in class_dict.items():
    data_container_name = key.replace("_", " ").title()
    if type(value) is list:
      display_list = []
      for i in value:
        simplified_dict_identifier = list(i.values())[0]
        display_list.append(f"{simplified_dict_identifier}")
      print(f"{class_option_indent}{data_container_name}: {display_list}")
    else:
      print(f"{class_option_indent}{data_container_name}: {value}")

  for i in range(len(page_travel_options)):
    specific_option_name = page_travel_option_displayed[i]
    print(f"\n{class_option_indent}[{i}] {specific_option_name}")

  user_choice = int(input(f"\n{class_option_indent}Your choice: "))

  try:
    return page_travel_options[user_choice]
  except:
    return self_loc


def input_assignment(back_lot: dict):
    name = input("Name of Assignment: ")
    due_date = input("Due Date: ")
    mark = float(input("Points: "))
    assignment = create_assignment(name, due_date, mark)
    return assignment, back_lot


def add_assignment_to_classroom(assignment: Dict, classroom: Dict):
    """Adds assignment to a classroom

    Args:
        assignment: assignment dict
        classroom: The classroom to add the assignment to
    """
    classroom["assignment_list"].append(assignment)
    return classroom


def edit_assignment(assignment: dict):
    user_input = input("Name of assignment you want to change: ")
    for i in assignments_list:
        for key, value in i.items():
            if key == user_input:
                name_change = input("Name Change: ") 
                due_change = input("Due Date Change: ")
                points_change = input("Points change: ")
                assignment["name"] = name_change
                assignment["due"] = due_change
                assignment["points"] = points_change
    return assignment


def input_student(back_loc : dict):
    print("Enter student details")  
    first_name = input("\nEnter first name: ")
    last_name = input("Enter last name: ")
    gender = input("Enter gender: ")
    #student_number = input("Enter student number: ")
    #grade = int(input("Enter grade: "))
    #email = input("Enter email: ")
    #numMarks = int(input("How many marks do you want to enter: "))
    #marks = []
    #for i in range(numMarks):
        #mark = input("Enter marks: ")
        #marks.append(mark)
    #comments = input("Enter comments: ")
    student = {"first_name": first_name, "last_name": last_name, "gender": gender}
    return student, back_loc



while True: 
  os.system('clear')
  if current_page == "classes_page":
    current_page = classes_page(class_list, "add_class", "classes_page", 5)
  elif current_page == "add_class":
    adding_classroom = input_classroom("classes_page")
    class_list.append(adding_classroom[0])
    current_page = adding_classroom[1]
  else:
    for i in class_list:
      if current_page == i:
        current_page = individual_class_page(
        class_list, i, 6,
        ["classes_page", "edit_class", "remove_class", "add_student", "add_assignment", "edit_assignment"], 
        ["Back", "Edit Class", "Remove Class", "Add Student", "Add Assignment", "Edit Assignment"])
      elif current_page == "edit_class":
        adding_classroom = input_classroom(i)
        i.update(adding_classroom[0])
        current_page = adding_classroom[1]
      elif current_page == "remove_class":
        remove_classroom(i, class_list)
        current_page = "classes_page"
      elif current_page == "add_student":
        adding_student = input_student(i)
        add_student_to_classroom(adding_student[0], i)
        current_page = adding_student[1]
      elif current_page == "add_assignment":
        adding_assignment = input_assignment(i)
        add_assignment_to_classroom(adding_assignment[0], i)
        current_page = adding_assignment[1]
      elif current_page == "edit_assignment":
        pass
        
