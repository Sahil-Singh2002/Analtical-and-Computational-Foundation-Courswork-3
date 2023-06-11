# Estimating $π$

**Introduction**

It is possible to use different methods to compute approximations to $π$. One way is to use the so-called Monte Carlo method which uses random numbers to estimate $π$. Consider the left-hand figure below, which shows the unit disc inscribed in the square $[-1, 1] \times [-1, 1]$. While one of the most efficient algorithms is using the following partial sums bellow. The convergence is very rapid. Versions of this algorithm are used for all record-breaking calculations for digits of $π$. So I wrote two functions which uses these algorithms to approximate $π$. The function should use `SymPy`, return an estimate of $π$ given as a SymPy float with at least 1000 digits precision for the second algorithm.
 
## Algorithms

$$\textbf{Monte Carlo Method}$$

One way to estimate the value of $π$ is by using the Monte Carlo method, which utilizes random numbers. 

The Monte Carlo method for estimating $π$ involves the following steps:

1. Consider a unit square $[-1, 1] \times [-1, 1]$ that contains a unit circle.
2. Generate a large number of random points uniformly distributed within the unit square.
3. Determine the number of points that fall within the unit circle.
4. Calculate the ratio of the number of points inside the circle to the total number of generated points.
5. Multiply this ratio by 4 to obtain an estimate of $π$.

The idea behind this method is based on the relationship between the areas of the square and the circle. Since the area of the square is known (4), the ratio of the areas of the circle to the square is equal to $\frac{\pi}{4}$. By randomly sampling points within the square and counting the number of points that fall within the circle, we can approximate this ratio and subsequently estimate the value of $π$.

Implementing the Monte Carlo method allows us to estimate $π$ by utilizing random numbers and basic geometric principles. This method is simple yet powerful and can provide accurate approximations of $π$ by increasing the number of generated points.

To implement the Monte Carlo method, you can use random number generators in your programming language of choice to generate points within the square and determine if they fall within the circle. By keeping track of the count of points inside the circle and the total number of generated points, you can calculate the estimated value of $π$.

$$\textbf{Chudnovsky Algorithm}$$

The Chudnovsky algorithm is a fast algorithm for computing the digits of $π$. It is based on the following infinite series representation of $π$:

```math
\frac{1}{\pi} = \frac{12}{\sqrt{640320^3}} \sum_{k=0}^{\infty} \frac{(-1)^k (6k)! (545140134k + 13591409)}{(3k)! (k!)^3 640320^{3k}}
```

The algorithm allows for the efficient computation of $π$ by calculating the terms of the series iteratively. By summing a sufficient number of terms, an increasingly accurate approximation of $π$ can be obtained.

The Chudnovsky algorithm is known for its rapid convergence and has been used to compute $π$ to billions (and even trillions) of decimal places. It is widely employed in high-precision computations and is one of the most efficient algorithms for calculating $π$.

To implement the Chudnovsky algorithm, you can use a loop or recursion to iterate through the terms of the series and sum them up. Keep in mind that the convergence of the algorithm improves as more terms are added to the sum. Additionally, efficient arithmetic operations are required to handle the large factorials and powers involved in the computation.

## Conclusion

Both algoritms are designed tp help compute a strong numerical approximation of $π$. With chudnovsky method deminstrating a rapid convergence to the solution $π$. In our code we demand a minimum of 1,000 digits precision.
