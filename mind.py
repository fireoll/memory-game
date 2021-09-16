from os import system,name
from time import sleep
from playsound import playsound
import string
import random # define the random module
def clear():
    if(name=='nt'):
        _ = system('cls')
    else:
        _ =system('clear')

option=1
while(option==1):
    print("Please select your desired level")
    print("1.Beginner")
    print("2.Amateur")
    print("3.Professional")
    print("4.Expert")
    opt=int(input())
    if(opt==1):
        capable=30
    elif(opt==2):
        capable=40
    elif(opt==3):
        capable=50
    else:
        capable=60
    l=[]
    for i in range(capable):
        S = random.randint(2,4)
        l.append(''.join(random.choices(string.ascii_uppercase ,k = S)))
    for j in l:
        print(j)
    sleep(5)
    clear()
    r=input("Please enter the remebered words")
    r=r.split(" ")
    count=0
    for k in r:
        if k in l:
            count+=1
    if(count<(capable//2)):
        try:
            print("You need improvement")
            playsound(r"C:\python project\projects\fail-trombone-03.wav")
            sleep(5)
        except:
            pass

    else:
        try:
            print("Damn you are good")
            playsound(r"C:\python project\projects\applause-01.wav")
            sleep(5)

        except:
            pass
    clear()
    print("Please select the desired option:")
    print("1.Restart")
    print("2.Exit")
    option=int(input())