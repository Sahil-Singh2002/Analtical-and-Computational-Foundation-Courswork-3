# Analtical and Computational 3

**Introduction**

It is possible to use different methods to compute approximations to π. One way is to use the so-called Monte Carlo method which uses random numbers to estimate π. Consider the left-hand figure below, which shows the unit disc inscribed in the square [−1,1]×[−1,1]. 
![Screenshot 2023-04-01 152509](https://user-images.githubusercontent.com/125428501/229295056-4d7b6dce-06bb-4794-971e-7e7ecc3ceaba.png)

Denote the areas of the square and disc by As and Ad, respectively. Then of course As = 4 and Ad = π so Ad/As=π/4. In the right-hand figure, a set of *N*_total random points (uniformly distributed) have been plotted on the unit square. The points inside and outside the disc are coloured green and red, respectively. If the number of points inside the disc is denoted *N*_disc, then the ratio of *N*_disc to *N*_total is an approximation of the ratio of areas above, namely *N*_disc/*N*_total ≈ Ad/As = π/4. This implies π ≈ 4*N*_disc/*N*_total.
**CODE**
* The function `estimate_pi_monte_carlo` which implements an algorithm for estimating π by generating a sequence of *N*_total uniformly distributed random numbers in the square [−1,1]×[−1,1], counting how many of those points land inside the unit circle, and then returning an approximation to π given by the formula above. The function should:
  - Take the number *N*_total as input and raise a ValueError if the input is not a positive integer.
  - return a rational number in the form of a `sympy.Rational`.
* Now we Illustrate the Monte Carlo method of approximating π by writing a function `draw_monte_carlo` which takes as input *N*_total and draws the figures included above with two subplots of the square [−1,1]x[−1,1]. 
  - The left subplot would contain a green circle and the rest red.
  - The right subplot would contain a scatter plot of N_{total} uniformly distributed random points.
  - The points inside the unit circle would be coloured green and points outside coloured red.
  - The unit circle itself will be coloured blue.
* There are many many ways to approximate π. One of the most efficient algorithms is using the following partial sums bellow. The convergence is very rapid. Versions of this algorithm are used for all record-breaking calculations for digits of π. So I wrote a function `estimate_pi_chudnovsky` which uses this formula to approximate π. The function should use `SymPy`, take a non-negative integer n as input and return an estimate of π given as a SymPy float with at least 1000 digits precision. The function will raise a ValueError if the input is not a non-negative integer.
 ![Screenshot 2023-04-01 151922](https://user-images.githubusercontent.com/125428501/229294718-a16af7fe-3c14-495f-95bb-5aa3a023477c.png)
 
**Conclusion**
Both algoritms are designed tp help compute a strong numerical approximation of π. With chudnovsky method deminstrating a rapid convergence to the solution π. In our code we demand a minimum of 1,000 digits precision. 

  
