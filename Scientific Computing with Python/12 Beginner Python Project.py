#12. Beginner Python Project

choice=input("Choose one game: Guess(g), ComputerGuess(cg), RockPaperScissors(r): ")
# Guess the Number
import random
def guess(x):
    ran_num = random.randint(1,x)
    guess = 0
    while guess != ran_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        
        if guess<ran_num:
            print("Too low!")
        elif guess>ran_num:
            print("Too high!")
    print(f"congrats! You have guessed the number {ran_num}.")

# Guess the Number(computer)
import random
def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='C':
        if low!=high:
            guess=random.randint(low,high)
        else:
             guess=low 
        feedback=input(f'Is {guess} too high (H), too low (L), or correct (C)??')
        if feedback=='H':
            high=guess-1
        elif feedback== 'L':
            low=guess+1

    print(f'Yay!! The computer guess your number,{guess}, correctly!!')


#Rock Paper Scissors
def rockplay():
    user = input("'r'rock, 'p' paper, 's'scissors: ")
    computer = random.choice(['r','s','p'])

    if user==computer:
        return 'It\' a tie'
    if isWin(user,computer):
        return 'You win!'
    return ""

def isWin(u,c):
    if (u=='r'and c=='s')or(u=='p'and c=='r')or(u=='s'and c=='p'):
        return True
    
#Game play
if choice =='g':
    x=int(input(f"maximum number: "))
    guess(x)

elif choice =='cg':
    x=int(input(f"maximum number: "))
    computer_guess(x)
    
elif choice=='r':
    result=rockplay()
    print(result)





