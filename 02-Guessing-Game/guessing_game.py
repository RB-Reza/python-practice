import random
name=input('what is your name : ')
a=1
b=99
guess=random.randint(a,b)
print(guess)
x=input('Is my guess higher(H), lower (L),or correct (C) ')
while x!='C':
    if x=='H':
        a=guess+1
        guess=random.randint(a,b)
        print(guess)
        x=input('is my guess higher (H),lower (L),or correct (C) ')
    elif x=='L': 
        b=guess-1
        guess=random.randint(a,b)
        print(guess)
        x=input('is my guess higher (H),lower (L),or correct (C) ')
    else:
        print('please enter H, L, or C')
        x=input('is my guess higher (H),lower (L),or correct (C) ')
print('wow I guessed it! Great job',name)

    
  
    
 
