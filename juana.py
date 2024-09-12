import turtle
import tkinter as tk
from tkinter import messagebox

def draw_sunflower():
    turtle.speed(20)
    turtle.bgcolor("black")
    turtle.hideturtle()
    
    turtle.color("white")  
    turtle.penup()
    turtle.goto(-180, 250)  
    turtle.pendown()
    turtle.write(header_text, align="center", font=("Impact", 12, "normal"))

    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.color("green")
    turtle.begin_fill()
    turtle.rt(90)
    turtle.fd(400)
    turtle.lt(90)
    turtle.fd(20)
    turtle.lt(90)
    turtle.fd(400)
    turtle.lt(90)
    turtle.fd(20)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    h = 0
    for i in range(16):
        for j in range(18):
            turtle.color("purple") 
            h += 0.005
            turtle.rt(90)
            turtle.circle(150 - j * 6, 90)
            turtle.lt(90)
            turtle.circle(150 - j * 6, 90)
            turtle.rt(180)
        turtle.circle(40, 24)

    # Colorear el centro de marrón
    turtle.penup()
    turtle.goto(-20, 0)
    turtle.pendown()
    turtle.color("dark brown")
    turtle.begin_fill()
    turtle.circle(44)  # Ajustar el radio del centro
    turtle.end_fill()
    turtle.done()

def show_sunflower():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter

    # Preguntar al usuario si quiere ver el girasol
    response = messagebox.askyesno("Mostrar Girasol", "¿Quieres ver algo lindo?")
    
    if response:
        draw_sunflower()
    else:
        root.destroy() 

header_text = "PA TI CORAZON"
show_sunflower()
