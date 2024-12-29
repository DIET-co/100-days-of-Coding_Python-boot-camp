def find_treasure():
  """Navigates the Treasure Island game and returns the outcome."""

  # First decision: left or right
  choice1 = input("Welcome to Treasure Island. Your mission is to find the treasure. \nLeft or right? ")
  if choice1.lower() == "left":
    # Second decision: swim or wait
    choice2 = input("Swim or wait? ")
    if choice2.lower() == "wait":
      # Third decision: red, blue, or yellow door
      choice3 = input("Which door? Red, blue, or yellow? ")
      if choice3.lower() == "yellow":
        return "You Win!"
      else:
        return "Game Over."
    else:
      return "Attacked by trout. Game Over."
  else:
    return "Fall into a hole. Game Over."
    
c=input("do u want to play a game yes or no:")

# Run the game
if(c.lower() == "yes"):
    outcome = find_treasure()
    print(outcome)




