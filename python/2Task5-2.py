import turtle
bob = turtle.Turtle()
print(bob)

def square(length,n):
    for i in range(4):
        bob.fd(length)
        bob.lt(360/n)

square(100, 5)

turtle.mainloop()