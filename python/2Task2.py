import turtle
bob = turtle.Turtle()
print(bob)

def square(t, length):
    for i in range(4):
        bob.fd(t, length)
        bob.lt(t)

square(bob, 200)

turtle.mainloop()