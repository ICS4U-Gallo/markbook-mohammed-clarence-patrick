"""
Markbook Application
Group members: 
"""
from typing import Dict

#Variables:
current_page = "classes_page"
class_list = []

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
    
    
def input_classroom(back_loc : str):
    print("Enter class details")
    course_code = input("\nEnter course code: ")
    course_name = input("Enter course name: ")
    period = int(input("Enter period: "))
    teacher_name = input("Enter teacher name: ")
    classroom = create_classroom(course_code, course_name, period, teacher_name)
    return classroom, back_loc


def edit_classroom(classroom: Dict):
    classroom["course_code"] = input("Edit course code")
    classroom["course_name"] = input("Edit course name")
    classroom["period"] = int(input("Edit period"))
    classroom["teacher"] = input("Edit teacher")

    
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


def input_student(back_loc : dict):
    print("Enter student details")  
    first_name = input("\nEnter first name: ")
    last_name = input("Enter last name: ")
    gender = input("Enter gender: ")
    student_number = input("Enter student number: ")
    grade = int(input("Enter grade: "))
    email = input("Enter email: ")
    numMarks = int(input("How many marks do you want to enter: "))
    marks = []
    for i in range(numMarks):
        mark = input("Enter marks: ")
        marks.append(mark)
    comments = input("Enter comments: ")
    student = {"first_name": first_name, "last_name": last_name, "gender": gender, "image": image, "student_number": student_number, "grade": grade, "email": email, "marks": marks, "comments": comments}
    return student, back_loc


def individual_student_page(student: Dict):
    for key, value in student.items():
        print(key + ": " + value)


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
        class_list, i, 5,
        ["classes_page", "edit_class", "remove_class", "add_student", "add_assignment"], 
        ["Back", "Edit Class", "Remove Class", "Add Student", "Add Assignment"])
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
        pass
