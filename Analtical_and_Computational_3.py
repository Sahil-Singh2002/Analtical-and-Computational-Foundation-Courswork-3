import random
import sympy
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

def estimate_pi_monte_carlo(Ntotal):
    if not isinstance(Ntotal, int) or Ntotal <= 0:
        raise ValueError("Ntotal must be a positive integer")
    
    points = [(random.uniform(-1,1), random.uniform(-1,1)) for _ in range(Ntotal)]
    count = sum(1 for point in points if point[0]**2 + point[1]**2 <= 1)
    return sympy.Rational(4 * count, Ntotal)    

def draw_monte_carlo(Ntotal):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    
    rect = Rectangle((-1, -1), 2, 2, color="red")
    cir = Circle((0, 0), 1, color="green")
    axes[0].add_patch(rect)
    axes[0].set_xlim(-1, 1)
    axes[0].set_ylim(-1, 1)
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("y")
    axes[0].add_patch(cir)
    
    x = [random.uniform(-1, 1) for _ in range(Ntotal)]
    y = [random.uniform(-1, 1) for _ in range(Ntotal)]
    colours = ["green" if x[i]**2 + y[i]**2 <= 1 else "red" for i in range(Ntotal)]
    axes[1].scatter(x, y, color=colours)
    axes[1].add_patch(Circle((0, 0), 1, color="blue", fill=False))
    axes[1].set_xlabel("x")
    axes[1].set_xlim(-1, 1)
    axes[1].set_ylabel("y")
    axes[1].set_ylim(-1, 1)
    
    fig.suptitle("Monte Carlo Approximation of Pi")
    plt.show()
    fig.savefig('outputimage.png')

draw_monte_carlo(250)

def estimate_pi_chudnovsky(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    
    a = sympy.Rational(13591409)
    b = sympy.Rational(545140134)
    c = sympy.Rational(640320)
    
    i = sympy.symbols('i')
    num = (-1)**i * sympy.factorial(6*i) * (a + b*i)
    den = sympy.factorial(3*i) * (sympy.factorial(i)**3) * c**((3*i) + sympy.Rational(3, 2))
    
    The_Function = num / den
    The_summation = sympy.Sum(The_Function, (i, 0, n))
    approximation = (sympy.Rational(12) * The_summation.doit()).evalf(10**4)
    
    return sympy.Float(approximation**-1, 10**4)
