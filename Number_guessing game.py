import random
print("Welcome to number guessing game!")
while True:
   
    level = input("Select difficulty level(easy,medium,hard):").lower()
    if level == "easy":
        number = random.randint(1,10)
        break
    elif level == "medium":
        number = random.randint(1,50)
        break
    elif level == "hard":
        number = random.randint(1,100)
        break
    else:
        print("Invalid difficulty level")
    
score = 0
while True:   
    try:
        guess_number = int(input("Guess the number(or enter 0 to exit):"))
    except ValueError:
        print("The input should be integer value!")
        continue
    
    if guess_number == 0:
        print("Thank you for playing")
        break
    if guess_number == number:
        score += 10
        print("Correct number")
    else:
        print("Wrong answer,try again")    
print("Score:",score)


