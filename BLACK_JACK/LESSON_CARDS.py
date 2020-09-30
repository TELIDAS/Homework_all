import random

def compare_results(player_list, computer_list, opens=False):
    if sum(player_list) > 21 and sum(computer_list) > 21:
        print("Draw")
        return True
    elif sum(player_list) > 21 and sum(computer_list) == 21:
        print(f"You loose-{sum(player_list)}! Computer score was {sum(computer_list)}")
        return True
    elif sum(computer_list) > 21 and sum(player_list) == 21:
        print(f"You win -{sum(player_list)}! Computer score was {sum(computer_list)}")
        return True
    else:
        if opens:
            if sum(player_list) > sum(computer_list):
                print(f"You loose-{sum(player_list)}! Computer score was {sum(computer_list)}")
        return False

def black_jack():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    computer = [random.choice(cards), random.choice(cards)]
    player = [random.choice(cards), random.choice(cards)]


    while True:
        print("choose an option")
        print("(1)Draw new card")
        print("(2)open your cards")
        print("(3)End The Game")
        print(f"your sum of cards -> {sum(player)}")
        choice = int(input("enter your choice: "))


        if choice == 1:
            player.append(random.choice(cards))
            computer.append(random.choice(cards))
            if compare_results(player, computer):
                break
            else:
                pass
        elif choice == 2:
            compare_results(player, computer, opens=True)
            break
        elif choice == 3:
            break
        else:
            print("wrong number!")

black_jack()