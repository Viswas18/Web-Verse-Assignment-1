def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
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
