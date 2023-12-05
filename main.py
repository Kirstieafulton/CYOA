yes_no = ["yes", "no"]
directions = ["left", "right"]
home_help = ["home", "help"]

def setup():
  name = input("Do you remember your name, adventurer?\n")
  print("Thank goodness, " + name + ". You fell from the sky and have been here for a while!")
  print("You are in a dark forest, with many obstacles.")
  print("Can you find your way out?\n")
  game_start()

def game_start():
    response = ""
    while response not in yes_no:
      response = input("Would you like to head towards the River?\nyes/no\n")
      if response == "no":
        print("Phew.. that wouldn’t have been the best decision. You suddenly hear screaming miles ahead of you.\n")
        entry_point()
      elif response == "yes":
        print("Unfortunately on your way down to the river you tripped and fell in. The current was too strong and you were swept away. Farewell.. ")
        quit()
      else:
        print("I didn't understand that. Try again\n")

def entry_point():
    import random 
    number = random. randint(1,6) 
    game_limit = 2
    number_of_guesses = 0
    print("The screams get louder as you struggle through the forest..\n")
    print("On your way you see a dice and a piece of paper on a rock.\n")
    print("The instructions read: If you roll the dice and get the right answer you go towards the shouting.\n")
    print("If you roll the dice and it is the wrong answer you go towards the spider cave, where you will be eaten alive.\n")
    print("Roll the dice you have " + str(game_limit) + " tries")
    while number_of_guesses <= game_limit:
      guess = int(input())
      number_of_guesses += 1 
      if number_of_guesses == game_limit +1: 
        print("Sorry, you did not guess the number correctly. The number was " + str(number), "Please proceed to the spider cave, where you will be eaten alive")
        break
      elif guess == number: #== means compare
        print("You guessed correctly! Please follow the screams!")
        the_screams() 
      elif guess < number: #elseif
        print("too low")
      elif guess > number:
        print ("too high")
      else:
        break 

def the_screams():
  response = ""
  while response not in directions:
    response = input("You come to a crossroads. To your left you hear the screams and to your right you see a road. Do you turn left towards the screams or right towards the road?\nleft/right\n")
    if response == "left":
        print("You struggle through the forest until you find a young girl who is on her own. She is lost just like you. You pick her up and make your way back to the road where you are met by a car, that takes you both home!\n")
        quit()
    elif response == "right":
        print("You see a car. The car comes towards you and stops.\n")
        way_out()
    else:
        print("I didn't understand, please try again..\n")

def way_out():
  response = ""
  while response not in home_help:
    response = input("Do you ask him to help you find the person with the screams? Or do you ask him to take you home?\nhome/help\n")
    if response == "home":
      print("The driver says yes. However on your journey he takes a wrong turn and takes you back into the forest where he pushes you out the car, leaving you stranded. Game over.\n")
      quit()
    elif response == "help":
      print("He agrees. Jumps out the car and follows you into the forest. You follow the screams and find a young girl on her own. Both you and the driver bring her back to the car. The driver takes both of you home. Congrats!\n")
      quit()
    else:
      print("I didn't understand, please try again..\n")

setup()


    


 

