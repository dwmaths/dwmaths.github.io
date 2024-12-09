from random import random, choice
import matplotlib.pyplot as plt

def generer_points(zone=3, disp=2):
    res = []
    
    centres = [(10*random(), 10*random()) for _ in range(zone)]
    
    for _ in range(200):
        c = choice(centres)
        x = c[0] + (2*random()-1)*disp
        y = c[1] + (2*random()-1)*disp
        res.append((x, y))
        
    return res

points = generer_points(zone=3, disp=2)
x = [elt[0] for elt in points]
y = [elt[1] for elt in points]

plt.axis([-2, 12, -2, 12])
plt.scatter(x, y)

plt.show()