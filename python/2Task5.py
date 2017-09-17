import turtle
bob = turtle.Turtle()
print(bob)

def square(t, length,n):
    for i in range(4):
        bob.fd(length)
        bob.lt(360/n)
		

square(bob, 200)

turtle.mainloop()