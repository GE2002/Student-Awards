#Name: Ginna Estrada
#File: if_else.py
#Checks Student's GPA's for the Dean's list and honors Roll

while True:
    last_name = input("Enter the last name (ZZZ to quit): ")
    if last_name.upper() == "ZZZ":
        break
    first_name = input("Enter the first name: ")
    while True:
        try: 
            gpa = float(input("Enter the GPA: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for GPA.")

    if gpa >= 3.5:
        print(first_name, "has made the Dean's list.")
    if gpa >= 3.25:
        print(first_name, "has made the Honors Roll.")

    print(first_name, last_name, "has a GPA of", gpa)