import random

invalid = "Invalid number."
low = "Too low number."
high = "Too high number."
card_names = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

def Main():
    stop = False
    defpl = True
    while(not stop):
        ClearScreen()
        print("BLACKJACK - Original\n\n")
        if(defpl):
            players = Players()
            defpl = False
        print("\n\nMAIN MENU\n\n1. Players vs dealer-bot\n2. Players vs dealer-player\n3. Rules\n4. Re-define players\n5. Exit")
        answer = CheckValues(1, 5, low, high)
        if(answer == 1):
            ClearScreen()
            PvB(players)
        elif(answer == 2):
            ClearScreen()
            PvP(players)
        elif(answer == 3):
            ClearScreen()
            Rules()
        elif(answer == 4):
            defpl = True
        else:
            print("\nAre you sure?\n1. Yes\n2. No")
            answer = CheckValues(1, 2, invalid, invalid)
            if(answer == 1):
                stop = True

def Menu():
    print("\nPress ENTER to return to the menu")
    input()

def EndOfGame(players, data, mode):
    print("\n\nPress ENTER to continue")
    input()
    ClearScreen()
    print("Players' money:\n")
    if(mode == "PvB"):
        for player in range(len(players)):
            print("{}: {}$".format(players[player], data[player][8]))
    else:
        for player in range(len(players) - 1):
            print("{}: {}$".format(players[player + 1], data[player + 1][8]))
    Menu()

def ClearScreen():
    for i in range(30):
        print("\n")

def CheckType(answer):
    integer = False
    while(not integer):
        try:
            answer = int(answer)
            integer = True
        except ValueError:
            integer = False
            print("Answer must be an integer. Try again!")
            answer = input()
    return answer

def CheckValues(low, high, message_low, message_high):
    answer = CheckType(input())
    if(high == -1):
        while(answer < low):
            if(answer < low):
                print(message_low, "Try again!")
                answer = CheckType(input())
    else:
        while(answer < low or answer > high):
            if(answer < low):
                print(message_low, "Try again!")
                answer = CheckType(input())
            elif(answer > high):
                print(message_high, "Try again!")
                answer = CheckType(input())
    return answer

def Players():
    names = []
    print("Number of players: ")
    number = CheckValues(1, -1, "At least one player must join the game!", "")
    print("\nType the name of every player.")
    for i in range(number):
        names.append(input("Player {}: ".format(i + 1)))
    ClearScreen()
    return names

def PlayerData(players, mode):
    player_data = []
    for player in range(len(players)):
        current_player = []
        current_player.append(players[player])
        if(mode == "PvB" or player > 0):
            print("\n{} bet ($):".format(players[player]))
            current_player.append(CheckValues(2, 500, low, high))
        else:
            current_player.append(0)
        current_player.append(0)
        current_player.append([])
        current_player.append([])
        current_player.append(11)
        current_player.append(0)
        current_player.append(0)
        current_player.append(-current_player[1])
        player_data.append(current_player)        
    return player_data

def CardChoose(card_deck):
    temp_list = []
    for card in range(13):
        if(card_deck[card] > 0):
            temp_list.append(card)
    if(temp_list == []):
        return 0
    else:
        number = random.randint(0, len(temp_list) - 1)
        choose = temp_list[number] + 1
        return choose    

