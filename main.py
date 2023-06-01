import random

def get_random_word(words):
    random_index = random.randrange(len(words))
    return words[random_index]
#Delete above for submission

def intro():
    name = input("Please enter your name: ")
    print(f"\nWelcome to Wordle 101 {name}\n")
    print("========================================================================")
    print("                                 Rules")
    print("You have 6 guesses to figure out the solution.")
    print("All solutions are words that are 5 letters long.")
    print("Words may include repeated letters.")
    print("Letters that have been guessed correctly are displayed in uppercase.")
    print("Letters that are in the word but have been guessed in the wrong location")
    print("are displayed in lowercase.")
    print("========================================================================\n")

def print_bar_chart(data_dict, rounds_won, round_counter):
    keys = sorted(data_dict)
    win_percentage = round((sum(data_dict.values())/round_counter)*100)
    print("========================================================================")
    print("                                Summary")
    print(f"Win percentage: {win_percentage}%")
    print("Win Distribution:")
    for key in keys:
        print(str(key)+"|"+"#"*data_dict[key]+str(data_dict[key]))
    print("========================================================================")

def get_player_guess():
    guess = input("Please enter your guess: ")
    while (len(guess)!=5) or (not guess.isalpha()):
        guess = input("Your guess must have 5 letters: ")
    return guess.lower()

def play_round(target_word):
    attempts = 1
    print(f"Guess {attempts}:")
    print()
    guess = get_player_guess()
    while guess.lower() != target_word:

        word_copy = list(target_word)
        matching = []
        print_list = ['_'] * 5
        for i in range(len(guess)):
            if guess[i] == target_word[i]:
                print_list[i] = guess[i].upper()
                matching.append(i)

        matching.sort(reverse=True)
        for index_value in matching:
            word_copy[index_value] = ""

        for i in range(len(word_copy)):
            if print_list[i] == "_":
                if guess[i] in word_copy:
                    match_index = word_copy.index(guess[i])
                    print_list[i] = guess[i].lower()
                    word_copy[match_index] = ""

        if guess != target_word:
            print(" ".join(print_list))
            print()
            attempts += 1
            if attempts == 7:
                return (attempts-1, False)
            print(f"Guess {attempts}:")
            print()
            guess = get_player_guess()

    formatted_word = []
    for i in range(len(target_word)):
        if target_word[i] == guess[i]:
            formatted_word.append(target_word[i].upper())
        else:
            formatted_word.append(target_word[i].lower())
    print(" ".join(formatted_word))
    print()
    return (attempts, True)

        
def play_game_round(word):
    rounds_win = play_round(word)
    return rounds_win

def play_game(word):
    score_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    round_win_counter = 0
    round_results = play_game_round(word)
    if round_results[1] == True:
        score_dict[round_results[0]] += 1
        round_win_counter += 1
        print(f"Success! The word is {word}!")
        print()
    else:
        print(f"Better luck next time! The word is {word}!")
        print()
    game_continue = input("Please enter 'Y' to continue or 'N' to stop playing: ")
    
    while game_continue != 'Y' and game_continue != 'N':
        print("Only enter 'Y' or 'N'!")
        game_continue = input("Please enter 'Y' to continue or 'N' to stop playing: ")
    else:
        if game_continue[0] == "Y":
            print()
            return (True,round_win_counter, score_dict)
        else:
            print()
            return (False,round_win_counter, score_dict)

def get_words(filename):
    file = open(filename)
    word_list = file.read().split()
    file.close()
    return word_list

def main():
    score_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    round_win_counter = 0
    word_file = input("Enter the name of the word file: ")
    word_list = get_words(word_file)
    intro()
    word = get_random_word(word_list)
    print()
    round_counter = 1
    print(f"Round: {round_counter}")
    print()
    game_continue = play_game(word)
    while game_continue[0] == True:
        round_counter += 1
        round_win_counter += game_continue[1]
        for key in score_dict:
            score_dict[key] += game_continue[2][key] 
        word = get_random_word(word_list)
        print(f"Round: {round_counter}")
        print()
        game_continue = play_game(word)
    else:
        round_win_counter += game_continue[1]
        for key in score_dict:
            score_dict[key] += game_continue[2][key]
    print_bar_chart(score_dict, round_win_counter, round_counter)

main()
