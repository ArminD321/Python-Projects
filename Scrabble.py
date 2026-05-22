'''
SCRABBLE
Coder: Armin
Date: August 7th 2024

'''


import random as r

TILES = ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'A', 'I', 'A', 'I', 'A', 'I', 'A', 'I', 'A',
         'I', 'A', 'I', 'A', 'I', 'A', 'I', 'A', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'N', 'R', 'T', 'N',
         'R', 'T', 'N', 'R', 'T', 'N', 'R', 'T', 'N', 'R', 'T', 'N', 'R', 'T', 'L', 'S', 'U', 'L', 'S', 'U', 'L',
         'S', 'U', 'L', 'S', 'U', 'D', 'D', 'D', 'D', 'G', 'G', 'G', 'B', 'C', 'M', 'P', 'B', 'C', 'M', 'P',
         'F', 'H', 'V', 'W', 'Y', 'F', 'H', 'V', 'W', 'Y', 'K', 'J', 'X', 'Q', 'Z']

tile_to_points = {'E': 1, 'A': 1, 'I': 1, 'O': 1, 'N': 1, 'R': 1, 'T': 1, 'L': 1, 'S': 1, 'U': 1, 'D': 2, 'G': 2,
                  'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8,
                  'Q': 10, 'Z': 10}


## FUNCTION SPACE ##
dictionary=open('Collins Scrabble Words (2019).txt', 'r')
valid_words=[]
for i in dictionary:
    valid_words.append(i[:-1:])
dictionary.close()
# print(valid_words)
# GAME PLAY FUNCTIONS #
# by creating these two input sanitization functions, later code is much cleaner


def int_input(prompt):
    answer_int=input(prompt)
    while answer_int.isdigit() == False:
        answer_int=input(prompt)
    return int(answer_int)

# a=int_input('enter a integer')
# print(a,type(a))


def str_input(prompt):
    answer_str=input(prompt)
    while answer_str.isalpha() == False:
        answer_str=input(prompt)
    return answer_str

# a=str_input('enter a word')
# print(a, type(a))


def get_new_tiles(num):
    hand=(r.sample(TILES, k=num))
    for i in hand:
        TILES.remove(i)
    return hand

# print(len(TILES))
# b=get_new_tiles(7)
# print(b)
# print(len(TILES))

def print_hand(hand):
    for letter in hand:
        print('Letter:',letter, 'Value:', tile_to_points[letter])
# print_hand(b)

def get_points(word):
    '''
    The parameter 'word' is a word played by a player.
    Using the tiles_to_points dictionary, find out the total number of points this word is worth.
    Return this number.

    ex. get_points('CAT') returns 5
    '''
    total=0
    for letter in word:
        total+=tile_to_points[letter]
    return total

# a=get_points('ZAP')
# print(a)

def is_valid_play(word, hand):
    '''
    The parameter 'word' is a word the player is attempting to play, and 'hand' is that player's hand.
    This function needs to return True if this word is a valid play, and False otherwise.
    A word is a valid play if it only uses the tiles from hand AND contains at least one letter.
    It ALSO must be a valid scrabble word, as determined by the valid_words list.

    EX:
    is_valid_play('DOG', ['D', 'G', 'O', 'H', 'A', 'V', 'B']) is True
    is_valid_play('GLUE', ['D', 'G', 'O', 'H', 'A', 'V', 'B']) is False, hand does not have L, U, or E
    is_valid_play('DAD', ['D', 'G', 'O', 'H', 'A', 'V', 'B']) is False, there is only one D in hand
    is_valid_play('', ['D', 'G', 'O', 'H', 'A', 'V', 'B']) is False, word has to have some letters
    is_valid_play('VB', ['D', 'G', 'O', 'H', 'A', 'V', 'B']) is False, VB is not a valid scrabble word
    '''
    hand2 = hand[:]
    if word not in valid_words or not word:
        return False
    for letter in word:
        if letter in hand2:
            hand2.remove(letter)
        else:
            return False
    return True
# a='DOG'
# b=['D', 'G', 'O', 'H', 'A', 'V', 'B']
# e=is_valid_play(a,b)
# print(e)
# GAME STATISTIC FUNCTIONS #


def get_winner(player_to_points):
    highest_points = 0
    winner = ""
    for player, points in player_to_points.items():
        if points > highest_points:
            highest_points = points
            winner = player

    return winner


def get_best_word(player_to_words):
    best_word = ""
    highest_score = 0

    for words in player_to_words.values():
        for word in words:
            score = get_points(word)
            if score > highest_score:
                highest_score = score
                best_word = word

    return best_word

## GAME STARTS ##



num_players = int_input("Number of players: ")
player_to_words = {}  # maps a player to the words they have played
player_to_points = {}  # maps a player to the poins they have earned
player_to_hand = {}  # maps a player to a list of the tiles in their hand

# initialising all the dictionaries
for i in range(1, num_players + 1):
    name = str_input("Enter name of player " + str(i) + ": ")
    player_to_words[name] = []
    player_to_points[name] = 0
    player_to_hand[name] = get_new_tiles(7)
    print_hand(player_to_hand[name])

# MAIN GAME LOOP #
# this section contains the part of the game that repeats until the game is over
# the game is over if they run out of tiles or players choose to stop

choice = int(input("Enter a number to select: "))

while len(TILES) > 0:
    print("---- NEW ROUND ----")
    for player in player_to_words:
        print("--%s's TURN--" % (player))  # this prints whose turn it is now
        print_hand(player_to_hand[player])  # let them see their hand
        print("Options for your turn:\n0 - \t pick new tiles\n1 - \t play word\nany other number - \t STOP GAME")
        # player enters 0 to replace hand, 1 to play a word, and anything else to quit game
        choice = int_input("Enter a number to select: ")

        if choice == 0:
            # put their tiles back in the pool
            TILES.extend(player_to_hand[player])
            player_to_hand[player] = get_new_tiles(7)  # replace their hand
            print_hand(player_to_hand[player])  # show the new hand
            print("END OF TURN")

        elif choice == 1:
            word = str_input("Enter the word to play: ")
            # they can only play valid words!
            if not is_valid_play(word, player_to_hand[player]):
                print("INVALID GUESS - TURN SKIPPED")
            else:
                player_to_words[player].append(word)  # update word dictionary
                # find out how many points they earned
                points = get_points(word)
                print("Your word earned", points, "points!")
                player_to_points[player] += points  # update points dictionary
                for char in word:
                    # remove tiles from their hand
                    player_to_hand[player].remove(char)
                player_to_hand[player].extend(
                    get_new_tiles(7 - len(word)))  # refill their hand
                print("UPDATED HAND:")
                print_hand(player_to_hand[player])  # show them their new hand

        else:
            print("STOPPING GAME...")
            break  # get out of the for loop, while condition will be checked and will be false

print("GAME OVER - GENERATING GAME STATS")

