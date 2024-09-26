def sumP(itérations):
    """fonction which sums numbers with power"""
    total_sum = 0
    current_number = ""
    for i in range(itérations):
        current_number += "1"
        total_sum += int(current_number)
    return total_sum


# sumP()


def calculate():
    str = ""
    str += 42 / 4
    print(str)
    print()
    str += 42 // 4
    print(str)
    print()
    str += 42 % 4
    print(str)


# calculate()


def pairorimpair(number):
    """check if a number is odd or even"""
    # if the rest == 0 its even else its odd
    if number % 2 == 0:
        print("even")
    else:
        print("odd")


# pairorimpair(4)


def sum(number):
    """calculates the sum of the digits"""
    compteur = 0
    # convert int to str to browse the list
    string = str(number)
    for i in string:
        # convert str to int to add it in the counter
        compteur += int(i)
    print(compteur)


# sum(64356789)


def decimal(number):
    """extracts the decimal part of the following numbers"""
    return number - int(number)


# decimal(12.45)


def pi(number):
    """calculate the number of PI"""
    res = 0
    for i in range(number):
        # find the sign of the number
        sign = (-1) ** i
        res += sign / (2 * i + 1)
    pi = 4 * res
    print(pi)


# pi(4000000)


def recursif(nb_iterations, param=1):
    """calculate the number of PI more precisely"""
    rayon = 6
    if nb_iterations == 0:
        return 0
    else:
        # recursive method to reach a number more and more precise
        return (param**2) / (rayon + recursif(nb_iterations - 1, param + 2))


# print(str(3 + recursif(100))[:8])


def sortList(liste):
    """sort localy the list degresing and increasing by changing the direction of the chevron in the 'if'"""
    for i in range(len(liste)):
        # compare the number with others
        for j in range(0, len(liste) - i - 1):
            # switch current number with the next
            if liste[j] > liste[j + 1]:
                ancien = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = ancien
    return liste


# print(sortList([89, 3]))
print(sortList([8, 9, 8, 2, 6, 4, 8, 2, 0, 3]))
