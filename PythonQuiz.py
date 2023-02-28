#Python Quiz Program

questions = ("1. A = { 1,5,3,7,9} and B = {2,3,4,5,6} then A n  B = ___",
             "2. A = {1,2,3,4,5,6} and B = {2,4,6} Which of the following represent A  U B?",
             "3. Who created C language?",
             "4. Who designed and implemented C++ Language?",
             "5. Python Language was created by - ")


options = (("A.{ 1,5,3,7,9}","B.{2,3,4,5,6}","C.{ 3, 5}","D. None of these"),
           ("A.{3,4,6}","B.{2,4,6}","C.{1,10,90}","D. {1,2,3,4,5,6}"),
           ("A.Guido van Rossum","B.Bjarne Stroustup","C.Dennis Ritchie","D.James Gosling"),
           ("A.Dennis Ritchie","B.Guido van Rossum","C.James Gosling","D.Bjarne Stroustup"),
           ("A.Guido van Rossum","B.Bjarne Stroustup","C.Dennis Ritchie","D.James Gosling"))

answers = ("C","D","C","D","A")
guesses = []
score = 0
q_num = 0

for question in questions:
    print("**********************")
    print(question)
    for option in options[q_num]:
        print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    if guess == answers[q_num]:
        score += 1
        print("Correct answer!")
    else:
        print("Incorrect answer.")
        print(f"{answers[q_num]} is the correct answer.")
    q_num += 1


print("********/RESULTS/********")

print("Answers- ",end = " ")
for answer in answers:
    print(answer,end = " ")
print()
    
print("Guesses = ",end = " ")
for guess in guesses:
    print(guess, end = " ")
print()

score = int(score / len(questions)*100)
print(f"Your score is = {score}%")









