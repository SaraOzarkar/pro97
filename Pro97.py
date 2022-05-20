import random

secretnumber= random,random.randint(0,10)


chances=0

while(chances<3):
   guess_number=int(input('Guess the Number'))

    if(guess_number===secretnumber):
      print('YOU WON THE GAME')
       break
    elif(guess_number>secretnumber):
     print('THE NUMBER IS LOWER')
    else:
       print('THE NUMBER IS BIGGER')
       chances +=1
