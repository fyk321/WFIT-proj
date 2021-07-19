# FRAKTALE
# 11-06-2021
# SMOK HEIGHWAYA

from turtle import Screen, Turtle

def smok():
    obieg = 0
    start = 'R'
    poprzedni = 'R'

    while obieg < 15:
        start = poprzedni + 'R'
        # ODWRÓCENIE KOLEJNOŚCI SEKWENCJI
        poprzedni = poprzedni[::-1]
           
        for x in range(0, len(poprzedni)):
            if poprzedni[x] == 'L':
                # DOPISANIE R W ŚRODKU SEKWENCJI
                poprzedni = poprzedni[:x] + 'R' + poprzedni[x + 1:]
            elif poprzedni[x] == 'R':
                # DOPISANIE L W ŚRODKU SEKWENCJI
                poprzedni = poprzedni[:x] + 'L' + poprzedni[x + 1:]

        start += poprzedni
        poprzedni = start
        obieg += 1
        
    kroki.append(start)
    
    return kroki

if __name__ == "__main__":

    kroki = []

    # INICJACJA ŻÓŁWIA
    turtle = Turtle()

    # INICJACJA EKRANU
    widok = Screen()
        
    # SZEROKOŚĆ, WYSOKOŚĆ, POŁOŻENIE EKRANU
    widok.setup(1920, 1080, 0, 0)

    # POŁOŻENIE ŻÓŁWIA
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()

    # ZWROT
    turtle.setheading(90)

    # WIDOCZNOŚĆ
    turtle.hideturtle()

    # PRĘDKOŚĆ RYSOWANIA
    turtle.speed(1000)

    # KOLOR
    turtle.color("black")

    kroki = smok()[0]
    turtle.forward(5)

    for i in range(0,len(kroki)):
        if kroki[i] == 'R':
            # ZWRÓCENIE ŻÓŁWIA W PRAWO
            turtle.right(90)
            turtle.forward(5)
        elif kroki[i] == 'L':
            # ZWRÓCENIE ŻÓŁWIA W LEWO
            turtle.left(90)
            turtle.forward(5)

    input('')
