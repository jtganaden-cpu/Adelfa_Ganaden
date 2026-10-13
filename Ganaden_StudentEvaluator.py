def display_header():
    print("STUDENT PERFORMANCE EVALUATOR")
    print()

def get_student_info():
    return name

def evaluate_performance():
    a1 = float(input("Enter Assessment 1: "))
    a2 = float(input("Enter Assessment 2: "))
    a3 = float(input("Enter Assessment 3: "))
    average = (a1 + a2 + a3)/3
    display_report(average, a1, a2, a3)
    return average

def display_report(average, a1, a2, a3):
    print("STUDENT PERFORMANCE REPORT")
    print()
    print(f"Student Name: {name}")
    print(f"Assessment Scores: {a1}, {a2}, {a3}")
    print(f"Average Score: {average:.2f}")
    if average >= 90 and average <= 100:
        print("Performance Level: Outstanding")
    elif average >= 85 and average < 90:
        print("Performance Level: Very Satisfactory")
    elif average >= 80 and average < 85:
        print("Performance Level: Satisfactory")
    elif average >= 75 and average < 80:
        print("Performance Level: Fairly Satisfactory")
    else:
        print("Performance Level: Needs Improvement")

display_header()
name = input("Enter student name: ")
get_student_info()
evaluate_performance()
