import random

game_running = True

computer_input_list = ["0","1","2","3","4","5","6","7","8","9"]
computer_input = random.sample(computer_input_list,4)

print(computer_input)
def player_1_input_validator(input):
    if not input.isdigit():
        print("please you must input a number")
        return False
    if len(input) != 4:
        print("please you must input a four digit number")
        return False
    if len(set(input)) != 4:
        print("please the numbers must be unique")
        return False

def human_input():  
    global player_1_input 
    player_1_input = input("Input a four digit number(no repition): ")

    while player_1_input_validator(player_1_input) == False:
        player_1_input = input("Input a four digit number(no repition): ")
    player_1_input = list(player_1_input)
    
def secret_code_comparison(human_input,computer_input):
    dead = sum(1 for i in range(4) if human_input[i] == computer_input[i])
    injured = sum(1 for digit in human_input if digit in computer_input) - dead

    if dead == 4:
        print("you gussed right")
        game_running == False
        
        
    print(f"{dead} Dead,{injured} Injured")




if game_running == True:
    human_input()
    secret_code_comparison(player_1_input,computer_input)

    
