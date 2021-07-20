#uno game
import random

#card type determines what the card is
def card_type(card):
    color = ""
    if (card <= 25 or card == 110 or card == 114):
        color += "blue "
    elif (card <= 50 or card == 111 or card == 115):
        color += "green "
    elif (card <= 75 or card == 112 or card == 116):
        color += "red "
    elif (card <= 100 or card == 113 or card == 117):
        color += "yellow "
    else:
        color += "wild "
    
    if (card >= 114):
        color += "wild"
        return color

    
    if (card <= 100):
        type = card % 25
        
        if (type <= 19 and card % 25 != 0):
            num = type // 2 
        
            color += str(num)

        else:
            type -= 20
            num = type // 2

            if (card % 25 == 0):
                color += "+2"
            elif (num == 0):
                color += "skip"
            elif (num == 1):
                color += "reverse"
            elif (num == 2):
                color += "+2"

    else:
        wild_type = card - 100

        if (wild_type <= 4):
            color += "card"
        else:
            color += "+4"

    return color

def current_turn(num_of_players, player_turn):
    if (num_of_players == 2):
        if (player_turn % 2 == 1):
            player = "p1"
        else:
            player = "p2"
    elif (num_of_players == 3):
        if(player_turn % 3 == 1):
            player = "p1"
        elif (player_turn % 3 == 2):
            player = "p2"
        else:
            player = "p3"
    else:
        if (player_turn % 4 == 1):
            player = "p1"
        elif (player_turn % 4 == 2):
            player = "p2"
        elif (player_turn % 4 == 3):
            player = "p3"
        else:
            player = "p4"
    
    return player

def new_deck(cards, discard):
    if (len(cards) == 0):
        temp = discard[len(discard)-1]
        discard.pop(len(discard)-1)
        cards = discard
        discard = []
        discard.append(temp)
    
    return cards, discard

#start_game function
def start_game(num_of_players, cards, p1, p2, p3, p4):
    for i in range(7):
        rand_int = random.randint(0, len(cards)-1)
        p1.append(cards[rand_int])
        cards.pop(rand_int)
    for i in range(7):
        rand_int = random.randint(0, len(cards)-1)
        p2.append(cards[rand_int])
        cards.pop(rand_int)
    
    if (num_of_players >= 3):
        for i in range(7):
            rand_int = random.randint(0, len(cards)-1)
            p3.append(cards[rand_int])
            cards.pop(rand_int)

    if (num_of_players == 4):
        for i in range(7):
            rand_int = random.randint(0, len(cards)-1)
            p4.append(cards[rand_int])
            cards.pop(rand_int)
    
    return cards, p1, p2, p3, p4


#logic function
def can_play(current_card, playing_card):
    c1 = card_type(current_card)
    c2 = card_type(playing_card)
    c1_split = c1.split()
    c2_split = c2.split()

    if (c2_split[0] == "wild"):
        return True
    if (c1_split[0] == c2_split[0]):
        return True
    if (c1_split[1] == c2_split[1]):
        return True

    return False
    
#print function
def print_table(p1, p2, p3, p4, current_card):

    print("p1 cards")
    for i in range(len(p1)):
        print(str(i) + " " + card_type(p1[i]))
    
    print()
    print("p2 cards")
    for i in range(len(p2)):
        print(str(i) + " " + card_type(p2[i]))

    if (len(p3) > 0):
        print()
        print("p3 cards")
        for i in range(len(p3)):
            print(str(i) + " " + card_type(p3[i]))
    
    if (len(p4) > 0):
        print()
        print("p4 cards")
        for i in range(len(p4)):
            print(str(i) + " " + card_type(p4[i]))

    print()
    print ("-1 draw a card")

    print()
    print("current card: " + card_type(current_card))





