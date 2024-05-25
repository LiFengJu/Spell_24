import gurobipy as gp
from gurobipy import GRB

# 创建模型
model = gp.Model()

# 定义变量
BM = model.addVar(name="BM", lb=0)
BP = model.addVar(name="BP", lb=0)
FCM = model.addVar(name="FCM", lb=0)
FCP = model.addVar(name="FCP", lb=0)
TCM = model.addVar(name="TCM", lb=0)
TCP = model.addVar(name="TCP", lb=0)
FTM = model.addVar(name="FTM", lb=0)
FTP = model.addVar(name="FTP", lb=0)
TTM = model.addVar(name="TTM", lb=0)
TTP = model.addVar(name="TTP", lb=0)
OT = model.addVar(name="OT", lb=0)

# 更新模型，以包含新添加的变量
model.update()

# 添加约束
model.addConstr(BM + BP == 5000)
model.addConstr(FCM + FCP == 3000)
model.addConstr(TCM + TCP == 2000)
model.addConstr(FTM + FTP == 3000)
model.addConstr(TTM + TTP == 2000)
model.addConstr(OT <= 50)
model.addConstr(BM + 3 * FCM + 2.5 * TCM + FTM + 1.5 * TTM <= 12000 + 60 * OT)

# 定义目标函数
model.setObjective(
    0.5 * BM + 0.6 * BP + 3.75 * FCM + 4 * FCP + 3.3 * TCM + 3.9 * TCP + 0.6 * FTM + 0.65 * FTP + 0.75 * TTM + 0.78 * TTP + 9 * OT,
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
