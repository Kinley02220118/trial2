students_list = []
students_dict = {}

name = input("Enter students Name: ")
age = input("Enter student age: ")
grade = input("Enter student's grade: ")
students_list.append(name)
students_dict[name] = {"age": age, "grade": grade}
print("Information added successfully!")

search_students = input("Enter the student's name to search")
if search_students in students_dict:
    print(f"Student found: {name}, Age: {students_dict[name]['age']}, Grade: {students_dict[name]['grade']}")
else:
    print("Information not found")
    
remove_students = input("Enter the student's name to remove")
if remove_students in students_dict:
    students_list.remove(name)
    del students_dict[name]
    print("Student removed successfully!")
    
else:
    print("Student not found")