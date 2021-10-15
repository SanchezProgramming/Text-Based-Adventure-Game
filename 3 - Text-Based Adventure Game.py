
def userDecision(givenUserInput):

      while (givenUserInput != 3):

            if (givenUserInput == 1):
                  print("You won't reach the person in time!\n")

            elif (givenUserInput == 2):
                  print("The ladder won't reach that far!\n")

            else:
                  print("Please choose between 1-3\n")

            givenUserInput = int(input("What do you do? "))

      print("Awesome! You saved that person!\n")



def startStory():
      print("One day you go to sleep and then suddenly\n"
            "you wake up in another person's body.\n"
            "And then you realize you are now SPIDER-MAN!\n")

      print("Anyways...after you figured out how to web sling\n"
            "and helped a grandma cross the street.\n")

      print("You see that there is a burning building\n"
            "and there are people trapped inside.")

      print("\n=========================\n"
            "Objective: SAVE THEM!"
            "\n=========================\n")



def Objective1():
      print("\n=======================================")
      print("Objective 1: There is a person yelling\n"
            "for help on the 5th floor.\n")

      print("How can you help them:")
      print("1) Climb up the wall")
      print("2) Use a ladder")
      print("3) Web sling to the 5th floor and\n"
            "take the person down to safety.")

      userInput1 = int(input("\nChoose between 1-3: "))

      userDecision(userInput1)



def Objective2():
      print("\n=============================================")
      print("Objective 2: You hear a child yelling for help.\n"
            "You find the child on the 2nd floor\n"
            "and across the hall you see fire standing\n"
            "between you and the child.\n")

      print("How can you help them:")
      print("1) Wait for the fire to stop")
      print("2) Wait for the firefighters")
      print("3) Grab a fire extinguisher and put out the fire\n"
            "and take the child to safety.\n")

      userInput2 = int(input("Choose between 1-3: "))

      userDecision(userInput2)



def main():

      startStory()

      Objective1()

      Objective2()

      print("After rescuing everyone successfully. The fire\n"
            "fighters came to put out the fire.\n"
            "After heading back home, and night time comes.\n"
            "You decide to get some sleep and\n"
            "the next morning you are back in your regular body.\n\n")


      print("THE END!\nThank you for playing.")

main()