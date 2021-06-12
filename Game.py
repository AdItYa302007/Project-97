import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Guess A Number Between(1 And 9)")

while chances < 5:
    guess = int(input("Enter Your Guess- "))
    if guess == number:
        print("Coungratulations You Won!!!")
        print("Thanks For Playing") 
        break    
    elif guess < number:
        print("Your Guess Was Too Low: Guess A Number Higher Than", guess)
    else:
        print("Your Guess Was Too High: Guess A Number Lower Than", guess)
    chances += 1

if not chances < 5:
    print("You Lose!!! The Number Was", number)  
    print("Thanks For Playing")      
    