students_list=[]
students_dict={}
name=input('Enter your name:')
age =int(input('Enter your age:'))
grade=int(input('Enter your grade:'))
students_list.append('name')
 # Add information to lists and dictionary
students_list.append(name)
students_dict[name] = {"Age": age, "Grade": grade}

print("Student information added successfully.")


    # Print student details from the dictionary
print("Student Details:")
for name, info in students_dict.items():
    print(f"Name: {name}, Age: {info['Age']}, Grade: {info['Grade']}")


    # Search for a student by name
name_to_search = input("Enter student name to search: ")
if name_to_search in students_dict:
    info = students_dict[name_to_search]
    print(f"Student Found - Name: {name_to_search}, Age: {info['Age']}, Grade: {info['Grade']}")
else:
    print(f"Student not found!")