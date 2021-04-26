from war_classes import *
from time import sleep

p1 = Player("P1")
p2 = Player("P2")

game_deck = Deck()
game_deck.shuffle()

# Split deck between players
for card in range(26):
    p1.add_cards(game_deck.deal_one())
    p2.add_cards(game_deck.deal_one())

playing_game = True
round_count = 0

while playing_game:

    #Display current round
    round_count+=1
    print(f"Round {round_count}")

    #Check win conditions, break out of loop if reached
    if len(p1.all_cards) == 0:
        print("Player 2 wins, player 1 has no cards")
        playing_game = False
        break

    if len(p2.all_cards) == 0:
        print("Player 1 wins, player 2 has no cards")
        playing_game = False
        break

    # Set/reset the hand of both players to zero cards and draw one for each
    p1_cards = []
    p1_cards.append(p1.remove_one())

    p2_cards = []
    p2_cards.append(p2.remove_one())

    #Check for round win condtions/war
    at_war = True

    while at_war:
        print(f"Player 1 has a {p1_cards[-1].rank}")
        print(f"Player 2 has a {p2_cards[-1].rank}")

        if p1_cards[-1].value > p2_cards[-1].value:
            p1.add_cards(p1_cards)
            p1.add_cards(p2_cards)
            print("Player 1 wins the round")
            at_war = False
            sleep(1)
            print("\n\n")

        elif p2_cards[-1].value > p1_cards[-1].value:
            p2.add_cards(p1_cards)
            p2.add_cards(p2_cards)
            print("Player 2 wins the round")
            at_war = False
            sleep(1)
            print("\n\n")

        # Going to war
        else:
            print("War!")
            #Check if both players afford to go to war
            if len(p1.all_cards) < 10:
                print("Player 2 wins, player 1 couldn't go to war")
                playing_game = False
                break

            if len(p2.all_cards) < 10:
                print("Player 1 wins, player 2 couldn't go to war")
                playing_game = False
                break

            #Each player draws 10 more cards
            else:
                for x in range(10):
                    p1_cards.append(p1.remove_one())
                    p2_cards.append(p2.remove_one())