local b1 = {
    debug = true,
    stateTimer = {}
}

--- run 运行状态机
function b1:run()
    local time = require("timer")
  local client = {
        id = conf.id or "b1",
        ip = conf.ip or "127.0.0.1"
}
    setmetatable(client, { __index = self })
    client:subscribe()
    timer.afterFunc(3000, function()
        client:changeState("s_b1_connect")
    end)  -- 在此处添加一个闭合的括号
    return client
end

--- changeState 改变状态机当前状态
function b1:changeState(name, ...)
    log(name)
    for _, timerId in pairs(self.stateTimer) do
        time.removeTimer(timerId)
    end
    if self.state ~= nil and self.state.exit ~= nil then
        self.state:exit(self)
    end
    self.state = require(name)
    self.state:run(self, ...)
end

--- subscribe 订阅消息
function b1:subscribe()
    mqtt:Subscribe(self.id, function(data)
        if self.state ~= nil and self.state.onEvent ~= nil then
            self.state:onEvent(self, data)
        end
    end)
end

--- publish 发布消息
function b1:publish(data)
    mqtt:Publish(self.id, data)
end

--- connected 已连接运动控制器
function b1:connected()
    return self.handle ~= nil
end

--- connected 已连接运动控制器
function b1:createTimer(key, interval, callback)
    local id = time.createTimer(interval, callback)
    self.stateTimer[key] = id
end

--- removeTimer 删除状态创建的定时器
---   key 定时器名称(如果为空则删除全部)
function b1:removeTimer(key)
    if key==nil then
        for _, timerId in pairs(self.stateTimer) do
            time.removeTimer(timerId)
        end
        return
    end
    local id = self.stateTimer[key]
    if id~=nil then
        time.removeTimer(id)
    end
end

return b1
