from typing import Dict, Callable
from markbook import *

# Patrick
def generic_individual_page(
  comments : str,
  current_dict : dict,
  indent : int, 
  dict_display : int,
  functional_lists : bool,
  page_travel_options : list,
  page_travel_option_displayed : list): 
  #Contribution log: Made by Patrick
  class_option_indent = " " * indent
  current_number_of_options = -1
  generated_options = []

  print(f"{comments}\n")

  for key, value in current_dict.items():
    data_container_name = key.replace("_", " ").title()

    if type(value) is list:
      print(f"{class_option_indent}{data_container_name}:")

      for i in range(len(value)):
        list_options_display = ""

        if functional_lists:
          dict_display_temp = len(list(value[i].values())) if dict_display > len(list(value[i].values())) else dict_display

          for i2 in range(dict_display_temp):
            list_options_display += f"{list(value[i].values())[i2]} | "
          current_number_of_options += 1
          generated_options.append(value[i])
          print(f"{class_option_indent*2}{[current_number_of_options]} {list_options_display}")
        else:
          list_options_display = value[i]
          print(f"{class_option_indent*2}{list_options_display}")
    else:
      print(f"{class_option_indent}{data_container_name}: {value}")

  for i in range(len(page_travel_options)):
    current_number_of_options += 1
    specific_option_name = page_travel_option_displayed[i]
    print(f"\n{class_option_indent}[{current_number_of_options}] {specific_option_name}")

  user_choice = int(input(f"\n{class_option_indent}Select an option between 0 and {current_number_of_options}: "))

  try:
    user_choice_page_travel = user_choice - (current_number_of_options - len(page_travel_options) + 1)
    return page_travel_options[user_choice_page_travel] if user_choice > len(generated_options) - 1 else generated_options[user_choice]
  except:
    return current_dict


def input_classroom(back_loc, updating : bool):
    if updating:
      print("Update class details")
    else:
      print("Enter class details")
    course_code = input("\nEnter Course Code: ")
    course_name = input("Enter Course Name: ")
    period = int(input("Enter Period: "))
    teacher_name = input("Enter Teacher Name: ")
    classroom = create_classroom(course_code, course_name, period, teacher_name)
    return classroom, back_loc

  # Clarence
  def input_assignment(back_loc, updating : bool):
    if updating:
      print("Update assignment details")
    else:
      print("Enter assignment details")
    name = input("\nName of Assignment: ")
    due_date = input("Due Date: ")
    mark = float(input("Mark: "))
    assignment = create_assignment(name, due_date, mark)
    return assignment, back_loc

# Mohammed
def input_student(back_loc, updating : bool):
    if updating:
      print("Update student details")
    else:
      print("Enter student details")
    first_name = input("\nEnter First Name: ")
    last_name = input("Enter Last Name: ")
    student_number = input("Enter Student Number: ") 
    gender = input("Enter Gender: ")
    grade = int(input("Enter Grade: "))
    email = input("Enter Email: ")
    numMarks = int(input("Number of Marks: "))
    marks = []
    for i in range(numMarks):
        mark = input(f"Enter Mark {i + 1}: ")
        marks.append(mark)
    comments = input("Enter Comments: ")
    student = {
    "first_name": first_name, "last_name": last_name, 
    "gender": gender, "student_number" : student_number, 
    "grade" : grade, "email" : email,
    "marks" : marks, "comments" : comments}
    return student, back_loc
