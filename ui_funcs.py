from typing import Dict, Callable
from markbook import *


# Made by Patrick
def generic_individual_page(            
                            comments: str,
                            current_dict: dict,
                            indent: int,
                            dict_display: int,
                            functional_lists: bool,
                            page_travel_options: list,
                            page_travel_option_displayed: list):
  """
  Creates a page that can represent many things when called. The page consists of a 'comment' at the very top, a series of strings that represent the current page's dictionary (which may or may not contain options. Refer to the functional_lists section below for more information), a series of options which allow the user to naviage from the page at hand, and finally--at the very bottom--an input reciever for the user to select the page's options.
  
  A page create like this: 

  - generic_individual_page("===  Cakes  ===", {"number_of_cakes" : 5}, 4, 0, false, ["main_menu"], ["Back"])

  Would look like something like this:

  ===  Cakes ===

      Number Of Cakes: 5

      [0] Back
  
    Args:
        - comments: A string to your choosing will be printed near the top of the console when generic_individual_page() is called. The comments parameter represents that string.

        - current_dict: What data generic_individual_page() will display (if it's a student page use a student dict, etc.)

        - indent: The higher an int 'indent' is, the more everything (except for the comments) will be pushed right.

        - dict_display: How many values of a dict should be displayed (horizontally) if a series of dicts are to be displayed in the page? Keep in mind that the program cannot represent dicts directly--only lists of dicts--and cannot represent lists within lists.

        - functional_lists: Setting functional lists to true essentially turns every element in any list contained in current_dict into an option that can be selected by the user. If there is a list of dicts (dicts that represent objects that need pages of their own) somewhere in current_dict, set this to true. Otherwise, set this as false. Functional_lists will cause the program problems if it is set to true and a list in current_dict contains anything other than dicts. 

        - page_travel_options: A list that represents all the pages this page can lead to. Each element in page_travel_options is a destination that generic_individual_page() will automatically make a selectable option for. This list determines what the program will RETURN if a certain option is chosen.

        - page_travel_option_displayed: How each option created with page_travel_options will be displayed for the user. If, for instance, you want the program to return "hello_world" if a certain option is chosen, but you want the option to look like "Hello World!!!" in the console, you would put "Hello World!!!" in page_travel_option_displayed at the same index you put "hello_world" in page_travel options. Page_travel_option_displayed and page_travel_options must be the same length.

    Returns:
        - Depending on user input, the function may return an element from page_travel_options or a dict from within a list inside current_dict (assuming functional_lists is set to true with regards to the latter statement). This returned value can then be used to change the markbook's page inside main() by setting the main()'s current_page variable to this function's return value.
  """
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


# Made by Patrick
def input_classroom(back_loc, updating: bool):
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


# Made by Clarence
def input_assignment(back_loc, updating: bool):  # Clarence
    if updating:
        print("Update assignment details")
    else:
        print("Enter assignment details")
    name = input("\nName of Assignment: ")
    due_date = input("Due Date: ")
    mark = float(input("Mark: "))
    assignment = create_assignment(name, due_date, mark)
    return assignment, back_loc


# Made by Mohammed
def input_student(back_loc, updating: bool):     # Mohammed
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
        mark = int(input(f"Enter Mark {i + 1}: "))
        marks.append(mark)
    comments = input("Enter Comments: ")
    student = {
            "first_name": first_name, "last_name": last_name,
            "gender": gender, "student_number": student_number,
            "grade": grade, "email": email,
            "marks": marks, "comments": comments}
    return student, back_loc
