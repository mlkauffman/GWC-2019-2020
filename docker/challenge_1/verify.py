import student_submission
import copy
import sys, os

sys.stdout = open(os.devnull, "w")

books = [
    "panda",
    "bear",
    "monkey",
    "fish",
    "laser",
    "power",
    "tiger",
    "apple",
    "lion",
    "goldfish"
]

student_result = student_submission.run(copy.deepcopy(books))

scoring_result = books
scoring_result.sort()

x = 0
while x < len(books):
    books[x] = books[x].title()
    x = x + 1
    
print("Student Result:")
print(student_result)
print("\nScoring Result:")
print(scoring_result)

sys.stdout = sys.__stdout__
if(student_result == scoring_result):
    print("Victory!")
else:
    print("Defeat!")