"""
    LETULZEAU Baptiste
    EPITECH day_4 python
"""

def Task_1_2():
    inputInt = int(input("Enter an int"))
    if (inputInt == 42):
        print("Correct answer")

def Task_1_3():
    inputInt = int(input("Enter an int"))
    if (inputInt % 2 == 0):
        print("This integer is odd")
    else:
        print("This integer is even")

def Task_1_4():
    inputStr = str(input("Enter a string"))
    if (inputStr == "open sesame"):
        print("access granted")
    elif (inputStr == "will you open, you goddamn !¤*@¡‘, display"):
        print("access fucking granted")
    else:
        print("permission denied")

def Task_1_5():
    inputInt = int(input("Enter an int"))
    if (inputInt == 42):
        print("OK")
    elif (inputInt >= 21):
        print("OK")
    elif (inputInt % 2 != 0):
        print("OK")
    elif (inputInt / 2 > 21):
        print("OK")
    elif (inputInt % 2 == 0 and inputInt >= 45):
        print("OK")
    else:
        print("You got wrong my poor friend!")

def Task_1_6():
    a = 42
    b = 41
    if a == b:
        print ("A and B are the sames ")
    if b <= a:
        print ("B is equal or lower as A")
    if b != a:
        print ("B his different from A")

def Task_2_1():
    for i in range(1,1000):
        print(i)

def Task_2_2():
    inputStr = str(input("Enter a string"))
    finalStr = ""
    for letter in inputStr:
        finalStr += letter
        finalStr += letter
    print(finalStr)

def Task_2_3(number, maxNumber):
    list = []
    for num in range(maxNumber):
        if (num % number == 0):
            list.append(str(num))
    print(list)
    return list

#Task_2_3(7, 10000)

def Task_2_4():
    for num in range(-30, 30):
        if (num % 3 == 0):
            print("Fizz")
        elif (num % 5 == 0):
            print("Buzz")
        elif(num % 3 == 0 and num % 5 == 0):
            print("FizzBuzz")
        else:
            print(num)

def Task_2_5():
    """re write the lyrics of the music"""
    number_bottles = 100
    while (number_bottles > 0):
        if (number_bottles > 1):
            print(f"{number_bottles} bottles of beer on the wall.")
            print(f"{number_bottles}bottles of beer on the wall.")
            print("Take one down, pass it around,")
            print(f"{number_bottles-1}bottles of beer on the wall.")
        else:
            print(f"{number_bottles} bottle of beer on the wall.")
            print(f"{number_bottles}bottle of beer on the wall.")
            print("Take one down, pass it around,")
            print(f"{number_bottles-1}bottle of beer on the wall.")
        
        number_bottles -= 1
    print("\n\nNo more bottles of beer on the wall, \n no more bottles of beer.\n We've taken them down and passed them around;\n now we're drunk and passed out!")


def Task_2_6():
    """diplays all the multiples smaller than inputint"""
    inputInt = int(input("Enter an integer"))
    list = ""
    for num in range(2, int(inputInt/2+1)):
        var = inputInt
        while (var - num >= 0):
            if (var % num == 0 and var != inputInt):
                list += str(var) + " "
                var -= num
            else:
                var -= 1  
        print(list)
        list = ""

#Task_2_6()


def challenge():
    list = "aeiouy"
    inputint = int(input("Enter an integer"))
    inputStr = str(input("Enter a string"))
    if (inputint == 0):
        return
    for letter in list:
        if (letter in inputStr):
            print(inputint)
    if (inputint >= 42):
        print(inputint)
    else:
        print(inputStr)


def Task_3_1():
    """encrypt any Caesar-ciphered text"""
    inputStr = str(input("Enter a string")).lower()
    inputInt = int(input("Enter a key as an integer"))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    finalMessage = ""

    for letter in inputStr:
        # if letter is in alphabet
        if letter in alphabet:
            # have old position and new
            position = alphabet.index(letter)
            newPosition = (position + inputInt) % 26
            finalMessage += alphabet[newPosition]
        else:
            # if not a letter, we put it with no change
            finalMessage += letter


def Task_3_2():
    """decrypt any Caesar-ciphered text"""
    inputStr = str(input("Enter a string")).lower()
    inputInt = int(input("Enter a key as an integer"))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    finalMessage = ""

    for letter in inputStr:
        # if letter is in alphabet
        if (letter in alphabet):
            # have old position and new
            position = alphabet.index(letter)
            newPosition = (position - inputInt) % 26
            finalMessage += alphabet[newPosition]
        else:
            # if not a letter, we put it with no change
            finalMessage += letter

def Task_3_3():
    """encrypt a text using a Vigenere code."""
    inputStr = str(input("Enter a string")).lower()
    inputKey = str(input("Enter a key as a string"))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    final_message = ""
    index_key = 0

    # find the letter who correspond to the true letter of the string by the method
    for letter in inputStr:
        if (letter in alphabet):
            position_aphabet = alphabet.index(letter)
            position_letter_key = alphabet.index(inputKey[index_key])
            final_message += alphabet[position_letter_key + position_aphabet]
            index_key += 1

    print(final_message)


def Task_3_3_decript():
    """decrypt a text using a Vigenere code."""
    inputStr = str(input("Enter a string")).lower()
    inputKey = str(input("Enter a key as a string"))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    final_message = ""
    index_key = 0

    # find the letter who correspond to the true letter of the string by the method
    for letter in inputStr:
        if (letter in alphabet):
            position_aphabet = alphabet.index(letter)
            position_letter_key = alphabet.index(inputKey[index_key])
            final_message += alphabet[position_letter_key - position_aphabet]
            index_key += 1

    print(final_message)

#def Task_3_4(text, key_length):
    





