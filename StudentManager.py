students_list = []
students_dict = {}

name = input("Enter student name: ")
age = input("Enter student age: ")
grade = input("Enter student grade: ")

students_list.append(name)
students_dict[name] = {"Age": age, "Grade": grade}

print("Student information added successfully.")


print("Student Details:")
for name, info in students_dict.items():
    print(f"Name: {name}, Age: {info['Age']}, Grade: {info['Grade']}")


name_to_search = input("Enter student name to search: ")
if name_to_search in students_dict:
    info = students_dict[name_to_search]
    print(f"Student Found - Name: {name_to_search}, Age: {info['Age']}, Grade: {info['Grade']}")
else:
    print(f"Student not found!")

name_to_remove = input("Enter student name to remove: ")
if name_to_remove in students_dict:
    students_list.remove(name_to_remove)
    del students_dict[name_to_remove]
    print(f"Student '{name_to_remove}' removed successfully.")
    print("Updated Student details: ", students_dict)
else:
    print(f"Student not found!")