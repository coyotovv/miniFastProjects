import random as rnd


theNum = rnd.randint(1, 100)

print("Welcome to the guessing game! Try to guess the number I'm thinking of between 1 and 100.\n")
counter = 0


while True:
    guess = int(input("Enter your guess: "))
    if guess < 1 or guess > 100:
        print("Please enter a valid number between 1 and 100.")

    elif counter == 10:
            print("Sorry, you've used all your attempts. The number was:", theNum)
            break
    
    else:
        if guess < theNum:
            print("Too low!")
            counter += 1
            print(f"You have {10 - counter} attempts left.")

        elif guess > theNum:
            print("Too high!")
            counter += 1
            print(f"You have {10 - counter} attempts left.")


        else:
            print("Congratulations! You guessed it!")


