import random

def play(): #function
    print("*********************************")
    print("****Welcome to Guessing Game!****")
    print("*********************************")

    secret_number = random.randrange(1,101)
    attempt_total = 0
    point = 1000


    #define level to game
    print("What level do you want?")
    print("(1) Easy (2) Medium (3) Hard")


    level = int(input("Define a level: "))


    if (level == 1):
        attempt_total = 20
    elif(level== 2):
        attempt_total = 10
    else:
        attempt_total = 5


    #looping
    for rounding in range (1, attempt_total + 1):
        print("Attempt {} of {}".format(rounding, attempt_total))
        guess_str = input("Enter a number between 1 and 100: ")
    #   print("You Typed: ", guess_str)  
        guess = int(guess_str)


        if (guess < 1 or guess > 100):
            print("You should guess a number between 1 and 100.")
            continue


        hit     = guess == secret_number
        bigger  = guess > secret_number
        smaller = guess < secret_number


        if (hit):
            print("YEAAAH YOU HIT and score {} points" .format(point)) #retornando errado, problema não é a logica 
            break
        else:
            if(bigger):
                print("You Missed! This number that u guess is bigger than secret number.")
            elif (smaller):
                print("You Missed! This number that u guess is smaller than a secret number.")


        lost_point = abs(secret_number - guess)
        point = point - lost_point
        

    print("End of game. the number of the game is {}" .format(secret_number))

if(__name__ == "__main__"):
    play()