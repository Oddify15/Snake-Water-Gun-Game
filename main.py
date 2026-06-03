import random 
#importing random module to generate a random choice by the computer

while True:
    computer=random.choice([-1,0,1])
    #the computer will choose between -1,0,1 randomly

    choice= input("Enter Your Choice: ")

    Dict={"Snake": 1, "Water":-1, "Gun":0}
    #Assigning Snake as 1. water as -1 and Gun as 0 through a dictionary in the form of {key:value}

    YourChoice=Dict[choice]
    #It will fetch the value after entering the "key"

    reversedict={1:"Snake",-1:"Water", 0:"Gun"}
    #It swaps the position of keys and values 
    #We have two variables now, our choice and computer


    print(f"You chose {reversedict[YourChoice]} \nComputer Chose {reversedict[computer]} ")
    #This will display our choice and computer's choice

    if (computer==YourChoice):
        print("The game is a tie")
    #This will result into the game being a tie 

    else:
    #Here, we make nested conditions
        if (computer==1 and YourChoice==-1):
            print("Snake drinks the Water. You lose!")

        elif (computer==1 and YourChoice==0):
            print("Gun shoots the Snake. You Win!")

        elif (computer==-1 and YourChoice==1):
            print("Snake drinks the Water. You win!")

        elif (computer==1 and YourChoice==0):
            print("The Gun drowns in the water. You lose!")

        elif (computer==0 and YourChoice==1):
            print("The Gun shoots the snake. You lose!")

        elif (computer==0 and YourChoice==-1):
            print ("The Gun Drowns in the Water. You win!")

    #After the program ends, It will lead us to a Thank you message along with a choice to restart or end the game 

    print("Thank You for Playing")

    restart=input("Play Again? Yes/No: ")

    if restart== "No" or restart=="N":
        print("Okay, Have a Nice Day")
        break

    elif restart=="Yes" or restart=="Y":
        print("Starting Again")