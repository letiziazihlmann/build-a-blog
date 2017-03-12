grades = {}
while True:
    grade = input('What grade did you get? [0.0 - 4.0]')
    grade = float(grade)
    credits = input('How many credits?')
    credits = int(credits)
    #will need to append to the dictonary
    grades[grade] = credits
    another_grade = input("Do you want to enter another grade? [y/n]")
    if another_grade == 'n':
        break
qualityScore = 0
credits = 0

for (k,v) in grades.items():
    qualityScore += k * v
    credits += v

finalGrade = qualityScore/credits
print("Total GPA: " + str(finalGrade))
