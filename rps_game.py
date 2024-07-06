import random
li=["rock","paper","scissor"]
again=True
while(again==True):
    user=input("Enter your choice? rock/paper/scissor\n")
    com=random.choice(li)
    print(com)
    if user==com:
        print("Draw match")
    elif user=='rock' and com=='paper' or user=='paper' and com=='scissor' or user=='scissor' and com=='rock':
        print("You lost")
    elif user=='rock' and com=='scissor' or user=='paper' and com=='rock' or user=='scissor' and com=='paper':
        print("You won")
    choice=input("Do you want to play again? enter y for yes and n for no: ")
    if choice=='n':
        again=False