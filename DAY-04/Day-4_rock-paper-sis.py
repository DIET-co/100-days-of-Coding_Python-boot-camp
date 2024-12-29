import random
rock =  '''
      ------
-----'  _____)
       (_______)
       (______)
       (_____)
---,__(____)      

'''
paper = '''
      ------____
-----'      _____)__
            (_______)
              (______)
              (_____)
---,________(____)    

'''
scissors = ''' 

     --------
 ---'      ___)_____
            ________)
          __________)
       (_____)
---,___(_____)

'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissor"))
if user_choice >= 0 and user_choice <=2:
    print(game_images[user_choice])
    
computer_choice = random.randint(0, 2)
if computer_choice >= 0 and computer_choice <=2:
   print(game_images[computer_choice])

print(f"Computer chose{computer_choice}")

if user_choice >= 3 or user_choice < 0:
    print("invalid input")
elif user_choice == 0 and computer_choice == 2:
    print("you win")
elif computer_choice == 0 and user_choice ==2:
    print("you lose")      
elif computer_choice > user_choice:
    print("you lose")
elif user_choice > computer_choice:
    print("youwin") 
elif computer_choice == user_choice:
    print("draw")
           


