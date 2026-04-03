import random

count = 0   

while True:   
    n = int(input(
        "enter choice\n"
        "1. rock\n"
        "2. paper\n"
        "3. scissor\n"
        "4. exit\n"
    ))

    if n == 4:
        print("Game Over")
        break

    m = ['rock', 'paper', 'scissor']

    comp = random.choice(m)  
    
    if n == 1:
        user = 'rock'
    elif n == 2:
        user = 'paper'
    elif n == 3:
        user = 'scissor'
    else:
        print("invalid choice")
        continue

    print("Computer chose:", comp)

    
    if user == comp:
        print("tie")

    elif user == 'rock' and comp == 'paper':
        print("computer win")
        count += 1

    elif user == 'rock' and comp == 'scissor':
        print("user win")
        count += 1

    elif user == 'scissor' and comp == 'paper':
        print("user win")
        count += 1

    elif user == 'scissor' and comp == 'rock':
        print("computer win")
        count += 1

    elif user == 'paper' and comp == 'rock':
        print("user win")
        count += 1

    elif user == 'paper' and comp == 'scissor':
        print("computer win")
        count += 1

    print("Score:", count)