"""
    LETULZEAU Baptiste
    EPITECH day 7 python
"""

import random 
import string
import turtle

def gameEngine():
    # graphique interface
    # window = turtle.Screen()
    # window.title("HangingGame")
    # pendu = turtle.Turtle()

    #def draw_part(part):
        # """Dessine une partie du pendu en fonction des erreurs."""
        # if part == 1:
        #     # Dessine la base
        #     pendu.penup()
        #     pendu.goto(-50, -150)
        #     pendu.pendown()
        #     pendu.forward(100)
        # elif part == 2:
        #     # Dessine le poteau
        #     pendu.penup()
        #     pendu.goto(0, -150)
        #     pendu.pendown()
        #     pendu.left(90)
        #     pendu.forward(200)
        # elif part == 3:
        #     # Dessine la barre horizontale
        #     pendu.right(90)
        #     pendu.forward(50)
        # elif part == 4:
        #     # Dessine la corde
        #     pendu.right(90)
        #     pendu.forward(30)
        # elif part == 5:
        #     # Dessine la tête
        #     pendu.circle(10)
        # elif part == 6:
        #     # Dessine le corps
        #     pendu.right(90)
        #     pendu.forward(50)
        # elif part == 7:
        #     # Dessine la jambe gauche
        #     pendu.left(45)
        #     pendu.forward(30)
        # elif part == 8:
        #     # Dessine la jambe droite
        #     pendu.penup()
        #     pendu.goto(0, -80)
        #     pendu.pendown()
        #     pendu.right(90)
        #     pendu.forward(30)


    # dictionnary of the most used langages
    frequence_langs = {
        'a' : 7.636, 'b' : 0.901, 'c' : 3.260, 'd' : 3.669, 'e' : 14.715, 'f' : 1.066, 'g' : 0.866, 'h' : 0.737,
                    'i' : 7.529, 'j' : 0.613, 'k' : 0.074, 'l' : 5.456, 'm' : 2.968, 'n' : 7.095, 'o' : 5.796, 'p' : 2.521, 
                    'q' : 1.362, 'r' : 6.693, 's' : 7.948, 't' : 7.244, 'u' : 6.311, 'v' : 1.838, 'w' : 0.049, 'x' : 0.427,
                    'y' : 0.128, 'z' : 0.326
    }

    with open('mots.txt', 'r') as fichier:
        content = fichier.read()
        mots = content.split()

    # list of word which can perhaps be selected by the random
    #list_of_words = ["kayak", "alphabet", "gabriel"]

    def deleteNonAlpha(finalWord):
        """Allows you to remove accents from letters with"""
        tableau = { 'éèêẽ' : 'e'
            , 'ç'    : 'c'
            , 'àâã'  : 'a'
            , 'ù'    : 'u'
            , 'îï'   : 'i'
        }

        mot = ""
        for char in finalWord:
            for k in tableau:
                if char in k: 
                    char = tableau[k]
            mot+=char

        return mot.upper()

    # random to have an index to select a word among the list
    #random_index = random.randint(0,2)
    random_index = random.randint(0, 100)
    random_word = mots[random_index]
    deleteNonAlpha(random_word.lower())
    #random_word = list_of_words[random_index]
    length_random_word = len(random_word)

    # dict of letters
    dict_letters = {letters:0 for letters in string.ascii_lowercase}

    # frequency of the letters in the word
    frequence_dict = {letter: round((dict_letters[letter] / length_random_word) * 100, 3) for letter in dict_letters}

    # dict sort by words which have the same length as the random_word
    dictionnary_words = {index: mot for index, mot in enumerate(mots) if len(mot) == length_random_word}

    # calculate the difference between both dict
    for frequence_langs in frequence_langs.items():
        difference = 0
        for letter in frequence_dict:
            if letter in frequence_langs:
                difference += (frequence_dict[letter] - frequence_langs[letter]) ** 2

    # put in liste the string to guess
    word_list = list(random_word)

    # hide the word with some "_"
    hidden_word = ['_'] * len(word_list)

    # letters already guessed and attempts_left
    guessed_letters = []
    attempts_left = 5

    def ask_letter():
        """return user letter asked"""
        ask = str(input("Please enter a letter: ").lower())
        return ask

    def IA_letter():
        """return a letter which the IA has played"""
        ask = random.randint(0,25)
        return string.ascii_lowercase[ask]
    
    mode = int(input("Put an integer (0 or 1)"))
    
    if (mode == 0):
        while attempts_left > 0 and "_" in hidden_word:
            # ask a letter to the user
            letter_asked = ask_letter()

            if (letter_asked in guessed_letters):
                print("Letter already played !")
                continue

            # to verify if the user have already played the letter
            guessed_letters.append(letter_asked)

            if (letter_asked in word_list):
                for i, letter in enumerate(word_list):
                    if (letter == letter_asked):
                        hidden_word[i] = letter_asked
                print(f"The letter {letter_asked} is in the word !")
                print(f"{hidden_word}")
                print(f"You have already played: {guessed_letters}")
            else:
                print(f"The letter {letter_asked} isn't in the word !")
                print(f"You have already played: {guessed_letters}")
                print(f"Numbers of attempts left: {attempts_left}")
                attempts_left -= 1
                #draw_part(8 - attempts_left)

    else:
        while attempts_left > 0 and "_" in hidden_word:
            # ask a letter to the user
            letter_asked = IA_letter()

            if (letter_asked in guessed_letters):
                print("Letter already played !")
                continue
                
            # to verify if the user have already played the letter
            guessed_letters.append(letter_asked)

            if (letter_asked in word_list):
                for i, letter in enumerate(word_list):
                    if (letter == letter_asked):
                        hidden_word[i] = letter_asked
                        dictionnary_words = {index: word for index, word in dictionnary_words.items() if word[i] == letter}
                print(f"The letter {letter_asked} is in the word !")
                print(f"{hidden_word}")
                print(f"You have already played: {guessed_letters}")
            else:
                print(f"The letter {letter_asked} isn't in the word !")
                print(f"You have already played: {guessed_letters}")
                print(f"Numbers of attempts left: {attempts_left}")
                attempts_left -= 1
                #draw_part(8 - attempts_left)

    if "_" not in hidden_word:
        print("Congradulation you have guessed the word !")
    elif (mode == 0):
        print(f"You have loose, the word was {random_word} !")
    else:
        print(f"IA have loose, the word was {random_word} !")

    # close the window
    #turtle.done()

gameEngine()

            
