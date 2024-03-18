from queue import Queue
import sys

patients = Queue()
current_patient = None

while True:
    print("Desktop Manager - patient registration and appointment system\n")
    print("""
        1. press 1 to register the patient
        2. press 2 to remove the patient
        3. press 3. Display the patient
        4. press 4 to exit
          """)
    userinput = input(">>>").lower()
    print()

    if userinput == "1":
        patient_name = input("Enter patient name:")
        patients.put(patient_name)
        current_patient = patient_name
        print(f"patient{patient_name} successfully registered\n")

    elif userinput == "2":
        patients.get()
        print(f"patient{current_patient} removed after meeting the doctor.\n")

    elif userinput == "3":
        print("Current Patient Queue")
        for i in list(patients):
            print(i)







