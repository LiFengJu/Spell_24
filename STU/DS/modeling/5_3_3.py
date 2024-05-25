import gurobipy as gp
from gurobipy import GRB

# 创建模型
model = gp.Model()

# 定义变量
FS = model.addVar(name="FS", lb=0)
IB = model.addVar(name="IB", lb=0)
LG = model.addVar(name="LG", lb=0)
LV = model.addVar(name="LV", lb=0)
SG = model.addVar(name="SG", lb=0)
SV = model.addVar(name="SV", lb=0)

R = {}
for i in range(1, 6):
    R[i] = model.addVar(name=f"R{i}", lb=2)

# 更新模型，以包含新添加的变量
model.update()

# 添加约束
model.addConstr(10.06 * FS + 17.64 * IB + 32.41 * LG + 32.36 * LV + 33.44 * SG + 24.56 * SV == R[1])
model.addConstr(13.12 * FS + 3.25 * IB + 18.71 * LG + 20.61 * LV + 19.40 * SG + 25.32 * SV == R[2])
model.addConstr(13.47 * FS + 7.51 * IB + 33.28 * LG + 12.93 * LV + 3.85 * SG - 6.70 * SV == R[3])
model.addConstr(45.42 * FS - 1.33 * IB + 41.46 * LG + 7.06 * LV + 58.68 * SG + 5.43 * SV == R[4])
model.addConstr(-21.93 * FS + 7.36 * IB - 23.26 * LG - 5.37 * LV - 9.02 * SG + 17.31 * SV == R[5])

# 添加额外约束
model.addConstr(FS + IB + LG + LV + SG + SV == 1)

# 定义目标函数
model.setObjective(0.2 * sum(R[i] for i in range(1, 6)), sense=GRB.MAXIMIZE)

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
