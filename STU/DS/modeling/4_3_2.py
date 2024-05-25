import gurobipy as gp
from gurobipy import GRB

# 创建模型
model = gp.Model()

# 定义变量
x = {(i, j): model.addVar(name=f'x{i}{j}', lb=0) for i in range(1, 4) for j in range(1, 4)}
s = {(i, j): model.addVar(name=f's{i}{j}', lb=0) for i in range(1, 4) for j in range(1, 4)}
I = {i: model.addVar(name=f'I{i}', lb=0) for i in range(1, 4)}
D = {i: model.addVar(name=f'D{i}', lb=0) for i in range(1, 4)}

# 更新模型，以包含新添加的变量
model.update()

# 添加约束
model.addConstr(500 + x[1, 1] - s[1, 1] == 1000)
model.addConstr(200 + x[2, 1] - s[2, 1] == 1000)
model.addConstr(x[1, 1] - s[1, 1] == 500)
model.addConstr(x[2, 1] - s[2, 1] == 800)
model.addConstr(s[1, 1] + x[1, 2] - s[1, 2] == 3000)
model.addConstr(s[2, 1] + x[2, 2] - s[2, 2] == 500)
model.addConstr(s[1, 2] + x[1, 3] - s[1, 3] == 5000)
model.addConstr(s[2, 2] + x[2, 3] - s[2, 3] == 3000)
model.addConstr(s[1, 3] >= 400)
model.addConstr(s[2, 3] >= 200)
model.addConstr(0.10 * x[1, 1] + 0.08 * x[2, 1] <= 4000)
model.addConstr(0.10 * x[1, 2] + 0.08 * x[2, 2] <= 500)
model.addConstr(0.1 * x[1, 3] + 0.08 * x[2, 3] <= 600)
model.addConstr(0.05 * x[1, 1] + 0.07 * x[2, 1] <= 300)
model.addConstr(0.05 * x[1, 2] + 0.07 * x[2, 2] <= 300)
model.addConstr(0.05 * x[1, 3] + 0.07 * x[2, 3] <= 300)
model.addConstr(2 * s[1, 1] + 3 * s[2, 1] <= 10000)
model.addConstr(2 * s[1, 2] + 3 * s[2, 2] <= 10000)
model.addConstr(2 * s[1, 3] + 3 * s[2, 3] <= 10000)
model.addConstr((x[1, 1] + x[2, 1]) - 2500 == I[1] - D[1])
model.addConstr((x[1, 2] + x[2, 2]) - (x[1, 1] + x[2, 1]) == I[2] - D[2])
model.addConstr((x[1, 3] + x[2, 3]) - (x[1, 2] + x[2, 2]) == I[3] - D[3])

# 定义目标函数
model.setObjective(
    20 * x[1, 1] + 20 * x[1, 2] + 20 * x[1, 3] + 10 * x[2, 1] + 10 * x[2, 2] + 10 * x[2, 3] +
    0.3 * s[1, 1] + 0.3 * s[1, 2] + 0.3 * s[1, 3] + 0.15 * s[2, 1] + 0.15 * s[2, 2] + 0.15 * s[2, 3] +
    0.5 * I[1] + 0.50 * I[2] + 0.5 * I[3] + 0.2 * D[1] + 0.2 * D[2] + 0.2 * D[3],
    sense=GRB.MINIMIZE
)

# 求解
model.optimize()

# 输出结果
if model.status == GRB.OPTIMAL:
    print("Optimal Objective Value:", model.objVal)
    print("Optimal Solution:")
    for var in model.getVars():
        print(f"{var.varName}: {var.x}")
else:
    print("No optimal solution found.")
