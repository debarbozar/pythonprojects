print("*********************************")
print("Welcome to Guessing Game!")
print("*********************************")

secret_number = 42
attempt_total = 3 
rounding = 1

while (rounding <= attempt_total):
    print("Attempt", rounding, "of", attempt_total)
    guess_str = input("Enter a number: ")
    print("You Typed: ", guess_str)  
    guess = int(guess_str)

    hit = guess == secret_number
    bigger = guess > secret_number
    smaller = guess < secret_number

    if (hit):
        print("YEAAAH YOU HIT") #retornando errado, problema não é a logica 
        break
    else:
        if(bigger):
            print("You Missed! This number that u guess is bigger than secret number.")
        elif (smaller):
            print("You Missed! This number that u guess is smaller than a secret number.")
    
    rounding = rounding + 1 


print("End of game.")