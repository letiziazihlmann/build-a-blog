# this is for the grade walk-through
# create an empty dictonary to store the grades and credits
grades = {}

# create a while loop that will add to the dictonary, while the user needs to add more grades
while True:
    # create an input to ask the user for the # of credits and grade
    grade = input("What grade did you get in the class?")
    credit = input("How many credits is the class worth?")
    #store the inputs to the dictonary
    grades.append({'grade': float(grade), 'credit': int(credit)})
    # ask the user if they need to enter another class - for while loop
    another_grade =  input("Do you need to enter another grade?")
    if another_grade == 'n':
        break

#create variables to calculate GPA
total_quality_score = 0
total_credits = 0

#calculate total_quality_score and total_credits
for gradeinfo in grades:
    total_quality_score += (gradeinfo['grade'] * gradeinfo['credits'])
    total_credits += gradeinfo['credits']

gpa = total_quality_score / total_credits
print("Your GPA is:", gpa)
