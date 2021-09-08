from random import randint

def initialize_score(make_score_0):
    if not make_score_0:
        pass
    else:
        # initial scores
        global player1_score, player2_score, player3_score, player4_score, player5_score
        player1_score = 0
        player2_score = 0
        player3_score = 0
        player4_score = 0
        player5_score = 0
        make_score_0 = False


def players():
    player = []
    for i in range(5):
        new_player = input("enter player name: ")
        print()
        player.append(new_player)
    return player


def jumble():
    position_list = ['king', 'queen', 'minister', 'police', 'thief']
    jumbled_position = []
    remaining_position = len(position_list)
    for i in range(5):
        random_number = randint(0, remaining_position - 1)
        position = position_list[random_number]
        jumbled_position.append(position)
        position_list.pop(random_number)
        remaining_position -= 1
    return jumbled_position


def select_token(player_name):
    temporary_position = {}
    token = [1, 2, 3, 4, 5]
    token_result = []
    for i in range(4):
        print(f"{player_name[i]}'s turn : ")
        print(f"Available Token : {token}")
        selected_token = int(input("select your token among given numbers: "))
        print()
        token_result.append(selected_token)
        token.remove(selected_token)
    else:
        last_token = token[0]
        print(f'{player_name[4]} turn : ')
        print(f"{player_name[4]} ,the last token is {last_token}. It's yours.")
        print()
        print("=================================================================")
        print()
        token_result.append(last_token)
    return token_result


def add_player_score(name, number,player_name):
    global player1_score, player2_score, player3_score, player4_score, player5_score
    if name == player_name[0]:
        player1_score += number
    elif name == player_name[1]:
        player2_score += number
    elif name == player_name[2]:
        player3_score += number
    elif name == player_name[3]:
        player4_score += number
    else:
        player5_score += number


def add_thief_score(thief, score):
    global player1_score, player2_score, player3_score, player4_score, player5_score
    if thief == 0:
        player1_score += score
    elif thief == 1:
        player2_score += score
    elif thief == 2:
        player3_score += score
    elif thief == 3:
        player4_score += score
    elif thief == 4:
        player5_score += score


def add_police_score(police, score):
    global player1_score, player2_score, player3_score, player4_score, player5_score
    if police == 0:
        player1_score += score
    elif police == 1:
        player2_score += score
    elif police == 2:
        player3_score += score
    elif police == 3:
        player4_score += score
    elif police == 4:
        player5_score += score


def police_call(lootera,k_paro,chittha_number):
    # players_name = players()
    police = 0
    thief = 0
    for i in range(1, 6):
        if k_paro[i] == 'thief':
            j = chittha_number.index(i)
            thief_name = player_name[j]
            thief = j
            # print(f'the thief index is {j}')
        if k_paro[i] == 'police':
            k = chittha_number.index(i)
            # police = player_name[k]
            police = k
            # print(f'the police index is {k}')

    culprit = input("enter the culprit name : ")
    print()
    culprit_name = culprit.strip()
    if culprit_name != lootera:
        add_police_score(police, 0)
        add_thief_score(thief, 50)
        print(f"The wanted criminal who stole the necklace was: {thief_name}")
        print('Mr. Culprit you were able to claim your loot $50 safely')
        print()
    else:
        add_police_score(police, 100)
        print('Mr. Police, queen sends regard to you.\n She has invited you tonight')
        print()
        add_thief_score(thief, 0)
        print(f"The wanted criminal who stole the necklace was: {thief_name}")
        print()


def add_score(player_name,chittha_number,k_paro):
    for i in range(1, 6):
        user = player_name[i - 1]
        lucky_number = chittha_number[i-1]

        if k_paro[lucky_number] == "king":
            add_player_score(user, 1000,player_name)
        elif k_paro[lucky_number] == "queen":
            add_player_score(user, 800,player_name)
        elif k_paro[lucky_number] == "minister":
            add_player_score(user, 400,player_name)
            print(
                f"{user} : This is your minister speaking.\nQueen's necklace has been stolen.\nI want police to find "
                f"the culprit.")
            print()
        elif k_paro[lucky_number] == "police":
            print(f'{user} : yes, sir. This is police.')
            print()
        else:
            looteraa = user

    police_call(looteraa,k_paro,chittha_number)


def final_score(player_name):
    player1, player2, player3, player4, player5 = player_name

    # all_score = [player1_score,player2_score,player3_score,player4_score,player5_score]
    # all_score.sort(reverse=True)

    print("============================================")
    print()
    print("     SCORE-BOARD    ")
    print(f"{player1}s' score: {player1_score}")
    print(f"{player2}' score: {player2_score}")
    print(f"{player3}' score: {player3_score}")
    print(f"{player4}' score: {player4_score}")
    print(f"{player5}' score: {player5_score}")
    print()
    print("===============================================")


def start_game(no_of_round):
    while(no_of_round>0):

        chittha = jumble()
        chittha_number = select_token(player_name)

        # print(chittha)
        # print(chittha_number)

        k_paro = {}
        j = 0
        for i in chittha_number:
            k_paro[i] = chittha[j]
            j += 1

        # print(k_paro)

        add_score(player_name,chittha_number,k_paro)

        no_of_round -=1


if __name__ == '__main__':
    print()
    print("                                                                                   ")
    print("   |||||  ||  ||  ||||||  ||||||          ||||||  ||||||  ||    ||  |||||  |||||   ")
    print("   ||     ||||||  ||  ||  ||__||   <==>   ||__||  ||  ||  ||    ||  ||     ||==:   ")
    print("   |||||  ||  ||  ||||||  || \L           ||      ||||||  ||||  ||  |||||  |||||   ")
    print()
    print()

    make_score_0 = True
    initialize_score(make_score_0)

    total_round = int(input("Enter number of rounds, you want to play : "))
    print()

    player_name = players()
    print("Players' name: ")
    [print(x, end="  ") for x in player_name]
    print()
    print()
    # print(player_name)

    start_game(total_round)
    final_score(player_name)