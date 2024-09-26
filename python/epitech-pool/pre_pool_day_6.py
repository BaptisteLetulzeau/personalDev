"""
    LETULZEAU Baptiste
    EPITECH day 6 python
"""


import time
import os


def Task_1_1():
    """multiples uses of fonctions"""
    def f ( x ) :
        return 2 * x + 1
    def g () :
        return 7
    y = f (2)
    print ( y )
    y = f (5) + g ()
    print ( y )


def Task_1_2():
    """classic burger"""
    def bread () :
        print (" <////////// > ")
    def lettuce () :
        print (" ~~~~~~~~~~~~ ")
    def tomato () :
        print ("O O O O O O")
    def ham () :
        print (" ============ ")

    bread() + lettuce() + tomato() + ham() + bread()


def Task_1_3():
    """classic burger 42 times"""
    def bread () :
        print (" <////////// > ")
    def lettuce () :
        print (" ~~~~~~~~~~~~ ")
    def tomato () :
        print ("O O O O O O")
    def ham () :
        print (" ============ ")

    for i in range(42):
        bread() + lettuce() + tomato() + ham() + bread()


def Task_1_4(param):
    """classic burger param times"""
    def bread () :
        print (" <////////// > ")
    def lettuce () :
        print (" ~~~~~~~~~~~~ ")
    def tomato () :
        print ("O O O O O O")
    def ham () :
        print (" ============ ")

    for i in range(param):
        bread() + lettuce() + tomato() + ham() + bread()


def Task_1_5(count, veggie):
    """make a burger in case of the person wants a veggie burger or not"""
    def bread () :
        print (" <////////// > ")
    def lettuce () :
        print (" ~~~~~~~~~~~~ ")
    def tomato () :
        print ("O O O O O O")
    def ham () :
        print (" ============ ")
    
    for i in range(count):
        if (not veggie):
            bread() + lettuce() + tomato() + ham() + bread()
        else:
            bread() + lettuce() + tomato() + lettuce() + bread()


def challenge(number, power):
    """power of a number, 42**84 = 0.0005159378051757812s"""
    startingTime = time.time()
    print(number ** power)
    print(time.time()- startingTime)


def Task_2_1(string):
    """test if the string is a palindrome"""
    def is_palindrome(s):
        s = ''.join(char.lower() for char in s if char.isalnum())
    
        # recursive
        def helper(first_carac, last_carac):
            if first_carac >= last_carac:
                return True
            
            # if they are the same
            if s[first_carac] != s[last_carac]:
                return False
            
            # continue with the next two carac
            return helper(first_carac + 1, last_carac - 1)

        return helper(0, len(s) - 1)
    
    return is_palindrome(string)

# print(Task_2_1("kayak"))
# print(Task_2_1("never odd or even")) 


def Task_2_2():
    """print all files in the current directory"""
    files = [f for f in os.listdir() if os.path.isfile(f)]

    print(files)


# Task_3_1() below
def lower(s, n):
    count = 0
    for letter in (s):
        if (letter.islower()):
            count += 1
    return count >= n
def funB(s, n):
    count = 0
    for letter in (s):
        if (letter.isupper()):
            count += 1
    return count >= n
def funC(s, n):
    if (len(s) != n):
        return False
    else:
        return True
def special(s, n):
    compteur = sum(1 for char in s if not char.isalnum())

    return compteur >= n
def funE(s, n):
    compteur = sum(1 for char in s if not char.isdigit())

    return compteur == n


def Task_3_2():
    """check if the password contains n special caracters or n lower letters"""
    def check_password(function, number, string):
        print(function(string, number))
        return function(string, number)
        
    check_password(lower, 4, "mysecretpassword") and check_password(special, 2, "mysecretpassword")

#Task_3_2()

