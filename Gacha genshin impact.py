import random
import math

guarantee5 = 0
guarantee4 = 0
guaranteeayaka = False

def asterisk():
    for a in range(45):
        print("*",end="")
def dottedline():
    for a in range(112):
        print("-",end="")
def if1(p1):
    global guarantee5
    global guarantee4
    global guaranteeayaka
    if(p1 <= 6 ):
        if(guaranteeayaka == True):
            guaranteeaya()
        else:
            gara5()
    elif(p1 > 6 and p1 <= 57):
        gara4()
    else:
        print("3 star")
        guarantee5 += 1
        guarantee4 += 1
def guaranteeaya():
    global guaranteeayaka
    print("Ayaka")
    guaranteeayaka = False

def gara5():
    global guarantee5
    global guarantee4
    global guaranteeayaka
    guarantee5 = 0
    if(random.randint(0,2) == 0):
        print("Ayaka")
        guaranteeayaka = False
    else:
        guaranteeayaka = True
        print("5 star หลุดเรทว๊าย")

def gara4():
    global guarantee5
    global guarantee4
    guarantee4 = 0
    print("4 star")
    guarantee5 += 1
        


print()
asterisk()
print(" Ayaka 2nd Rerun Banner ",end="")
asterisk()
print()
print()
print(" ",end="")
dottedline()
print()
print("|                                                     Rate                                                       |")
print("|                                                                                                                |")
print("| 5-star : 0.6 % (Guaranteed at 90 times)                                                                        |")
print("| (When open 5 stars,50% chance to get Ayaka If the character that received 5 stars is not Ayaka The next 5-star |")
print("| character is guaranteed to be Ayaka.)                                                                          |")
print("|                                                                                                                |")
print("| 4-star : 5.1 % (Guaranteed at 10 times)                                                                        |")
print("|                                                                                                                |")
dottedline()



while(True):
    print()
    press50 = str(input("'exit' or 'play' : "))
    if(press50 == "exit"):
        break 
    elif(press50 == "play"):
        press = int(input("Enter the number of times to randomize (1 or 10) : "))

        if(press == 1 or press == 10):
            for c in range(press):
                if(guarantee5 == 89):
                    if(guaranteeayaka == True):
                        guaranteeaya()
                    else:
                        gara5()
                elif(guarantee4 == 9):

                    gara4()
                else:
                    p1 = random.randint(1,1000)
                    if1(p1)
            
