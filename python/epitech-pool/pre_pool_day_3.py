"""
    LETULZEAU Baptiste
    EPITECH pré-pool day3 python
"""

import re
import string

def Task_1_1(string):
    print(string)


def Task_1_2(string):
    print(string[0])


def Task_1_3(string):
    print(string[-0])


def Task_1_4(string):
    print(string[5:10])


def Task_2_1(string):
    print(string.lower())


def Task_2_2(string):
    stringNew = ""
    print(string.replace(string, stringNew))


def Task_2_3():
    """it returns -1 if no result"""
    string = " hello world "
    position = string.find("a")
    print(position)


def Task_2_4():
    p = "abcdefghij"
    print(p[::-2][:5][::-1][3:])


def Task_2_5():
    p = "abcdefghij"
    print(p[7:9])


def Task_2_6(string, times):
    for i in range(times):
        print(string)


def Task_2_7(s):
    for _ in range(10):
        print(s)


def Task_2_8():
    """can't concatenate str and int"""
    s1 = "Hello"
    s2 = 42
    concat = s1 + s2
    print(concat)


def Task_2_9():
    """calculate the legth of the sentence and print it"""
    string1 = "42"
    string2 = "is"
    string3 = " the answer "
    concat = string1 + string2 + string3
    length = len(concat)
    print(f"The string {concat} contains {length} characters ).")


def challenge(string):
    """read if the string contains some words right side up and upside down"""
    string1 = "cat"
    string2 = "garden"
    string3 = "mice"
    stringLower = string.lower()
    counter = 0

    # test if somes strings are in my string right side up
    if string1 in stringLower:
        counter += 1
    if string2 in stringLower:
        counter += 1
    if string3 in stringLower:
        counter += 1

    # reverse the string
    newString = string[::-1]

    # test if somes strings are in my string upside down
    if string1 in newString:
        counter += 1
    if string2 in newString:
        counter += 1
    if string3 in newString:
        counter += 1

    print(counter)
    return counter


# challenge("thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN")


def Task_3_1():
    inputName = input("Put your name")
    print(f"Hello {inputName}")


def Task_3_2():
    inputName = input("Put your name")
    concat = inputName[0].upper() + inputName[1:]
    print(f"Hello {concat}")


def Task_3_3():
    inputInt1 = int(input("Put one number"))
    inputInt2 = int(input("Put one other number"))
    sum = inputInt1 + inputInt2
    print("The sum of the two provided numbers is {sum}")


def Task_3_4():
    inputInt = int(input("Put one number"))
    print(type(inputInt))
    return type(inputInt)


def Task_3_5(string):
    # slice sentences in the string 
    sentences = re.split(r'[.!?]\s*', string.strip())
    
    # first word of each sentence
    first_words = []
    for sentence in sentences:
        if sentence:
            first_words.append(sentence.split()[0])
    
    # join sliced words with spaces and a dot at the end
    result = " ".join(first_words) + "."
    
    print(result)
    return result


#Task_3_5("This is a test. Is it possible to fly? Good things come to those who never give up.")


