student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]

if score >= 90:
    student_grades[student] = ('outstanding performance')
elif score >= 80:
    student[student] = (' V good performance')
elif score >= 70:
     student_grades[student] = ('good performance')
elif score >= 60:
     student_grades[student] = ('average performance')
else:
    print('worst performance')

# 🚨 Don't change the code below 👇
print(student_grades)