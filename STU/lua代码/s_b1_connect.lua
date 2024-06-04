local b1_connect = {
    comment = "机器人1网络连接状态"
}

function b1_connect:run(b1, ...)
    timer.sleep(3000)
    b1:changeState("b1_idle")
end

function b1_connect:exit(r1)
    -- 在退出状态时执行的逻辑
end

function b1_connect:connect(b1)
    -- 连接逻辑，根据实际情况进行实现
    -- 如果连接成功，返回 true；否则返回 false
    -- 可以使用 r1.ip 和 r1.id 进行连接操作
end

function b1_connect:onEvent(b1, data)
    -- 在接收到事件时的逻辑处理
end

return b1_connect