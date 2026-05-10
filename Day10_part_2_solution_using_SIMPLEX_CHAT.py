
# I decided to use the simplex but I let ChatGPT generate the code for it 
import pulp

# Create the MILP problem
prob = pulp.LpProblem("Integer_LP", pulp.LpMinimize)

# Variables: integer and non-negative
k = pulp.LpVariable.dicts("k", range(6), lowBound=0, cat='Integer')

# Objective: minimize sum(k_i)
prob += pulp.lpSum([k[i] for i in range(6)])

# Matrix A
A = [
    [0,0,0,0,1,1],
    [0,1,0,0,0,1],
    [0,0,1,1,1,0],
    [1,1,0,1,0,0]
]

# RHS b
b = [7,5,12,7,2]#3, 5, 4, 7]

# Add equality constraints A*K = b
for row in range(4):
    prob += pulp.lpSum(A[row][col] * k[col] for col in range(6)) == b[row]

# Solve
prob.solve(pulp.PULP_CBC_CMD(msg=0))

# Print result
print("Status:", pulp.LpStatus[prob.status])
solution = [pulp.value(k[i]) for i in range(6)]
print("Optimal K =", solution)
print("Objective value =", sum(solution))