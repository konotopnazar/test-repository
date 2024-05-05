from turtle import *

if __name__ == '__main__':
    a = 200
    def draw():
        fd(a)
        left(120)
        fd(a)
        left(120)
        fd(a)
        left(120)


    while a >= 20:
        draw()
        a -= 20

# Привіт Назар