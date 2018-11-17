from turtle import *
canvas = Screen()
canvas.setup()
circle = Turtle()
circle.shape("turtle")



while(0==0):
    n = int(input("Number of sides(integer):"))
    r = 512
    side = (r/n)
    regang = (((n-2)*180)/n)
    rotang = (180-regang)
    cycln = 0

    while cycln < n:
        circle.forward(side)
        circle.left(rotang)
        cycln = cycln + 1
        break


    canvas.exitonclick()
    break