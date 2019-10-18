import test_submission
import copy

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

student_result = test_submission.run(copy.deepcopy(books))

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

if(student_result == scoring_result):
    print("Victory!")