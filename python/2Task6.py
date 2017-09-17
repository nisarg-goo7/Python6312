import turtle
bob = turtle.Turtle()
bob.delay = 0.01 
print bob  
 		 		

def polygon(t, length, n): 	
    for i in range(n): 		
        fd(t, length) 		
        lt(t, 360 / n) 		 

def circle(t, r): 	
    circumference = 2 * math.pi * r 	
    n = int(circumference) 	
    polygon(t, 1, n) 		 

circle(bob, 30)  

