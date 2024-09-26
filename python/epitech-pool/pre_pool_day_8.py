"""
    LETULZEAU Baptiste
    EPITECH day 8 python
"""


import pyjokes
from turtle import *
import turtle
import pygame
import sys
import math

def Task_1_1():
    print(pyjokes.get_joke())


def Task_2_1():
    def square(height, colorr):
        "draw a square"
        color(colorr)
        width(10)
        faces =0
        while faces < 4:
            forward(height)
            right(90)
            faces += 1
    up()
    goto(-100,200)
    down()
    square(400,'blue')
    up()


def Task_2_2():
    # create an object for the screen and fix it the color black
    toto = turtle.Screen()
    toto.bgcolor("black")
    # create an object for the canva and fix it the color red
    titi = turtle.Turtle()
    titi.color("red")
    # draw 3 times
    for _ in range(3):
        titi.right(90)
        titi.circle(42)
        # leave the canva on click
    toto.exitonclick()


def Task_2_3():
    def draw_polygon(sides):
        color("red")
        width(10)
        angle = 360 / sides
        for _ in range(sides):
            forward(50)
            right(angle)
    
    up()
    goto(-100,200)
    down()
    draw_polygon(10)
    up()


def Task_2_4():
    """spiral form"""
    for i in range(360):
        forward(i)
        right(20)

def challenge():
    def triangle(side_length, depth):
        """triangle recursive"""
        angle = 360 / 3
        color("black")
        width(1)
        if (depth == 0):
            for _ in range(3):
                forward(side_length)
                right(angle)
        else:
            triangle(side_length / 2, depth - 1)
            turtle.forward(side_length / 2)
            triangle(side_length / 2, depth - 1)
            turtle.backward(side_length / 2)
            turtle.left(60)
            turtle.forward(side_length / 2)
            turtle.right(60)
            triangle(side_length / 2, depth - 1)
            turtle.left(60)
            turtle.backward(side_length / 2)
            turtle.right(60)

    speed(0)
    up()
    goto(-200, -150)
    down()

    triangle(400, 3)

#challenge()



def Task_3_5():
    """draw a stickman"""
    width(2)
    color("black")

    pygame.init()

    screen = pygame.display.set_mode((400, 400))

    white = (255, 255, 255)

    black = (0, 0, 0)

    def draw_stickman(screen):

        # head
        pygame.draw.circle(screen, black, (200, 100), 30, 2)

        # eyes
        pygame.draw.circle(screen, black, (190, 90), 4, 2)
        pygame.draw.circle(screen, black, (210, 90), 4, 2)

        # smile
        pygame.draw.arc(screen, black, (185, 95, 30, 20), 3.14, 6.28, 2)

        # neck
        pygame.draw.line(screen, black, (200, 130), (200, 230), 2)

        # arm 1
        pygame.draw.line(screen, black, (200, 170), (150, 150), 2)

        # arm 2
        pygame.draw.line(screen, black, (200, 170), (250, 150), 2)

        # leg 1
        pygame.draw.line(screen, black, (200, 230), (150, 300), 2)

        # leg 2
        pygame.draw.line(screen, black, (200, 230), (250, 300), 2)

    running = True
    while running:
        # Remplir l'arrière-plan
        screen.fill(white)

        # Dessiner le stickman
        draw_stickman(screen)

        # Mettre à jour l'écran
        pygame.display.update()

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Quitter pygame
    pygame.quit()
    sys.exit()

# Task_3_5()


def rosace():
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)

    t.color("purple")

    def draw_flower():
        for _ in range(18):
            t.circle(100)
            t.left(20)

    draw_flower()

    screen.exitonclick()

    turtle.done()

rosace()

    

        
          


