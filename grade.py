print("----------Student Grade Calculator----------")

sub1 = float(input("Enter the marks of subject 1:"))

sub2 = float(input("Enter the marks of subject 2:"))

sub3 = float(input("Enter the marks of subject 3:"))

sub4 = float(input("Enter the marks of subject 4:"))

sub5 = float(input("Enter the marks of subject 5:"))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total/5 * 100

if percentage >= 90:
    grade = "A+"

elif percentage >= 75:
    grade = "A"

elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"

print("Grade =", grade)