#play card function
#TODO implement discard function
def play_card(cards, card_played, num_of_players, player_turn, p1, p2, p3, p4, current_card, winner, discard, isReverse):

    player = current_turn(num_of_players, player_turn)

    if (card_played == -1):
        if (player == "p1"):
            draw_card = random.randint(0, len(cards)-1)
            cards.pop(draw_card)
            p1.append(draw_card)
        elif (player == "p2"):
            draw_card = random.randint(0, len(cards)-1)
            cards.pop(draw_card)
            p2.append(draw_card)
        elif (player == "p3"):
            draw_card = random.randint(0, len(cards)-1)
            cards.pop(draw_card)
            p3.append(draw_card)
        else:
            draw_card = random.randint(0, len(cards)-1)
            cards.pop(draw_card)
            p4.append(draw_card)
        
        new_deck(cards, discard)
        
        if (isReverse == False):
            player_turn += 1
        else:
            player_turn -= 1

        return cards, card_played, player_turn, p1, p2, p3, p4, current_card, winner, discard, isReverse

    else:

        card_str = card_type(card_played)
        card_str = card_str.split()
        #color = card_str[0]
        type = card_str[1]
    
        #print(color)
        #print(type)

        #remove card from player hand
    
        if (player == "p1"):
            p1.remove(card_played)
            discard.append(card_played)
            if (len(p1) == 0):
                winner = True
                print("p1 won")
        
        elif (player == "p2"):
            p2.remove(card_played)
            discard.append(card_played)
            if (len(p2) == 0):
                winner = True
                print("p2 won")
        
        elif (player == "p3"):
            p3.remove(card_played)
            discard.append(card_played)
            if (len(p3) == 0):
                winner = True
                print("p3 won")
        
        else:
            p4.remove(card_played)
            discard.append(card_played)
            if (len(p4) == 0):
                winner = True
                print("p4 won")

        
        #change current card
        current_card = card_played

        #draw 2
        if (type == "+2"):
            print("draw 2!!!")
            if (isReverse == False):

                player_turn += 1
            else:
                player_turn -= 1

            card1 = random.randint(0, len(cards)-1)
            cards.pop(card1)

            new_deck(cards, discard)

            card2 = random.randint(0, len(cards)-1)
            cards.pop(card2)

            new_deck(cards, discard)

            player = current_turn(num_of_players, player_turn)
            if (player == "p1"):
                p1.append(card1)
                p1.append(card2)
            elif (player == "p2"):
                p2.append(card1)
                p2.append(card2)
            elif (player == "p3"):
                p3.append(card1)
                p3.append(card2)
            else:
                p4.append(card1)
                p4.append(card2)
            
            if (isReverse == False):

                player_turn += 1
            else:
                player_turn -= 1
        
        elif (type == "skip"):
            print("SKIP !!!")
            if (isReverse == False):

                player_turn += 2
            else:
                player_turn -= 2
        
        elif (type == "reverse"):
            print("REVERSE !!!")
            if (num_of_players == 2):
                player_turn += 2
            else:
                if (isReverse == False):
                    isReverse = True
                    player_turn -= 1
                else:
                    isReverse = False
                    player_turn += 1

        
        #TODO draw 4 wild card
        elif (type == "+4"):
            print("DRAW 4!!!")
            card1 = random.randint(0, len(cards)-1)
            cards.pop(card1)
            new_deck(cards, discard)
            card2 = random.randint(0, len(cards)-1)
            cards.pop(card2)
            new_deck(cards, discard)
            card3 = random.randint(0, len(cards)-1)
            cards.pop(card3)
            new_deck(cards, discard)
            card4 = random.randint(0, len(cards)-1)
            cards.pop(card4)
            new_deck(cards, discard)

            if (isReverse == False):

                player_turn += 1
            else:
                player_turn -= 1

            player = current_turn(num_of_players, player_turn)


            if (player == "p1"):
                p1.append(card1)
                p1.append(card2)
                p1.append(card3)
                p1.append(card4)
            elif (player == "p2"):
                p2.append(card1)
                p2.append(card2)
                p2.append(card3)
                p2.append(card4)
            elif (player == "p3"):
                p3.append(card1)
                p3.append(card2)
                p3.append(card3)
                p3.append(card4)
            else:
                p4.append(card1)
                p4.append(card2)
                p4.append(card3)
                p4.append(card4)
            
            inp = input("what color would you like: ")
            if (inp == "blue"):
                current_card = 110 #blue +4
            elif (inp == "green"):
                current_card = 111 #green +4
            elif (inp == "red"):
                current_card = 112 #red +4
            elif(inp == "yellow"):
                current_card = 113 #yellow +4

            if (isReverse == False):

                player_turn += 1
            else:
                player_turn -= 1
            

        #TODO wild card
        elif (type == "card"):
            inp = input("what color would you like: ")
            if (inp == "blue"):
                current_card = 114 #blue wild
            elif (inp == "green"):
                current_card = 115 #green wild
            elif (inp == "red"):
                current_card = 116 #red wild
            elif(inp == "yellow"):
                current_card = 117 #yellow wild

            if (isReverse == False):

                player_turn += 1
            else:
                player_turn -= 1

        else:

            if (isReverse == False):

                player_turn += 1
            else:
                player_turn -= 1


    return cards, card_played, player_turn, p1, p2, p3, p4, current_card, winner, discard, isReverse


def player_inp(player_turn, num_of_players, p1, p2, p3, p4, current_card):
    
    player = current_turn(num_of_players,player_turn)
    
    logical = False

    while (not logical):
    
        inp = int(input(player + " choose a card (-1 for draw a card): "))
        if (player == "p1"):
            while (inp < -1 or inp > len(p1)-1):
                print("invalid index!!!")
                inp = int(input(player + " choose a card (-1 for draw a card): "))
        if (player == "p2"):
            while(inp < -1 or inp > len(p2)-1):
                print("invalid index!!!")
                inp = int(input(player + " choose a card (-1 for draw a card): "))
        if (player == "p3"):
            while(inp < -1 or inp > len(p3)-1):
                print("invalid index!!!")
                inp = int(input(player + " choose a card (-1 for draw a card): "))
        if (player == "p4"):
            while(inp < -1 or inp > len(p4)-1):
                print("invalid index!!!")
                inp = int(input(player + " choose a card (-1 for draw a card): "))
        
        if (num_of_players == 2):
            if (player_turn % 2 == 1):
                card_chosen = p1[inp]
            else:
                card_chosen = p2[inp]
        elif (num_of_players == 3):
            if(player_turn % 3 == 1):
                card_chosen = p1[inp]
            elif (player_turn % 3 == 2):
                card_chosen = p2[inp]
            else:
                card_chosen = p3[inp]
        else:
            if (player_turn % 4 == 1):
                card_chosen = p1[inp]
            elif (player_turn % 4 == 2):
                card_chosen = p2[inp]
            elif (player_turn % 4 == 3):
                card_chosen = p3[inp]
            else:
                card_chosen = p4[inp]
        
        if (inp == -1):
            return inp
        else:
            logical = can_play(current_card, card_chosen)
            if (not logical):
                print("invalid card, choose another card")
    
    return card_chosen
    

    

#assume both players are human


#p1 = odd count p2 = even count

#need a option for draw card
#should make a def for interface
#need to add saying "uno"
#better variable names











