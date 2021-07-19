# FRAKTALE
# 22-05-2021
# TWORZENIE GAŁĘZi

from turtle import Screen, Turtle

def drzewo(turtle, krok, skroc, kat):
    if krok > WARTOSC:
        turtle.forward(krok)
        nastepny_krok = krok - skroc * 0.5
        turtle.right(kat)
        drzewo(turtle, nastepny_krok, skroc, kat)
        turtle.left(kat * 2)
        drzewo(turtle, nastepny_krok, skroc, kat)
        turtle.right(kat)
        turtle.backward(krok)

if __name__ == "__main__":

    WARTOSC = 30

    # INICJACJA EKRANU
    widok = Screen()
    
    # SZEROKOŚĆ, WYSOKOŚĆ, POŁOŻENIE
    widok.setup(1920, 1080, 0, 0)

    # INICJACJA ŻÓŁWIA
    turtle = Turtle()

    # ZWROT
    turtle.setheading(90)

    # WIDOCZNOŚĆ
    turtle.hideturtle()

    # PRĘDKOŚĆ RYSOWANIA
    turtle.speed(500)

    # KOLOR
    turtle.color('black')

    drzewo(turtle, 50, 5, 25)

    input('')
