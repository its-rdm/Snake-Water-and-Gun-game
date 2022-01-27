import random

def gameWin(comp,me):
    if comp==me:
        return None
    elif comp == 's':
        if me=='w':
            return False
        else:
            return True
    elif comp=='w':
        if me == 'g':
            return False
        else:
            return True
            
    elif comp=='g':
        if me == 's':
            return False
        else:
            return True


print("Computer's Turn : Snake(s) Water(w) or Gun(g) ?")
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'
me=input("Your Turn : Snake(s) Water(w) or Gun(g)?")
a=gameWin(comp,me)

print(f"Computer chose {comp}")
print (f"you chose {me}")

if a == None:
    print("Tie!")
elif a:
    print ("You win")
else:
        print("you lose")