#Build a simple score classifier and loop through 5 sample records
scores = [85, 92, 78, 96, 88]
for score in scores:
    if score >= 90:
        print(f"Score: {score} - Grade: A")
    elif score >= 80:
        print(f"Score: {score} - Grade: B")
    else:
        print(f"Score: {score} - Grade: C")
        