# the random function will return a floating point number,
# that is 0.0 <= random_num < 1.0
import random
random_num = random.random()
#
def scoreStudent(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade
#
def runScores(num):
    print "Scores and Grades"
    for i in range(0,num):
        score = int(random.random()*40)+60 # returns score between 60 & 100
        grade = scoreStudent(score)
        print "Score: "+str(score)+"; Your grade is",grade
    print "End of the program. Bye!"
    return
#
runScores(10)
#
