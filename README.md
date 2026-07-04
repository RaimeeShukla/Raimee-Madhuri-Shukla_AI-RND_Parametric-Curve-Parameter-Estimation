# AI R&D Assignment

Parameter estimation of a parametric curve using numerical optimization.

Objective:
Estimate the unknown parameters θ, M and X of a parametric curve from the provided dataset and reconstruct the original curve as accurately as possible.

Problem Statement:
Given - Parametric equation, unknown parameters (θ, M and X) with their ranges, dataset containing (x,y) points of the original curve.
To Solve - Estimate the unknown parameters that generated the provided dataset.

Dataset:
The provided dataset contains 1501 x and y coordinates to construct the original curve.

Understanding the Problem:
Initially I viewed the assignment as solving for three unknown values.
After analysing the mathematical formulation, I realised that the problem is actually a parameter estimation problem.

Initial Research:
Before trying to implement the solution, I wanted to understand the mathematics behind the problem.

Topics Studied-
- Parametric equations
- Objective/Loss functions
- Numerical optimization
- Gradient Descent
- Stochastic Gradient Descent

Resources-

- Parametric Equations
  https://www.youtube.com/playlist?list=PLSQl0a2vh4HDr-27pzzhO4DsZ6InbyExI

- Gradient Descent
  https://www.youtube.com/watch?v=sDv4f4s2SB8


Solution Strategies:
Following are the initial strategies I could think of-
1) Brute Force - Iterate through all possible combinations of θ, M, and X within their specified ranges. For each parameter combination, generate the predicted curve, compute the error between the predicted curve and the observed data, and retain the parameter set that produces the minimum error.

   Disadvantage - This approach is computationally expensive because the number of parameter combinations grows rapidly as more parameters are added.

2) Sequential Parameter Optimization - Start with an initial estimate of the parameters and optimize one parameter at a time while keeping the remaining parameters fixed. Repeat this process for all three parameters until the overall error no longer decreases significantly.

   Advantage - Reduces the search space compared to exhaustive search.
   Disadvantage - May converge to a locally optimal solution because the parameters are not optimized simultaneously.

3) Gradient Descent - Gradient Descent is an iterative optimization algorithm that updates the parameter values in the direction that most rapidly decreases the objective function. Starting from an initial estimate, the parameters are repeatedly updated until the loss converges or no significant improvement is observed.

   Advantage: More efficient than exhaustive search for continuous optimization problems.

4) Stochastic Gradient Descent - Instead of computing the gradient using the entire dataset at every iteration, SGD estimates the gradient using only a small subset of the data. This significantly reduces the computational cost of each iteration and often leads to faster optimization on large datasets.

   Advantage: Lower computational cost per iteration compared to standard Gradient Descent.

Initial Algorithm:
The initial algorithm formulated is provided in algorithm/initial_algorithm.png

Dataset Vizualization:
Next, I plotted the curve with the given data points from the csv file. The plot is stored in path dataset/plot_xy_data.png

Updated Conclusion:
The implemented loss function computes the average L1 distance between corresponding points of the generated and observed curves. This objective function will be minimized during parameter estimation.