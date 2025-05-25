'''
1.LOOP
2.ASK: roll the dice?
3.if user enters y
4.generates two random numbers
5.print them
6.if user enters n
7.print thank u msg
8.else 
9.print invalid choice # 
10. track of how many times the
11.Ask how many times to roll
'''
import random
rolls = int(input("How many times do you want to roll the dice? "))
count = 0
while True:
    choice = input('Roll the dice?(y/n):').lower()
    if choice =='y':
        die1= random.randint(1,6)
        die2= random.randint(1,6)
        print(f'({die1},{die2})')
        count +=1
        print(f"Roll count so far: {count}") 
    elif choice == 'n':
        print ('Thankks for playing!')
        count +=1
        print(f"Roll count so far: {count}") 
        break
    else:
        print('Invalid Choice!')
        print(f"Roll count so far: {count}") 

