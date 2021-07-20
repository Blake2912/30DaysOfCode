# Here I will be revising Lists in python
# Here I will create a student attendance list where it will have the details of the students
student_name = []
student_roll_number = []
student_attendance = []
while True:
    print("What do you want to do, 1. Register Student 2. Mark attendance 3. Display 0. Exit")
    option = int(input("Enter your option: "))
    if option == 1:
        print("Student Registration")
        n = int(input("Enter the number of students in your class: "))
        for i in range(0, n):
            name = input("Enter the name of the student: ")
            roll_number = int(input("Enter the roll number of the student: "))
            student_name.append(name)
            student_roll_number.append(roll_number)
    elif option == 2:
        print("Attendance Marking")
        for i in range(0, len(student_name)):
            print("NAME: {0}\nROLL NUMBER: {1}".format(student_name[i], student_roll_number[i]))
            attendance = input("Is the student present: ")
            student_attendance.append(attendance)
    elif option == 3:
        if not student_name or not student_roll_number or not student_attendance:
            print("Student details not available")
        else:
            for i in range(0, len(student_name)):
                print("Roll: {0}\t\tName: {1}\t\tAttendance: {2}".format(student_roll_number[i], student_name[i],
                                                                         student_attendance[i]))
    elif option == 0:
        break
    else:
        continue
