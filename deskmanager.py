from queue import Queue

# Initialized queue for storing patient names
patients = Queue()

while True:
    print("Desktop Manager - Patient Registration and Appointment System\n")
    print("""
        1. Press 1 to Register the patient
        2. Press 2 to Remove the Patient
        3. Press 3 Display the patient 
        4. Press 4 to Exit
        """)
    userinput = input(">>> ")
    print()

    if userinput == "1":
        patient_name = input('Enter patient name: ')
        patients.put(patient_name)
    elif userinput == "3":
        if patients.empty():
            print("No patients in the queue.")
        else:
            print("Current Patient Queue: ")
            for i in patients.queue:
                print(i)
    elif userinput == "4":
        print("Exiting the program.")
        break
