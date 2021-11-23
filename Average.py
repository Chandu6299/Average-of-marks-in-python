
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

Total_score = 0
for score in student_scores:
    Total_score += score
print(Total_score)

Total_student = 0
for student in student_scores:
    Total_student += 1
print(Total_student)

average = round(Total_score / Total_student)
print(average)



