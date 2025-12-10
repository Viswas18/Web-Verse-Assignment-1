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

scores = int(input("Enter scores (comma-separated): "))
score_list = scores.split(",")
for s in score_list:
    grade = get_grade(s)
    print("Score:", s, "Grade:", grade)
