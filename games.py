import guessingame
import hangingame

print("*********************************")
print("********Choose your Game********!")
print("*********************************")

print("(1) GuessingGame (2) HangingGame")

game = int(input("Wich game do you wanna play?"))

if(game == 1):
    print("Play Guessing Game")
    guessingame.play() #chamando uma função
elif(game == 2):
    print("Play Hanguing Game")
    hangingame.play()
else:
    print("Type a number valid")

