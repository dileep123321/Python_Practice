age = 20
gpa = 8.2
project_experience = False
knows_python = True

if age >= 18 and gpa > 7.0 and (project_experience or knows_python):
    print("Eligible for Internship")
else:
    print("Not eligible for Internship")
