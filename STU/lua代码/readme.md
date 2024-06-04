## 状态机
### api
1. run(machine, args...) 运行状态, 可在run中完成状态参数设置
2. exit(machine) 退出状态时被调用
3. onEvent(machine, data) 状态收到总线数据