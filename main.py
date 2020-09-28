"""
Markbook Application
Group members: Patrick Wu, Clarence Corpuz, Mohammed Tarek 
"""
from ui_funcs import *
from markbook import *
import os


current_page = "classes_page"       #Patrick
try:
  class_list = list(load())
except:
  class_list = []
  save(class_list)


def main(current_page, class_list : list):

  while True:
    os.system('clear')
    if current_page == "classes_page":
      current_page = generic_individual_page(
          "===  Welcome to the Markbook  ===",
          {"Class List" : class_list}, 5, 2, True,
          ["add_class", "save"], 
          ["Add Class", "Save"])
    elif current_page == "add_class":
      adding_classroom = input_classroom("classes_page", False)
      class_list.append(adding_classroom[0])
      current_page = adding_classroom[1]
    elif current_page == "save":
      save(class_list)
      current_page = "classes_page"
    else:
      os.system('clear')
      for i in class_list:
        if current_page == i:
          current_page = generic_individual_page(
          "===  Classroom  ===",
          i, 5, 4, True,
          ["classes_page", "edit_class", "remove_class", "add_student", "add_assignment", "report_card"], 
          ["Back", "Edit class", "Remove class", "Add student", "Add assignment", "Report Card"])
        elif current_page == "edit_class":
          editing_classroom = input_classroom(i, True)
          i.update(editing_classroom[0])
          current_page = editing_classroom[1]
        elif current_page == "remove_class":
          class_list = remove_classroom(i, class_list)
          current_page = "classes_page"
        elif current_page == "add_student":
          adding_student = input_student(i, False)
          add_student_to_classroom(adding_student[0], i)
          current_page = adding_student[1]
        elif current_page == "add_assignment":            #Clarence
          adding_assignment = input_assignment(i, False)
          add_assignment_to_classroom(adding_assignment[0], i)
          current_page = adding_assignment[1]
        elif current_page == "report_card":
          current_page = generic_individual_page(
          "===  Report Card  ===", 
          {"Class Averages" : report_card(i["student_list"], True)}, 5, 4, False,
          [i], 
          ["Back"])
        else:
          os.system('clear')
          for i2 in i["assignment_list"]:
            if current_page == i2:
              current_page = generic_individual_page(
              "===  Student  ===",
              i2, 5, 4, False,
              [i, "edit_assignment"], 
              ["Back", "Edit Assignment"])
            elif current_page == "edit_assignment":
              updating_assignment = input_assignment(i, True)
              i2.update(updating_assignment[0])
              current_page = updating_assignment[1]
          os.system('clear')
          for i2 in i["student_list"]:
            if current_page == i2:
              current_page = generic_individual_page(
              "===  Assignment  ===",
              i2, 5, 4, False,
              [i, "edit_student"], 
              ["Back", "Edit Student"])
            elif current_page == "edit_student":
              updating_student = input_student(i, True)
              edit_student(i2, **updating_student[0])
              current_page = updating_student[1]


if __name__ == "__main__":
    main(current_page, class_list)
