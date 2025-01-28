#3Q. Write a Python program that takes a student's marks in three subjects as input.
#1)If the average is greater than or equal to 90, print "Grade: A". 2)If the average is between 80 and 89, print "Grade: B". 3)If the average is between 70 and 79, print "Grade: C". 4)Otherwise, print "Grade: Fail".

# Input: Student's marks in three subjects
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

# Calculate average
average = (subject1 + subject2 + subject3) / 3

# Determine grade based on average
if average >= 90:
    print("Grade: A")
elif 80 <= average < 90:
    print("Grade: B")
elif 70 <= average < 80:
    print("Grade: C")
else:
    print("Grade: Fail")
