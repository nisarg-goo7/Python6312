import turtle
bob = turtle.Turtle()
print(bob)

def square(t):
    for i in range(4):
        bob.fd(t)
        bob.lt(90)

square(200)

turtle.mainloop()