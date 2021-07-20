#uno main
import functions
import random

def main():
    print("uno game")
    print()
    cards = []
    for i in range(108):
        cards.append(i+1)

    num_of_players = int(input("how many players: "))
    
    p1 = []
    p2 = []
    p3 = []
    p4 = []

    
    discard = []
    isReverse = False

    cards, p1, p2, p3, p4 = functions.start_game(num_of_players, cards, p1, p2, p3, p4)
    

    current_card = random.randint(0, len(cards)-1)
    cards.pop(current_card)
    discard.append(current_card)
    player_turn = 1
    winner = False


    
    while (not winner):
        #print function
        functions.print_table(p1, p2, p3, p4, current_card)

        card_chosen = functions.player_inp(player_turn, num_of_players, p1, p2, p3, p4, current_card)

        cards, card_chosen, player_turn, p1, p2, p3, p4, current_card, winner, discard, isReverse = functions.play_card(cards, card_chosen, num_of_players, player_turn, p1, p2, p3, p4, current_card, winner, discard, isReverse)

    
        
        # no_winner = True
        # while (no_winner):
            #input function
            #if not in bounds do input function
            #logic function 
            #if logic is false do input function 
            #remove played card from player hand
            #play card function (should determine whos turn it is)
            #if p1 or p2 have 0 cards winner is awarded
            #else print function with new cards
        


        #print function (p1, p2, current card) 
        #input function ()
        #logic card function (current card, card played)
        #play card function (cards, card played, opponent, p1, p2)
        #print function
        #if deck runs out need to determine what to do later AFTER I FINISH EVERYTHING ELSE


if __name__ == '__main__':
    main()



