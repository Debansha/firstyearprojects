
'''
1.Ask the useer to make a choice
2. If choice is not valid
3. Print an error
4. let the computer to make a choice
5. print choices(emojis)
6.determine the winner
7.ask the user if they want to continue
8. if not
9.terminate
'''


import random
emojis = {'r': '🪨',  's': '✂️','p': '📄'}
choices= ('r','p','s')

while True:
        user_choice = input('Rock,paper or scissors ? (r/p/s):- ').lower()
        computer_choice= random.choice(choices)

        if user_choice not in choices:
            print('Invalid choice!')
            continue

        print(f'You chose {emojis[user_choice]}')
        print(f'Computer chose {emojis[computer_choice]}')

        if user_choice == computer_choice:
            print('Tie')
        elif( 
            (user_choice =='r'and computer_choice == 's') or 
            (user_choice =='s' and computer_choice == 'p') or
            (user_choice =='p' and computer_choice == 'r')):
           print('You win')

        else:
           print('You lose')

        should_continue = input ('Continue? (y/n):').lower()
        if should_continue == 'n':
           break



  
