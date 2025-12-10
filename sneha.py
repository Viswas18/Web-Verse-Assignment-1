def get_grade(score):
    if 90 <= score <= 100:
        return 'A+'
    elif 85 <= score < 90:
        return 'A'
    elif 80 <= score < 85:
        return 'B+'
    elif 75 <= score < 80:
        return 'B'
    elif 70 <= score < 75:
        return 'C+'
    elif 65 <= score < 70:
        return 'C'
    elif 60 <= score < 65:
        return 'D+'
    elif 55 <= score < 60:
        return 'D'
    elif 50 <= score < 55:
        return 'P'    # just pass
    else:
        return 'F'
    

score = input("Enter Students Score: ")


scores = [int(score.strip()) for score in score.split(',')]


print("\n\t\tStudent Grades\t\t")
for i, score in enumerate(scores, start=1):
    grade = get_grade(score)
    print(f"Student {i}: Score = {score}, Grade = {grade}")