def Task_3_6(text):
    """search the lang of the text, depending on the frequency found"""
    # dictionnary of the most used langages
    frequence_langs = {
        'french' : {'a' : 7.636, 'b' : 0.901, 'c' : 3.260, 'd' : 3.669, 'e' : 14.715, 'f' : 1.066, 'g' : 0.866, 'h' : 0.737,
                    'i' : 7.529, 'j' : 0.613, 'k' : 0.074, 'l' : 5.456, 'm' : 2.968, 'n' : 7.095, 'o' : 5.796, 'p' : 2.521, 
                    'q' : 1.362, 'r' : 6.693, 's' : 7.948, 't' : 7.244, 'u' : 6.311, 'v' : 1.838, 'w' : 0.049, 'x' : 0.427,
                    'y' : 0.128, 'z' : 0.326},

        'english': {'a' : 8.167, 'b' : 1.492, 'c' : 2.782, 'd' : 4.253, 'e' : 12.702, 'f' : 2.228, 'g' : 2.015, 'h' : 6.094,
                    'i' : 6.966, 'j' : 0.153, 'k' : 0.772, 'l' : 4.025, 'm' : 2.406, 'n' : 6.749, 'o' : 7.507, 'p' : 1.929, 
                    'q' : 0.095, 'r' : 5.987, 's' : 6.327, 't' : 9.056, 'u' : 2.758, 'v' : 0.978, 'w' : 2.360, 'x' : 0.150,
                    'y' : 1.974, 'z' : 0.074},

        'spanish': {'a' : 12.525, 'b' : 1.415, 'c' : 4.679, 'd' : 5.816, 'e' : 13.681, 'f' : 0.692, 'g' : 1.008, 'h' : 0.703,
                    'i' : 6.247, 'j' : 0.493, 'k' : 0.011, 'l' : 4.967, 'm' : 3.157, 'n' : 6.712, 'o' : 8.683, 'p' : 2.510, 
                    'q' : 0.877, 'r' : 6.871, 's' : 7.977, 't' : 4.632, 'u' : 2.927, 'v' : 0.898, 'w' : 0.017, 'x' : 0.215,
                    'y' : 0.898, 'z' : 0.467},

        'german': { 'a' : 6.516, 'b' : 1.886, 'c' : 3.062, 'd' : 5.076, 'e' : 17.396, 'f' : 1.656, 'g' : 3.009, 'h' : 4.577,
                    'i' : 7.550, 'j' : 0.268, 'k' : 1.217, 'l' : 3.437, 'm' : 2.534, 'n' : 9.776, 'o' : 2.514, 'p' : 0.790, 
                    'q' : 0.018, 'r' : 7.003, 's' : 7.270, 't' : 6.154, 'u' : 4.346, 'v' : 0.846, 'w' : 1.891, 'x' : 0.034,
                    'y' : 0.039, 'z' : 1.134},

        'portuguese': { 'a' : 14.634, 'b' : 1.043, 'c' : 3.882, 'd' : 4.992, 'e' : 12.570, 'f' : 1.023, 'g' : 1.303, 'h' : 0.781,
                    'i' : 6.186, 'j' : 0.397, 'k' : 0.015, 'l' : 2.779, 'm' : 4.738, 'n' : 4.446, 'o' : 9.735, 'p' : 2.523, 
                    'q' : 1.204, 'r' : 6.530, 's' : 6.805, 't' : 4.336, 'u' : 3.639, 'v' : 1.575, 'w' : 0.037, 'x' : 0.253,
                    'y' : 0.006, 'z' : 0.470},

        'italian': {'a' : 11.745, 'b' : 0.927, 'c' : 4.501, 'd' : 3.736, 'e' : 11.792, 'f' : 1.153, 'g' : 1.644, 'h' : 0.636,
                    'i' : 10.143, 'j' : 0.011, 'k' : 0.009, 'l' : 6.510, 'm' : 2.512, 'n' : 6.883, 'o' : 9.832, 'p' : 3.056, 
                    'q' : 0.505, 'r' : 6.367, 's' : 4.981, 't' : 5.623, 'u' : 3.011, 'v' : 2.097, 'w' : 0.033, 'x' : 0.003,
                    'y' : 0.020, 'z' : 1.181}
    }

    text = text.lower()
    dict_letters = {letters:0 for letters in string.ascii_lowercase}

    # letter's count of the text
    count = 0
    for letter in text:
        if letter in dict_letters:
            count += 1
            dict_letters[letter] += 1

    # frequency of the letters in the text
    frequence_dict = {letter: round((dict_letters[letter] / count) * 100, 3) for letter in dict_letters}

    final_lang = ""
    difference_infinity = float('inf')

    # calculate the difference between both dict
    for lang, frequence_langs in frequence_langs.items():
        difference = 0
        for letter in frequence_dict:
            if letter in frequence_langs:
                difference += (frequence_dict[letter] - frequence_langs[letter]) ** 2

        # determines the final lang with the difference between both dict
        if difference < difference_infinity:
            difference_infinity = difference
            final_lang = lang 

    print(final_lang)
    return final_lang

Task_3_6("Ne t'inquiète pas, elle n'a rien pour l'instant. Par contre, dès que je serais relié au réseau, Florence ne sera plus. Tu comprends, je ne peux pas laisser Florence me gêner dans ma tâche. Et puis, elle en sait beaucoup trop sur moi. David avait dû s'asseoir lorsqu'il avait entendu le prénom Florence. Il était devenu blanc un instant. Il allait peut-être perdre Florence avant même de lui avoir avoué son amour. Il devait empêcher Prélude de continuer dans son délire. Mais comment pouvait-il stopper ce parasite créé par lui quelques années auparavant ? Ce n'était pas un adversaire ordinaire. David avait déjà détruit plus d'un virus, mais il s'agissait de virus installés sur des machines isolées. Aujourd'hui, c'est une sorte de virus qui a pris place sur tous les ordinateurs de la planète. Et en plus, ce virus, nommé Prélude, avait un soupçon, non négligeable, d'intelligence. Dans le plancher pour savoir si quelqu'un marchait et quel poids il faisait. Le cœur pouvait alors déterminer de quelle personne il s'agissait. Dans les murs, des cellules photosensibles, des micro-caméras et tout un réseau de détecteurs divers (magnétique, pression, infrarouge...) permettait de déterminer la position exacte de chaque personne et objet dans la maison, de ventiler ou chauffer en conséquence, d'allumer ou d'éteindre la lumière... C'est comme ça qu'il se voyait à cette époque. Un peu rebelle envers ce monde. L'informatique l'avait aidé à s'enfermer un peu plus dans cet état. Il était devenu doué d'une logique à toute épreuve et d'une intelligence remarquable, mais surtout, il était devenu insociable. Avec l'âge, le besoin de trouver l'âme sœur avait pris le dessus et il avait été un peu obligé de rencontrer des gens, de parler avec eux. Très difficile au début, il avait réussi à vaincre ces préjugés. Il avait accepté la lenteur d'esprit des autres ainsi que leur manque de logique. Internet n'est pas le seul réseau. Il existe un autre réseau plus performant. Je ne t'apprendrais rien en te disant qu'Internet a été crée par l'armée Américaine dans un but militaire. Internet n'était que le prototype. Un autre réseau a été créé pour les militaires. Complètement indépendant d'Internet. Tirant des leçons du premier réseau, le petit frère d'Internet est devenue un grand frère.")




