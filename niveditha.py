def get_grade(score):
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
         return "C"
    elif score >= 60:
         return "D"
    elif score >= 50:
         return "E"
    else:
         return "F"
    
score=(input("Enter the score list (score(0-100)):"))
list = [int(s.strip()) for s in score.split(",")]

for score in list:
    print(f"Score:{score} -> Grade:{get_grade(score)}")


    