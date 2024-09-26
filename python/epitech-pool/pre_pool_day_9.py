import random
import turtle
from collections import Counter

# Configure the turtle screen
wn = turtle.Screen()
wn.title("Hangman Game with Turtle")
wn.bgcolor("white")

# Configure the turtle to draw the hangman
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(2)
pen.width(5)

word_pen = turtle.Turtle()
word_pen.hideturtle()
word_pen.penup()
word_pen.goto(-150, -200)
word_pen.pendown()
word_pen.speed(2)

def draw_hangman(errors):
    """Draw the hangman figure based on the number of errors."""
    pen.penup()
    
    if errors == 1:  # Draw the base
        pen.goto(-100, -150)
        pen.pendown()
        pen.forward(200)
    elif errors == 2:  # Draw the vertical pole
        pen.penup()
        pen.goto(-100, -150)
        pen.left(90)
        pen.pendown()
        pen.forward(300)
    elif errors == 3:  # Draw the top bar
        pen.penup()
        pen.goto(-100, 150)
        pen.right(90)
        pen.pendown()
        pen.forward(150)
    elif errors == 4:  # Draw the rope
        pen.penup()
        pen.goto(50, 150)
        pen.right(90)
        pen.pendown()
        pen.forward(50)
    elif errors == 5:  # Draw the head
        pen.penup()
        pen.goto(25, 72)
        pen.pendown()
        pen.circle(25)
    elif errors == 6:  # Draw the body
        pen.penup()
        pen.goto(50, 50)
        pen.right(0)
        pen.pendown()
        pen.forward(100)
    elif errors == 7:  # Draw the left arm
        pen.penup()
        pen.goto(50, 40)
        pen.right(80)
        pen.pendown()
        pen.forward(50)
    elif errors == 8:  # Draw the right arm
        pen.penup()
        pen.goto(50, 40)
        pen.right(210)
        pen.pendown()
        pen.forward(50)
    elif errors == 9:  # Draw the left leg
        pen.penup()
        pen.goto(50, -50)
        pen.left(0)
        pen.pendown()
        pen.forward(50)
    elif errors == 10:  # Draw the right leg
        pen.penup()
        pen.goto(50, -50)
        pen.right(145)
        pen.pendown()
        pen.forward(50)

# Letter frequencies in the French language
letter_frequencies = {
    'a': 7.636, 'b': 0.901, 'c': 3.260, 'd': 3.669, 'e': 14.715, 'f': 1.066, 'g': 0.866, 'h': 0.737,
    'i': 7.529, 'j': 0.613, 'k': 0.074, 'l': 5.456, 'm': 2.968, 'n': 7.095, 'o': 5.796, 'p': 2.521,
    'q': 1.362, 'r': 6.693, 's': 7.948, 't': 7.244, 'u': 6.311, 'v': 1.838, 'w': 0.049, 'x': 0.427,
    'y': 0.128, 'z': 0.326
}

def deleteNonAlpha(finalWord):
    """remove accents and convert to uppercase"""
    tab = {'éèêẽ': 'e', 'ç': 'c', 'àâã': 'a', 'ù': 'u', 'îï': 'i', '©': '', '¢': 'c', '¨': '', '®': '', 'Ã': 'a', '©': 'c'}
    word = ""
    for char in finalWord:
        for k in tab:
            if char in k:
                char = tab[k]
        word += char
    return word.upper()

def display_word(letters_found):
    """display the word"""
    word_pen.clear()
    word_display = " ".join(letters_found)
    word_pen.write(word_display, align="center", font=("Arial", 24, "normal"))

def choose_letter(possible_words, proposed_letters):
    """IA choose a letter"""
    # Concatenate all possible remaining words
    concatenated_words = ''.join(possible_words)
    
    # Filter out already proposed letters
    remaining_letters = [letter for letter in concatenated_words if letter.upper() not in proposed_letters]
    
    # Count occurrences of the remaining letters
    letter_count = Counter(remaining_letters)
    
    # Find the most frequent letter
    if letter_count:
        return max(letter_count, key=letter_count.get).upper()
    else:
        return None

def hangman():
    """game where all function are regrouped"""
    with open('mots.txt', 'r') as file:
        content = file.read()
        words = content.split()

    # Choose a random word with a random index
    random_index = random.randint(0, len(words) - 1)
    random_word = deleteNonAlpha(words[random_index].lower())
    word_length = len(random_word)

    proposed_letters = set()
    found_letters = ["_"] * word_length

    def update_found_letters(word, letter, found_letters):
        for index, char in enumerate(word):
            if char == letter:
                found_letters[index] = letter
        return found_letters

    display_word(found_letters)

    # Start the game
    errors = 0
    possible_words = [word for word in words if len(word) == word_length]

    print(f"The word has {word_length} letters.")
    
    while "_" in found_letters and errors != 10:
        # AI proposes a new letter from the alphabet, excluding already proposed letters
        new_letter = choose_letter(possible_words, proposed_letters)
        if new_letter is not None:
            new_letter = new_letter.upper()
        proposed_letters.add(new_letter)
        
        print(f"The AI proposes the letter '{new_letter}'.")
        
        if new_letter in random_word:
            print(f"The letter '{new_letter}' is in the word.")
            # Update found letters list
            found_letters = update_found_letters(random_word, new_letter, found_letters)
        else:
            print(f"The letter '{new_letter}' isn't in the word.")
            errors += 1
            draw_hangman(errors)
        
        print(f"Errors: {errors}")
        print(f"Current word: {' '.join(found_letters)}")
        display_word(found_letters)
        
        # Filter possible words based on current letters found
        possible_words = [
            word for word in possible_words if all(
                (found_letters[i].lower() == word[i] or found_letters[i] == "_") for i in range(word_length)
            )
        ]
        
        # If only one word remains
        if len(possible_words) == 1:
            print(f"Word found: {possible_words[0].upper()}")
            display_word(list(possible_words[0].upper()))
            break
    
        # If AI loses
        if errors == 10:
            print(f"The AI lost, the word was {random_word}")
            print(f"The list of possible words was: {possible_words}")

hangman()

wn.mainloop()
