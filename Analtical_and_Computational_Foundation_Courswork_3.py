
import random
import sympy

def estimate_pi_monte_carlo(Ntotal):
    if type (Ntotal) != int or Ntotal <= 0:
        raise ValueError
#The code below is just giving the parameter of the squar to be between -1 and 1 for both height and the base
    points = [(random.uniform(-1,1),random.uniform(-1,1)) for _ in range(Ntotal)]
    return sympy.Rational(4*sum([1 for point in points if point[0]**2 +point[1]**2 <= 1]), Ntotal)    


import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Circle,Rectangle
def draw_monte_carlo(Ntotal):
    fig = plt.figure(figsize =(10,5))
#_______________________________________________________________________
# Left Subplot for the actual areas of the circle and Rectangle     
    ax = fig.add_subplot(121)
    rect= Rectangle((-1,-1),2,2, color = "red")
    cir = Circle((0,0),1,color="green")
    ax.add_patch(rect)
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.add_patch(cir)
    ax = fig.add_subplot(122)
#_______________________________________________________________________
# Estimatation of the Monti carlo aprroximation
    x, y = [random.uniform(-1,1) for _ in range(Ntotal)], [random.uniform(-1,1) for _ in range(Ntotal)]
    xy = zip(x,y)
    colour = ["green" if a[0]**2 +a[1]**2 <= 1 else "red" for a in xy]
    ax.scatter(x, y, color = colour)
    ax.add_patch(Circle((0,0),1,color ="blue", fill=False))
    ax.set_xlabel("x")    
    ax.set_xlim(-1,1)
    ax.set_ylabel("y")
    ax.set_ylim(-1,1)
#_______________________________________________________________________
#Plot the Two graphs
    fig.suptitle("Monte Carlo Approximation of Pi")
    plt.show()
    fig.savefig('outputimage.png')
# Call the plotting function
draw_monte_carlo(250)

def estimate_pi_chudnovsky(n):
# Validation of the input
    if type(n) != int or n<= 0:
        raise ValueError
#Constants
    a = sympy.Rational(13591409)
    i = sympy.symbols('i')
    b = sympy.Rational(545140134)
    c = sympy.Rational(640320)
# makes sure we have a higher precision, mostly that of 1,000 or above. I Chose 10**4 because its fun to more accurate
#__________________________________________________________________________________________________________
    #Simplify the whole function by spliting the function into two parts the numerator and denominator, makes the code more easy to observe.
    num = sympy.sympify(((-1)**i)*(sympy.factorial(6*i))*(a+b*i))
    den = sympy.sympify((sympy.factorial(3*i))*((sympy.factorial(i))**3)*c**((3*i)+sympy.Rational(3,2)))
    #The function is bellow in the simplest form.       
    The_Function = sympy.sympify(num/den)
    The_summation = sympy.Sum(The_Function,(i,0,n))
    #The aprox_tion is just a rough estimate of pi up to 10000 digits
    aprox_tion = (sympy.Rational(12)*The_summation.doit()).evalf(10**4)
    return sympy.Float(aprox_tion**-1,10**4)