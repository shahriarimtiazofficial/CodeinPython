def determine_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 85:
        return "A"
    elif marks >= 80:
        return "B+"
    elif marks >= 75:
        return "B"
    elif marks >= 70:
        return "C+"
    elif marks >= 65:
        return "C"
    elif marks >= 60:
        return "D+"
    elif marks >= 50:
        return "D"
    else:
        return "F"
marks = int(input("Enter your marks: "))
print("Your grade is:", determine_grade(marks))
