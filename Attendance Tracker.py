Total_lectures = int(input("Enter Total number of lectures : "))

if Total_lectures <= 0 :
     print("Total number of lectures must be greater than 0")

else:
     Attended_lectures = int(input("Enter Total number of lectures attended : "))

     Attendance_pct = (Attended_lectures / Total_lectures ) * 100

     if  Attendance_pct > 75  :
         print("Excellent, keep it up")

     elif Attendance_pct == 75 :
          print("Good, You have attended 75% of your lectures")

     elif  Attendance_pct >= 60 :
          print ("Warning! Attend all the lectures for next two days")

     else  :
          print("Red alert! Your attendance is low meet the class teacher immediately")





