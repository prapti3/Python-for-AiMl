# create a random number guessing game with python
import random 

guess_num = int(input("Guess the number between (1-20) : "))
num = random.randint(1,20)


if(guess_num < num):
        print("Too Low")
elif(guess_num > num):
    print("Too high")
elif(guess_num == num):
    print(f"Congratulation!!!!!! Guess number {guess_num} is equal to Generated num {num}")  
else:
    print("You Lose")