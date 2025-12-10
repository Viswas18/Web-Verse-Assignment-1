def get_grade(score):
    if 90 < score <= 100:
        return "A"
    elif 80 < score <=90:
        return "B"
    elif 70 < score <=80:
        return "C"
    elif 60 < score <= 70:
        return "D"
    else:
        return "F"


scores = input("Enter scores separated by commas: ")

score_list = scores.split(",")

print("\nStudent Grades:\n")

count = 1
for s in score_list:
    number = int(s)   
    grade = get_grade(number)
    print("Student", count, "Score:", number, "Grade:", grade)
    count += 1
