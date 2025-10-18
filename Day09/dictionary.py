student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for i in student_scores:
    # print(i) # access key
    score = (student_scores[i])   #access the value
    if score >=91:
        student_grades[i] = "Outstanding"
    elif score >= 81:
        student_grades[i] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[i] = "Acceptable"
    else:
        student_grades[i] = "Fail"
        