#Refactor yesterday's script into two functions; add one while-loop for input validation.
def classify_score(score):
    if score >= 90:
        return "Grade: A"
    elif score >= 80:
        return "Grade: B"
    else:
        return "Grade: C"


def process_scores(scores):
    for score in scores:
        grade = classify_score(score)
        print(f"Score: {score} - {grade}")



scores = []
count = 0

while count < 5:
    try:
        user_input = float(
            input(f"Enter score {count + 1} of 5 (0 to 100): ")
        )
        if 0 <= user_input <= 100:
            scores.append(user_input)
            count += 1
        else:
            print("Invalid score! Please enter a value between 0 and 100.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

print("\n--- Results ---")
process_scores(scores)