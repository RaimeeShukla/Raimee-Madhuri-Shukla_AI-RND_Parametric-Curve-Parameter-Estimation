# AI R&D Assignment

## Parameter Estimation of a Parametric Curve using Numerical Optimization

## Objective
Estimate the unknown parameters θ, M and X of a parametric curve from the provided dataset and reconstruct the original curve as accurately as possible.

---

## How to run
## 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Execute the Program

```bash
python src/main.py
```

## Output

The program will:
- Load the provided dataset
- Generate the parametric curve
- Perform the baseline grid search optimization
- Estimate the values of θ, M, and X
- Print the estimated parameters and the corresponding L1 loss
- Generate a comparison plot between the observed and predicted curves (`final_curve.png`)

---

# Problem Statement
## Given -
1. Parametric equation
2. Unknown parameters (θ, M and X) with their ranges
3. Dataset containing (x,y) points of the original curve.

## To Solve - 
Estimate the unknown parameters that generated the provided dataset.

---

# Dataset
The provided dataset contains 1500 x and y coordinates to construct the original curve.

---

# Understanding the Problem
Initially I viewed the assignment as solving for three unknown values.
After analysing the mathematical formulation, I realised that the problem is actually a parameter estimation problem, where the objective is to recover the unknown parameters that generated the original curve.

---

# Initial Research
Before trying to implement the solution, I wanted to understand the mathematics behind the problem.

Topics Studied-
- Parametric equations
- Objective/Loss functions
- Numerical optimization
- Gradient Descent
- Stochastic Gradient Descent

---

# Learning Resources

**Parametric Equations**
  https://www.youtube.com/playlist?list=PLSQl0a2vh4HDr-27pzzhO4DsZ6InbyExI

**Gradient Descent**
  https://www.youtube.com/watch?v=sDv4f4s2SB8

---

# Solution Strategies
Following are the initial strategies I could think of-
## 1. Brute Force - 
Iterate through all possible combinations of θ, M, and X within their specified ranges. For each parameter combination, generate the predicted curve, compute the error between the predicted curve and the observed data, and retain the parameter set that produces the minimum error.

   Disadvantage - This approach is computationally expensive because the number of parameter combinations grows rapidly as more parameters are added.

## 2. Sequential Parameter Optimization - 
Start with an initial estimate of the parameters and optimize one parameter at a time while keeping the remaining parameters fixed. Repeat this process for all three parameters until the overall error no longer decreases significantly.

   Advantage - Reduces the search space compared to exhaustive search.
   Disadvantage - May converge to a locally optimal solution because the parameters are not optimized simultaneously.

## 3. Gradient Descent - 
Gradient Descent is an iterative optimization algorithm that updates the parameter values in the direction that most rapidly decreases the objective function. Starting from an initial estimate, the parameters are repeatedly updated until the loss converges or no significant improvement is observed.

   Advantage: More efficient than exhaustive search for continuous optimization problems.

## 4. Stochastic Gradient Descent - 
Instead of computing the gradient using the entire dataset at every iteration, SGD estimates the gradient using only a small subset of the data. This significantly reduces the computational cost of each iteration and often leads to faster optimization on large datasets.

   Advantage: Lower computational cost per iteration compared to standard Gradient Descent.

---

# Initial Algorithm
The initial algorithm formulated is provided in algorithm/initial_algorithm.png

---

# Dataset Visualization
Next, I plotted the curve with the given data points from the csv file. 
The plot is stored in path dataset/plot_xy_data.png

---

# Objective Function
The objective of the optimization is to minimize the L1 distance between the observed dataset and the generated parametric curve.
For every θ,M,X, steps followed:
1. Generate the predicted curve
2. Compare the predicted curve against the observed dataset
3. Compute the average L1 distance
4. Retain the parameter combination with the minimum loss

---

# Optimization Approach
A baseline search was implemented. This baseline provides a deterministic solution while serving as a foundation for more advanced optimization algorithms.

---

# Baseline Implementation
src/
1. data_loader.py - Loads the provided dataset
2. curve.py - Generates the parametric curve
3. loss.py - Computes the L1 loss
4. optimizer.py - Baseline grid search optimizer
5. main.py - Executes the complete pipeline

---

# Results from baseline search
Final Theta : 28
Final M : 0.020000000000000004
Final X : 54
Final Loss : 25.256421442724314

---

# Result Visualization
final_curve.png shows the original and the predicted curve comparison.

---

# Future Explorations
- Gradient Descent as an optimization technique instead of evaluating all parameter combinations
- Experiment with different step sizes for θ, M and X to balance computation time and accuracy
- Explore alternative loss functions, like L2 loss and compare their effect on parameter estimation