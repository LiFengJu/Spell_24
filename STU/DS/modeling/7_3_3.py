import gurobipy as gp
from gurobipy import GRB

# 创建模型
model = gp.Model()

# 定义决策变量
x = {}
for i in range(1, 6):
    for j in range(1, 4):
        x[i, j] = model.addVar(name=f'x{i}{j}', lb=0)

y = {}
for i in range(1, 5):
    y[i] = model.addVar(name=f'y{i}', vtype=GRB.BINARY)

# 更新模型，以包含新添加的变量
model.update()

# 添加约束
model.addConstr(sum(x[1, j] for j in range(1, 4)) <= 10 * y[1])
model.addConstr(sum(x[2, j] for j in range(1, 4)) <= 20 * y[2])
model.addConstr(sum(x[3, j] for j in range(1, 4)) <= 30 * y[3])
model.addConstr(sum(x[4, j] for j in range(1, 4)) <= 40 * y[4])
model.addConstr(sum(x[5, j] for j in range(1, 4)) <= 30)
model.addConstr(sum(x[i, 1] for i in range(1, 6)) == 30)
model.addConstr(sum(x[i, 2] for i in range(1, 6)) == 20)
model.addConstr(sum(x[i, 3] for i in range(1, 6)) == 20)

# 定义目标函数
model.setObjective(
    5 * x[1, 1] + 2 * x[1, 2] + 3 * x[1, 3] + 4 * x[2, 1] + 3 * x[2, 2] + 4 * x[2, 3] +
    9 * x[3, 1] + 7 * x[3, 2] + 5 * x[3, 3] + 10 * x[4, 1] + 4 * x[4, 2] + 2 * x[4, 3] +
    8 * x[5, 1] + 4 * x[5, 2] + 3 * x[5, 3] + 175 * y[1] + 300 * y[2] + 375 * y[3] + 500 * y[4],
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

