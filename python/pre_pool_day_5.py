"""
    LETULZEAU Baptiste
    EPITECH day 5 python
"""


import random
import time

def Task_1_1():
    list = [5,6,7,8,9]
    print(list[0])

def Task_1_2():
    list = [5,6,7,8,9]
    print(list[-1])

def Task_1_3():
    list = [5,6,7,8,9]
    list.append(6)

def Task_1_4():
    list = [5,6,7,8,9]
    for i in list:
        print(i)

def Task_1_5():
    list = [5,6,7,8,9]
    list.pop()
    for i in list:
        print(i)

def Task_1_6():
    list = [5,6,7,8,9]
    del(list[0])
    print(list)

def Task_1_7():
    list = [5,6,7,8,9]
    print(list[2:6])

def Task_1_8():
    list = [5,6,7,8,9]
    newList = []
    for i in range(len(list)):
        newList.append(i+len(list)-1)
    print(list[0])

def Task_1_9():
    list = [5,6,7,8,9]
    for i in range(0, len(list), 2):
        print(i)
    print(list)

def Task_1_10():
    list = [5,6,7,8,9]
    for i in range(18):
        list.append(i)

def Task_1_11():
    my_first_list = [4 , 5 , 6]
    my_second_list = [1 , 2 , 3]
    # add elements of an iterable
    my_first_list.extend(my_second_list)

def Task_2_1():
    """multiplication of all number of the list"""
    list = [5,6,7,8,9]
    multiplication = 0
    for i in range(len(list)):
        multiplication += list[i] * list[i+1]
    print(multiplication)

def Task_2_2():
    # it's a for but in line
    [x + 10 for x in [3, 2, 6, 7, 1, 4]]

def Task_2_3():
    # elevate each element ²
    list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4]))

def Task_2_4():
    """sort the list descending"""
    list = [5,6,7,8,9]
    for i in range(len(list)):
        for j in range(0, len(list) - i - 1):
            if (list[j] < list[j+1]):
                smallest = list(j)
            if (list[j] > list[j+1]):
                biggest = list(j)
    print(smallest)
    print(biggest)

def Task_2_5():
    # sort the list with number smaller to 7 
    list = [5,6,7,8,9]
    newList = []
    for i in list:
        if (i < 7):
             newList.append(i)
    print(newList)

def Task_2_6():
    """sort a list descending"""
    list = [5,6,7,8,9]
    for i in range(len(list)):
        for j in range(0, len(list) - i - 1):
            if (list[j] > list[j+1]):
                old = list[j]
                list[j] = list[j + 1]
                list[j + 1] = old
    print(list)

def Task_2_7():
    [x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]]
    # it is like that
    for x in [42, 3, 4, 18, 3, 10]:
        if x % 2 == 0:
            x // 2
        else:
            x * 2

def Task_2_8():
    # the list is filtered by all number > 10
    list(filter(lambda x: x > 10, [42, 3, 4, 18, 3, 10]))

def Task_2_9():
    # print each number with his index
    print([*enumerate([42, 3, 4, 18, 3, 10])])

def Task_2_10():
    """it associates names with firstnameswith lastnames descending"""
    first_name = [" Jackie ", " Bruce ", " Arnold ", " Sylvester "]
    last_name = [" Stallone ", " Schwarzenegger ", " Willis ", " Chan "]
    magic = [* zip ( first_name , last_name [:: -1]) ]
    print(magic[0])
    print(magic[3])
    print(magic[1][0])
    print(magic[0][1])
    print(magic[2])

def challenge():
    """sort the list of 1000000random descending"""
    startingTime = time.time()
    list_random = [random.randint(1, 100) for _ in range(1000000)]

    for i in range(len(list_random)):
        for j in range(0, len(list_random) - i - 1):
            if (list_random[j] > list_random[j+1]):
                old = list_random[j]
                list_random[j] = list_random[j + 1]
                list_random[j + 1] = old
    print(list_random)
    print(duration = time.time()- startingTime)

#challenge()

def Task_3_2():
    """sort the dict by differents way"""
    students = [
        { 
            "name" : "Baptiste", 
            "academic_year" : "3", 
            "units" : [ 
                {
                    "name": "Web Development",
                    "credits": 4,
                    "grade": "A"
                }
            ],
            "total_credits" : 4,
            "GPA" : 4.0
        },
        { 
            "name" : "clement", 
            "academic_year" : "5", 
            "units" : [ 
                {
                    "name": "Java",
                    "credits": 2,
                    "grade": "D"
                }
            ],
            "total_credits" : 4,
            "GPA" : 4.0
        },
        { 
            "name" : "gabriel", 
            "academic_year" : "1", 
            "units" : [ 
                {
                    "name": "python",
                    "credits": 3,
                    "grade": "B"
                }
            ],
            "total_credits" : 4,
            "GPA" : 4.0
        },   
    ]

    grade_weight_mapping = { 
        "A" : "4",
        "B" : "3",
        "C" : "2",
        "D" : "1",
        "E" : "0"
    }

    # differents sorted dict
    alphabetical_order = sorted(students, key = lambda student : student["name"])
    sorted_by_gpa_ascending = sorted(students.values(), key = lambda student : student["GPA"])
    sorted_by_gpa_descending = sorted(students, key = lambda student : student["GPA"], reverse=True)
    print(alphabetical_order)
    print(sorted_by_gpa_ascending)
    print(sorted_by_gpa_descending)

#Task_3_2()

def Task_4_1():
    """verify if the name is in the list"""
    list = ["clement", "baptiste", "gaby", "hugo"]
    inputStr = str(input("Enter a string"))
    if (inputStr in list):
        print("welcome in")
    else:
        print("get lost!")

def Task_4_2():
    """delete names dupplicated"""
    listNames = ["clement", "baptiste", "gaby", "hugo", "clement"]
    list = []
    for name in listNames:
        if (name not in list):
            list.append(name)
    print(list)

def Task_4_3():
    """take a name in input, and verify if it is in our dict"""
    meetings = [
        ["Monday", "3:30 PM", "Joe", "Théo"],
        ["Tuesday", "2:00 PM", "Joe", "Gabriel"],
        ["Wednesday", "5:00 PM", "Clement", "Mathias"],
        ["Thursday", "1:30 PM", "Paul", "Pierre"],
        ["Friday", "6:00 AM", "Henri", "Paolo"],
        ["Saturday", "6:00", "Michel", "Enzo"],
        ["Sunday", "10:00 AM", "Jordan", "Jackson"]
    ]

    given_name = str(input("Enter a name"))
    # format the input's name
    nameFormatted = given_name[0].upper() + given_name[1:]
    list = []

    # browse meetings 
    for i in meetings:
        if (nameFormatted in i):
            list.append(i)

    # response
    if (list.isEmpty()):
        print(f"{nameFormatted} not return result")
    else:
        print(f"{nameFormatted} is in the metting {list}")

#Task_4_3()


