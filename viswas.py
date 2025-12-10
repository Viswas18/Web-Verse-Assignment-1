def get_grade(score):
    if 90 < score <= 100:
        return "A"
    elif 80 < score <= 90:
        return "B"
    elif 70 < score <= 80:
        return "C"
    elif 60 < score <= 70:
        return "D"
    else:
        return "F"


def main():
    """Main function to process student scores and display their grades."""
    user_input = input("Enter the score (comma separated): ")

    scores = [int(x.strip()) for x in user_input.split(",")]

    print()

    for score in scores:
        grade = get_grade(score)
        print(f"Grade of student with mark {score} is {grade}")


if __name__ == "__main__":
    main()