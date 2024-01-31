from art import logo, vs
from game_data import data
from random import randint
from replit import clear


choice_one = randint(0, len(data)-1)
choice_two = randint(0, len(data)-1)
while choice_two == choice_one:
    choice_two = randint(0, len(data)-1)
available_choices = [choice_one, choice_two]
   


def selection(option):
    if option == 'A':
        your_selection = choice_one
        other_selection = choice_two
    elif option == 'B':
        your_selection = choice_two
        other_selection = choice_one
    return your_selection, other_selection


# print(your_selection, data[your_selection]['follower_count'])
# print(other_selection, data[other_selection]['follower_count'])


print(logo)

continue_game = True
score = 0
while continue_game:
    # print(f"{data[choice_one]['follower_count']}")
    print(f"Compare A: {data[choice_one]['name']}, a {data[choice_one]['description']}, from {data[choice_one]['country']}.")
    print(vs)
    # print(f"{data[choice_two]['follower_count']}")
    print(f"Compare B: {data[choice_two]['name']}, a {data[choice_two]['description']}, from {data[choice_two]['country']}.")
    my_option = input("Who has more followers? Type 'A' or 'B':\n").upper()
    while my_option != 'A' and my_option != 'B':
        my_option = input("Please choose again.").upper()
    your_selection, other_selection = selection(my_option)
    if data[your_selection]['follower_count'] > data[other_selection]['follower_count']:
        score += 1
        clear()
        print(f"You're right. Current score: {score}")
        choice_one = choice_two
        choice_two = randint(0, len(data)-1)
        while choice_two ==  choice_one:
            choice_two = randint(0, len(data)-1)
    elif data[your_selection]['follower_count'] < data[other_selection]['follower_count']:
        clear()
        print(f"Sorry, that's wrong. Final score: {score}")
        continue_game = False