def PvB(players):
    print("Welcome to PvB! In this game, the dealer is a robot. A human can\nalso be the dealer in the PvP mode. Do you wish to continue?\n")
    print("1. Continue\n2. Switch mode")
    answer = CheckValues(1, 2, invalid, invalid)
    if(answer == 1):
        ClearScreen()
        Bets()
        player_data = PlayerData(players, "PvB")
        dealer_data = [[], 0]
        card_deck = []
        for i in range(13):
            card_deck.append(4)
        ClearScreen()
        for i in range(2):
            if(i == 0):
                print("Now, the dealer will give a card to each player...\n")
            else:
                print("\n\nPress ENTER to continue")
                input()
                ClearScreen()
                print("Again, the dealer will give a second card to each player but his\ncard will be hidden.\n")
            for player in range(len(players)):
                choose = CardChoose(card_deck)
                print("{}: {}\n".format(players[player], card_names[choose - 1]))
                if(choose == 1):
                    print("{}, you took an ace. By default, the first ace counts for 11 but if you\nexceed 21 in total count, you can count it as 1. Note that if you\ntake 2 aces, they count for 1 and 11 respectively.\n".format(players[player]))
                    player_data[player][6] += player_data[player][5]
                    if(player_data[player][5] == 11):
                        player_data[player][5] = 1
                    else:
                        player_data[player][5] = 11
                elif(choose <= 9):
                    player_data[player][6] += choose
                else:
                    player_data[player][6] += 10
                player_data[player][3].append(card_names[choose - 1])
                card_deck[choose - 1] -= 1
            choose = CardChoose(card_deck) # ----------
            if(i == 0):
                print("Dealer: {}".format(card_names[choose - 1]))
            else:
                print("Dealer: Hidden card")
            if(choose == 1):
                dealer_data[1] += 11
            elif(choose <= 9):
                dealer_data[1] += choose
            else:
                dealer_data[1] += 10
            dealer_data[0].append(card_names[choose - 1])
            card_deck[choose - 1] -= 1
        print("\n\nPress ENTER to continue")
        input()
        ClearScreen()
        if(dealer_data[0][0] == "Ace"):
            print("The dealer's first card is an ace. Bet for insurance?\n")
            print("1. Continue\n2. Learn more about insurance")
            answer = CheckValues(1, 2, invalid, invalid)
            if(answer == 2):
                Insurance()
                print("\n\nPress ENTER to continue")
                input()
            for player in range(len(players)):
                print("\n{}, place a bet from 0$ to {}$:".format(players[player], player_data[player][1]//2))
                player_data[player][2] = CheckValues(0, player_data[player][1]//2, low, high)
                player_data[player][8] -= player_data[player][2]
        if(dealer_data[0][0] == "Ace" or dealer_data[0][0] == "Ten" or dealer_data[0][0] == "Jack" or dealer_data[0][0] == "Queen" or dealer_data[0][0] == "King"):
            print("\n\nThe dealer will see if he has a blackjack...\n")
            if(dealer_data[1] == 21):
                print("\n\nBLACKJACK!!!\n")
                for player in range(len(players)):
                    print("The game ends. The players who placed a bet for insurance will\ntake back double the ammount. Players who also have a blackjack will take their initial bets back.\n")
                    player_data[player][8] += 2*player_data[player][2]
                    if(player_data[player][6] == 21):
                        player_data[player][8] += player_data[player][1]
                EndOfGame(players, player_data, "PvB")
                return
                if(dealer_data[0][0] == "Ace"):
                    print("The hidden card was a ten-card, so the dealer won a 'blackjack'.\n\nAll players loose their initial bets. If any player placed a bet\nfor insurance, he will get back double their insurance.")
                else:
                    print("The hidden card was an ace, so the dealer won a 'blackjack'.\n\nAll players loose their initial bets.")
                EndOfGame(players, player_data, "PvB")
                return
            else:
                print("\n\nThe dealer doesn't have a blackjack.\n")
            print("\n\nPress ENTER to continue")
            input()
        for player in range(len(players)):
            savage = 0
            doubled = False
            stop = False
            ClearScreen()
            print(players[player], "plays now!\n")
            if(player_data[player][6] >= 9 and player_data[player][6] <= 11):
                print("{}, your total is {}. You can double your bet if you want.\n".format(players[player], player_data[player][6]))
                print("1. Double down\n2. Learn more about doubling")
                answer = CheckValues(1, 2, invalid, invalid)
                if(answer == 2):
                    Doubling()
                    print("Double down?\n")
                    print("1. Yes\n2. No")
                    answer = CheckValues(1, 2, invalid, invalid)
                if(answer == 1):
                    doubled = True
                    player_data[player][8] -= player_data[player][1]
                    player_data[player][1] *= 2
                    print("\n{}, you doubled your bet. Total bet: {}$\n".format(players[player], player_data[player][1]))
                print("\nPress ENTER to continue\n")
                input()
            if(player_data[player][3][0] == player_data[player][3][1]):
                if(player_data[player][3][0] != "Five" or not doubled):
                    print("{}, you have 2 similar cards. Do you want to split pairs?\n".format(players[player]))
                    print("1. Split pairs\n2. Learn more about splitting pairs")
                    answer = CheckValues(1, 2, invalid, invalid)
                    if(answer == 2):
                        Splitting()
                        print("Split pairs?\n")
                        print("1. Yes\n2. No")
                        answer = CheckValues(1, 2, invalid, invalid)
                    if(answer == 1):
                        player_data[player][4].append(player_data[player][3][1])
                        del(player_data[player][3][1])
                        player_data[player][8] -= player_data[player][1]
                        print("\n{}, you split pairs and doubled your bet.\n\nPress ENTER to continue".format(players[player]))
                        input()
                        for i in range(2):
                            ClearScreen()
                            if(i == 0):
                                print("Left hand play:\n\n")
                            else:
                                print("Right hand play:\n\n")
                            player_data[player][5] = 11
                            player_data[player][i + 6] = card_names.index(player_data[player][i + 3][0]) + 1
                            savage = 0
                            stop = False
                            print("Your cards: {}\nYour total: {}\n".format(player_data[player][i + 3], player_data[player][i + 6]))
                            while(stop == False):
                                print("\n{}, do you want to take a card?".format(players[player]))
                                print("1. Take a card\n2. Stand")
                                answer = CheckValues(1, 2, invalid, invalid)
                                if(answer == 1):
                                    if(player_data[player][i + 3] == "Ace"):
                                        stop = True
                                    choose = CardChoose(card_deck)
                                    print("\n\n{}: {}".format(players[player], card_names[choose - 1]))
                                    if(choose == 1):
                                        print("\n{}, you took an ace. By default, the first ace counts for 11 but if you\nexceed 21 in total count, you can count it as 1. Note that if you\ntake 2 aces, they count for 1 and 11 respectively.\n".format(players[player]))
                                        player_data[player][i + 6] += player_data[player][5]
                                        if(player_data[player][5] == 11):
                                            player_data[player][5] = 1
                                        else:
                                            player_data[player][5] = 11
                                    elif(choose <= 9):
                                        player_data[player][i + 6] += choose
                                    else:
                                        player_data[player][i + 6] += 10
                                    player_data[player][i + 3].append(card_names[choose - 1])
                                    card_deck[choose - 1] -= 1
                                    print("Your cards: {}\nYour total: {}\n".format(player_data[player][i + 3], player_data[player][i + 6]))
                                    if(player_data[player][i + 6] > 21):
                                        if(player_data[player][i + 3].count("Ace") == 1 and savage == 0):
                                            print("\nYou exceeded 21. However, you have an ace counting as 11, so you can\ncount it as 1 and continue playing.")
                                            player_data[player][i + 6] -= 10
                                            player_data[player][5] = 11
                                            savage = 1
                                        else:
                                            print("\nBUST!!!")
                                            stop = True
                                else:
                                    print("\nYou stand.")
                                    stop = True
                            if(i == 0):
                                print("\n\nPress ENTER to continue\n")
                                input()
            elif(player_data[player][6] == 21):
                print("{}, you have a BLACKJACK!!! The dealer pays you 1,5 times your bet!".format(players[player]))
                player_data[player][8] += int(0.5*player_data[player][1])
                stop = True
            if(not stop):
                print("Your cards: {}\nYour total: {}\n".format(player_data[player][3], player_data[player][6]))
            while(stop == False):
                print("\n{}, do you want to take a card?".format(players[player]))
                print("1. Take a card\n2. Stand")
                answer = CheckValues(1, 2, invalid, invalid)
                if(answer == 1):
                    if(doubled):
                        stop = True
                    choose = CardChoose(card_deck)
                    print("\n\n{}: {}".format(players[player], card_names[choose - 1]))
                    if(choose == 1):
                        print("\n{}, you took an ace. By default, the first ace counts for 11 but if you\nexceed 21 in total count, you can count it as 1. Note that if you\ntake 2 aces, they count for 1 and 11 respectively.\n".format(players[player]))
                        player_data[player][6] += player_data[player][5]
                        if(player_data[player][5] == 11):
                            player_data[player][5] = 1
                        else:
                            player_data[player][5] = 11
                    elif(choose <= 9):
                        player_data[player][6] += choose
                    else:
                        player_data[player][6] += 10
                    player_data[player][3].append(card_names[choose - 1])
                    card_deck[choose - 1] -= 1
                    print("Your cards: {}\nYour total: {}\n".format(player_data[player][3], player_data[player][6]))
                    if(player_data[player][6] > 21):
                        if(player_data[player][3].count("Ace") == 1 and savage == 0):
                            print("\nYou exceeded 21. However, you have an ace counting as 11, so you can\ncount it as 1 and continue playing.")
                            player_data[player][6] -= 10
                            player_data[player][5] = 11
                            savage = 1
                            print("Your cards: {}\nYour total: {}\n".format(player_data[player][3], player_data[player][6]))
                        else:
                            print("\nBUST!!!\n\nYou lost the game.")
                            stop = True
                else:
                    print("\nYou stand.")
                    stop = True
            print("\n\nPress ENTER to continue\n")
            input()
        ClearScreen()
        print("The dealer plays now. He must take cards until\nhe has 17 or more.")
        print("\nPress ENTER to continue\n")
        input()
        print("Dealer's total:", dealer_data[1])
        savage = 0
        while(dealer_data[1] < 17):
            print("\nThe dealer will take another card...")
            print("\n\nPress ENTER to continue")
            input()
            choose = CardChoose(card_deck)
            print("\nDealer: {}".format(card_names[choose - 1]))
            if(choose == 1):
                dealer_data[1] += 11
            elif(choose <= 9):
                dealer_data[1] += choose
            else:
                dealer_data[1] += 10
            dealer_data[0].append(card_names[choose - 1])
            card_deck[choose - 1] -= 1
            print("\nDealer's total:", dealer_data[1])
            if(dealer_data[1] > 21):
                if(dealer_data[0].count("Ace") == 1 and savage == 0):
                    print("\nThe dealer exceeded 21. However, he has an ace counting as 11, so he will\ncount it as 1 and continue playing.")
                    dealer_data[1] -= 10
                    savage = 1
                else:
                    print("\nBUST!!!\nThe dealer's total is higher than 21, so he looses.\n\nAll the players who stood are paid their bets.")
                    for player in range(len(players)):
                        if(player_data[player][6] <= 21):
                            player_data[player][8] += 2*player_data[player][1]
                        if(player_data[player][7] <= 21 and player_data[player][7] > 0):
                            player_data[player][8] += 2*player_data[player][1]
                    EndOfGame(players, player_data, "PvB")
                    return
        print("The dealer's total is {}, so he will stand. If any player has a\nhigher total, the dealer pays him the bet he made. If a player\nhas a lower total, he looses his bet. Equal total means that the\nplayer keeps his initial bet.".format(dealer_data[1]))
        for player in range(len(players)):
            if(player_data[player][6] > dealer_data[1] and player_data[player][6] <= 21):
                player_data[player][8] += 2*player_data[player][1]
            elif(player_data[player][6] == dealer_data[1]):
                player_data[player][8] += player_data[player][1]
            if(player_data[player][7] > dealer_data[1] and player_data[player][7] <= 21):
                player_data[player][8] += 2*player_data[player][1]
            elif(player_data[player][7] == dealer_data[1]):
                player_data[player][8] += player_data[player][1]
        EndOfGame(players, player_data, "PvB")
        return
    else:
        ClearScreen()
        return PvP(players)

def PvP(players):
    if(len(players) < 2):
        print("You can't play PvP in single player mode.")
        return Menu()
    else:
        print("Welcome to PvP! In this game, the dealer is a human (the first\nname typed). You can also play with a bot dealer in the PvB mode.\nDo you wish to continue?\n")
        print("1. Continue\n2. Switch mode")
        answer = CheckValues(1, 2, invalid, invalid)
        if(answer == 1):
            ClearScreen()
            Bets()
            player_data = PlayerData(players, "PvP")
            dealer_data = [[], 0]
            card_deck = []
            for i in range(13):
                card_deck.append(4)
            ClearScreen()
            for i in range(2):
                if(i == 0):
                    print("Now, the dealer will give a card to each player...\n")
                else:
                    print("\n\nPress ENTER to continue")
                    input()
                    ClearScreen()
                    print("Again, the dealer will give a second card to each player but his\ncard will be hidden.\n")
                for player in range(len(players) - 1):
                    print("\nDealer ({}), press ENTER to give a card to {}.".format(players[0], players[player + 1]))
                    input()
                    choose = CardChoose(card_deck)
                    print("{}: {}\n".format(players[player + 1], card_names[choose - 1]))
                    if(choose == 1):
                        print("{}, you took an ace. By default, it counts for 11 but if you\nexceed 21 in total count, you can count it as 1. Note that if you\ntake 2 aces, they count for 1 and 11 respectively.\n".format(players[player+ 1]))
                        player_data[player][6] += player_data[player][5]
                        if(player_data[player][5] == 11):
                            player_data[player][5] = 1
                        else:
                            player_data[player][5] = 11
                    elif(choose <= 9):
                        player_data[player + 1][6] += choose
                    else:
                        player_data[player + 1][6] += 10
                    player_data[player + 1][3].append(card_names[choose - 1])
                    card_deck[choose - 1] -= 1
                choose = CardChoose(card_deck) # ------------
                if(i == 0):
                    print("\nDealer ({}), press ENTER to take a card.".format(players[0]))
                    input()
                    print("Dealer ({}): {}".format(players[0], card_names[choose - 1]))
                else:
                    print("\nDealer ({}), press ENTER to take a card.".format(players[0]))
                    input()
                    print("Dealer ({}): Hidden card".format(players[0]))
                if(choose == 1):
                    dealer_data[1] += 11
                elif(choose <= 9):
                    dealer_data[1] += choose
                else:
                    dealer_data[1] += 10
                dealer_data[0].append(card_names[choose - 1])
                card_deck[choose - 1] -= 1
            print("\n\nPress ENTER to continue")
            input()
            ClearScreen()
            if(dealer_data[0][0] == "Ace"):
                print("The dealer's first card is an ace. Bet for insurance?\n")
                print("1. Continue\n2. Learn more about insurance")
                answer = CheckValues(1, 2, invalid, invalid)
                if(answer == 2):
                    Insurance()
                    print("\n\nPress ENTER to continue")
                    input()
                for player in range(len(players) - 1):
                    print("\n{}, place a bet from 0$ to {}$:".format(players[player + 1], player_data[player + 1][1]//2))
                    player_data[player + 1][2] = CheckValues(0, player_data[player + 1][1]//2, low, high)
            if(dealer_data[0][0] == "Ace" or dealer_data[0][0] == "Ten" or dealer_data[0][0] == "Jack" or dealer_data[0][0] == "Queen" or dealer_data[0][0] == "King"):
                print("The dealer ({}) will see if he has a blackjack\n".format(players[0]))
                print("{} looking secretely... (Press ENTER to continue)".format(players[0]))
                input()
                if(dealer_data[1] == 21):
                    print("\n\nBLACKJACK!!!\n")
                    for player in range(len(players) - 1):
                        print("The game ends. The players who placed a bet for insurance will\ntake back double the ammount. Players who also have a blackjack will take their initial bets back.\n")
                        player_data[player + 1][8] += 2*player_data[player + 1][2]
                        if(player_data[player + 1][6] == 21):
                            player_data[player + 1][8] += player_data[player + 1][1]
                    EndOfGame(players, player_data, "PvP")
                    return
                    if(dealer_data[0][0] == "Ace"):
                        print("The hidden card was a ten-card, so the dealer ({}) won a 'blackjack'.\n\nAll players loose their initial bets. If any player placed a bet\nfor insurance, he will get back double their insurance.".format(players[0]))
                    else:
                        print("The hidden card was an ace, so the dealer ({}) won a 'blackjack'.\n\nAll players loose their initial bets.".format(players[0]))
                    EndOfGame(players, player_data, "PvP")
                    return
                else:
                    print("\n\n{} doesn't have a blackjack.\n".format(players[0]))
                print("\n\nPress ENTER to continue")
                input()
            for player in range(len(players) - 1):
                savage = 0
                doubled = False
                stop = False
                ClearScreen()
                print(players[player + 1], "plays now!\n")
                if(player_data[player + 1][6] >= 9 and player_data[player + 1][6] <= 11):
                    print("{}, your total is {}. You can double your bet if you want.\n".format(players[player + 1], player_data[player + 1][6]))
                    print("1. Double down\n2. Learn more about doubling")
                    answer = CheckValues(1, 2, invalid, invalid)
                    if(answer == 2):
                        Doubling()
                        print("Double down?\n")
                        print("1. Yes\n2. No")
                        answer = CheckValues(1, 2, invalid, invalid)
                    if(answer == 1):
                        doubled = True
                        player_data[player + 1][8] -= player_data[player + 1][1]
                        player_data[player + 1][1] *= 2
                        print("\n{}, you doubled your bet. Total bet: {}$\n".format(players[player + 1], player_data[player + 1][1]))
                    print("\nPress ENTER to continue\n")
                    input()
                if(player_data[player + 1][3][0] == player_data[player + 1][3][1]):
                    if(player_data[player + 1][3][0] != "Five" or not doubled):
                        print("{}, you have 2 similar cards. Do you want to split pairs?\n".format(players[player + 1]))
                        print("1. Split pairs\n2. Learn more about splitting pairs")
                        answer = CheckValues(1, 2, invalid, invalid)
                        if(answer == 2):
                            Splitting()
                            print("Split pairs?\n")
                            print("1. Yes\n2. No")
                            answer = CheckValues(1, 2, invalid, invalid)
                        if(answer == 1):
                            player_data[player + 1][4].append(player_data[player + 1][3][1])
                            del(player_data[player + 1][3][1])
                            player_data[player + 1][8] -= player_data[player + 1][1]
                            player_data[player + 1][1] *= 2
                            print("\n{}, you split pairs and doubled your bet.\n\nPress ENTER to continue".format(players[player + 1]))
                            input()
                            for i in range(2):
                                ClearScreen()
                                if(i == 0):
                                    print("Left hand play:\n\n")
                                else:
                                    print("Right hand play:\n\n")
                                player_data[player + 1][5] = 11
                                player_data[player + 1][i + 6] = card_names.index(player_data[player + 1][i + 3][0]) + 1
                                savage = 0
                                stop = False
                                print("Your cards: {}\nYour total: {}\n".format(player_data[player + 1][i + 3], player_data[player + 1][i + 6]))
                                while(stop == False):
                                    print("\n{}, do you want to take a card?".format(players[player + 1]))
                                    print("1. Take a card\n2. Stand")
                                    answer = CheckValues(1, 2, invalid, invalid)
                                    if(answer == 1):
                                        if(player_data[player + 1][i + 3] == "Ace"):
                                            stop = True
                                        choose = CardChoose(card_deck)
                                        print("\n\n{}: {}".format(players[player + 1], card_names[choose - 1]))
                                        if(choose == 1):
                                            print("\n{}, you took an ace. By default, the first ace counts for 11 but if you\nexceed 21 in total count, you can count it as 1. Note that if you\ntake 2 aces, they count for 1 and 11 respectively.\n".format(players[player]))
                                            player_data[player + 1][i + 6] += player_data[player + 1][5]
                                            if(player_data[player + 1][5] == 11):
                                                player_data[player + 1][5] = 1
                                            else:
                                                player_data[player + 1][5] = 11
                                        elif(choose <= 9):
                                            player_data[player + 1][i + 6] += choose
                                        else:
                                            player_data[player + 1][i + 6] += 10
                                        player_data[player + 1][i + 3].append(card_names[choose - 1])
                                        card_deck[choose - 1] -= 1
                                        print("Your cards: {}\nYour total: {}\n".format(player_data[player + 1][i + 3], player_data[player + 1][i + 6]))
                                        if(player_data[player + 1][i + 6] > 21):
                                            if(player_data[player + 1][i + 3].count("Ace") == 1 and savage == 0):
                                                print("\nYou exceeded 21. However, you have an ace counting as 11, so you can\ncount it as 1 and continue playing.")
                                                player_data[player + 1][i + 6] -= 10
                                                player_data[player + 1][5] = 11
                                                savage = 1
                                            else:
                                                print("\nBUST!!!")
                                                stop = True
                                    else:
                                        print("\nYou stand.")
                                        stop = True
                                if(i == 0):
                                    print("\n\nPress ENTER to continue\n")
                                    input()
                elif(player_data[player + 1][6] == 21):
                    print("{}, you have a BLACKJACK!!! The dealer ({}) pays you 1,5 times your bet!".format(players[player + 1], players[0]))
                    player_data[player + 1][8] += int(0.5*player_data[player + 1][1])
                    stop = True
                if(not stop):
                    print("Your cards: {}\nYour total: {}\n".format(player_data[player + 1][3], player_data[player + 1][6]))
                while(stop == False):
                    print("\n{}, do you want to take a card?".format(players[player + 1]))
                    print("1. Take a card\n2. Stand")
                    answer = CheckValues(1, 2, invalid, invalid)
                    if(answer == 1):
                        if(doubled):
                            stop = True
                        choose = CardChoose(card_deck)
                        print("\n\n{}: {}".format(players[player + 1], card_names[choose - 1]))
                        if(choose == 1):
                            print("\n{}, you took an ace. By default, the first ace counts for 11 but if you\nexceed 21 in total count, you can count it as 1. Note that if you\ntake 2 aces, they count for 1 and 11 respectively.\n".format(players[player + 1]))
                            player_data[player + 1][6] += player_data[player + 1][5]
                            if(player_data[player + 1][5] == 11):
                                player_data[player + 1][5] = 1
                            else:
                                player_data[player + 1][5] = 11
                        elif(choose <= 9):
                            player_data[player + 1][6] += choose
                        else:
                            player_data[player + 1][6] += 10
                        player_data[player + 1][3].append(card_names[choose - 1])
                        card_deck[choose - 1] -= 1
                        print("Your cards: {}\nYour total: {}\n".format(player_data[player + 1][3], player_data[player + 1][6]))
                        if(player_data[player + 1][6] > 21):
                            if(player_data[player + 1][3].count("Ace") == 1 and savage == 0):
                                print("\nYou exceeded 21. However, you have an ace counting as 11, so you can\ncount it as 1 and continue playing.")
                                player_data[player + 1][6] -= 10
                                player_data[player + 1][5] = 11
                                savage = 1
                                print("Your cards: {}\nYour total: {}\n".format(player_data[player + 1][3], player_data[player + 1][6]))
                            else:
                                print("\nBUST!!!\n\nYou lost the game.")
                                stop = True
                    else:
                        print("\nYou stand.")
                        stop = True
                print("\n\nPress ENTER to continue\n")
                input()
            ClearScreen()
            print("The dealer ({}) plays now. He must take cards until\nhe has 17 or more.".format(players[0]))
            print("\nPress ENTER to continue\n")
            input()
            print("Dealer's total:", dealer_data[1])
            savage = 0
            while(dealer_data[1] < 17):
                print("\nThe dealer will take another card...")
                print("{}, press ENTER to take a card.".format(players[0]))
                input()
                choose = CardChoose(card_deck)
                print("\nDealer ({}): {}".format(players[0], card_names[choose - 1]))
                if(choose == 1):
                    dealer_data[1] += 11
                elif(choose <= 9):
                    dealer_data[1] += choose
                else:
                    dealer_data[1] += 10
                dealer_data[0].append(card_names[choose - 1])
                card_deck[choose - 1] -= 1
                print("\nDealer's total:", dealer_data[1])
                if(dealer_data[1] > 21):
                    if(dealer_data[0].count("Ace") == 1 and savage == 0):
                        print("\nThe dealer ({}) exceeded 21. However, he has an ace counting as 11, so he will\ncount it as 1 and continue playing.".format(players[0]))
                        dealer_data[1] -= 10
                        savage = 1
                    else:
                        print("\nBUST!!!\nThe dealer's total is higher than 21, so he looses.\n\nAll the players who stood are paid their bets.")
                        for player in range(len(players) - 1):
                            if(player_data[player + 1][6] <= 21):
                                player_data[player + 1][8] += 2*player_data[player + 1][1]
                            if(player_data[player + 1][7] <= 21 and player_data[player + 1][7] > 0):
                                player_data[player + 1][8] += 2*player_data[player + 1][1]
                        EndOfGame(players, player_data, "PvP")
                        return
            print("The dealer's total is {}, so he will stand. If any player has a\nhigher total, the dealer ({}) pays him the bet he made. If a player\nhas a lower total, he looses his bet. Equal total means that the\nplayer keeps his initial bet.".format(dealer_data[1], players[0]))
            for player in range(len(players) - 1):
                if(player_data[player + 1][6] >= dealer_data[1] and player_data[player + 1][6] <= 21):
                    player_data[player + 1][8] += 2*player_data[player + 1][1]
                elif(player_data[player + 1][6] == dealer_data[1]):
                    player_data[player + 1][8] += player_data[player + 1][1]
                if(player_data[player + 1][7] >= dealer_data[1] and player_data[player + 1][7] <= 21):
                    player_data[player + 1][8] += 2*player_data[player + 1][1]
                elif(player_data[player + 1][7] == dealer_data[1]):
                    player_data[player + 1][8] += player_data[player + 1][1]
            EndOfGame(players, player_data, "PvP")
            return
        else:
            ClearScreen()
            return PvB(players)

def ObjectOfTheGame():
    print("OBJECT OF THE GAME\nEach participant attempts to beat the dealer by getting a count\nas close to 21 as possible, without going over 21.\n")

def CardValues():
    print("CARD VALUES\nIt is up to each individual player if an ace is worth 1 or 11.\nFace cards are 10 and any other card is its pip value.\n")

def Bets():
    print("BETS\nBefore the deal begins, each player places a bet from 2$ to 500$.\n")

def TheDeal():
    print("THE DEAL\nWhen all the players have placed their bets, the dealer gives\none card face up to each player and then one card face up to himself.\nAnother round of cards is then dealt face up to each player,\nbut the dealer takes his second card face down.\n")

def Naturals():
    print("NATURALS\nIf a player's first two cards are an ace and a 'ten-card' (a\npicture card or 10), giving him a count of 21 in two cards, this\nis a natural or 'blackjack.' If any player has a natural and the\ndealer does not, the dealer immediately pays that player one\nand a half times the amount of his bet. If the dealer has a natural,\nhe immediately collects the bets of all players who do not have naturals\n(but no additional amount). If the dealer and another player both\nhave naturals, the bet of that player is a stand-off (a tie),\nand the player takes back his chips. If the dealer's face-up card\nis a ten-card or an ace, he looks at his face-down card to see if\nthe two cards make a natural. If the face-up card is not a ten-card\nor an ace, he does not look at the face-down card until it is the\ndealer's turn to play.\n")

def ThePlay():
    print("THE PLAY\nThe player must decide whether to 'stand' (not ask for another\ncard) or 'hit' (ask for another card in an attempt to get closer\nto a count of 21, or even hit 21 exactly). Thus, a player may\nstand on the two cards originally dealt him, or he may ask the\ndealer for additional cards, one at a time, until he either decides\nto stand on the total (if it is 21 or under), or goes 'bust'\n(if it is over 21). In the latter case, the player loses and the\ndealer collects the bet wagered. The dealer then turns to the\nnext player and serves him in the same manner.\nThe combination of an ace with a card other than a ten-card is\nknown as a 'soft hand', because the player can count the ace as\n1 or 11 and either draw cards or not. For example, with a 'soft 17'\n(an ace and a 6), the total is 7 or 17. While a count of 17 is a\ngood hand, the player may wish to draw for a higher total. If the\ndraw creates a bust hand by counting the ace as an 11, the player\nsimply counts the ace as a 1 and continues playing by standing or 'hitting'.\n")

def DealersPlay():
    print("DEALER'S PLAY\nWhen the dealer has served every player, his face-down card is\nturned up. If the total is 17 or more, he must stand. If the total\nis 16 or under, he must take a card. He must continue to take\ncards until the total is 17 or more, at which point the dealer\nmust stand. If the dealer has an ace, and counting it as 11 would\nbring his total to 17 or more (but not over 21), he must count\nthe ace as 11 and stand.\n")

def Splitting():
    print("SPLITTING PAIRS\nIf a player's first two cards are of the same denomination, such as\ntwo jacks or two sixes, he may choose to treat them as two separate\nhands when his turn comes around. The amount of his original bet\nthen goes on one of the cards, and an equal amount must be placed\nas a bet on the other card. The player first plays the hand to his\nleft by standing or hitting one or more times; only then is the\nhand to the right played. The two hands are thus treated separately\nand the dealer settles with each on its own merits. With a pair of\naces, the player is given one card for each ace and may not draw again.\nAlso, if a ten-card is dealt to one of these aces, the payoff is\nequal to the bet (not one and one-half to one, as with a blackjack\nat any other time).\n")

def Doubling():
    print("DOUBLE DOWN\nAnother option open to the player is doubling his bet when the\noriginal two cards dealt total 9, 10, or 11. When the player's\nturn comes, he places a bet equal to the original bet and the\ndealer gives him just one card. With two fives, the player may\nsplit a pair, double down or just play the hand in the regular way.\nNote that the dealer does not have the option of splitting or doubling down.\n")

def Insurance():
    print("INSURANCE\nWhen the dealer's face-up card is an ace, any of the players may\nmake a side bet of up to half the original bet that the dealer's\nface-down card is a ten-card (a blackjack for the house). Once all\nsuch side bets are placed, the dealer looks at his hole card. If\nit is a ten-card, it is turned up and those players who have made\nthe insurance bet win and are paid double the amount of their\nhalf-bet - a 2 to 1 payoff. When a blackjack occurs for the dealer,\nof course, the hand is over and the players' main bets are collected\n- unless a player also has blackjack, in which case it is a stand-off.\n")

def Settlement():
    print("SETTLEMENT\nA bet once paid and collected is never returned. If the player\ngoes bust, he has already lost his wager, even if the dealer goes\nbust as well. If the dealer goes over 21, he pays each player\nwho has stood the amount of that player's bet. If the dealer stands\nat 20 or less, he pays the bet of any player having a higher total\n(not exceeding 21) and collects the bet of any player having a lower\ntotal. If there is a stand-off (a player having the same total as\nthe dealer), no chips are paid out or collected.\n")

def Rules():  # The rules are from https://www.bicyclecards.com/how-to-play/blackjack
    print("RULES\nThis is a list of rules of the game. It's not necessary to read\nthe rules if you know the basics, as there will be hints inside\nthe game.\n\n")
    print("1. Read the rules\n2. Return to the menu")
    answer = CheckValues(1, 2, invalid, invalid)
    if(answer == 1):
        ClearScreen()
        ObjectOfTheGame()
        CardValues()
        Bets()
        TheDeal()
        Naturals()
        ThePlay()
        DealersPlay()
        Splitting()
        Doubling()
        Insurance()
        Settlement()
        Menu()

Main() # starting the program
