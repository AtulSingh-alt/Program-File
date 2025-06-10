student_marks ={
    "Atul":96,
    "Sunny":87,
    "Dimpy":56,
    "Rahul":47,
    "Shubh":81
}
student_grades={}
for student in student_marks:
    marks=student_marks[student]
    if marks>90:
        student_grades[student]="A+"
    elif marks>80:
        student_grades[student]="A"
    elif marks>70:
        student_grades[student]="B+"
    elif marks>60:
        student_grades[student]="B"
    else:
        student_grades[student]="F"
print(student_grades)