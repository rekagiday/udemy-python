print("****  ROCK  ****  PAPER  **** SCISSORS  **** \n  r = rock, p = paper, s = scissors")
name1 = input('Player1 name:')
name2 = input('Player2 name:')

p1 = input(name1+ ", make your choice:")
if (p1 and p1 == 'r' or p1 == 'p' or p1 == 's'):
    print("Thank you!")
    p2 = input(name2+ ', make your choice:')
    if (p2 and p2 == 'r' or p2 == 'p' or p2 == 's'):
        print("Thank you!")
        if (p1 == p2):
            print("Tie!")
        elif(p1 == 'r' and p2 == 's') or (p1 == 'p' and p2 == 'r') or (p1 == 's' and p2 == 'p'):
            print(name1+' wins!')
        elif(p1 == 'r' and p2 == 'p') or (p1 == 'p' and p2 == 's') or (p1 == 's' and p2 == 'r'):
            print(name2 + ' wins!')
    else:
        print('Please enter a valid answer (r, p or s)')
else:
    print('Please enter a valid answer (r, p or s)')
