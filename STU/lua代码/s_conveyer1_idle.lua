local s_conveyer1_idle = {
    comment = "空闲状态"
}

function s_conveyer1_idle:run(w)
    -- 创建定时器
    --w:createTimer("idle.test", 6000, function()
    --    print("idle.test timeout")
    --end)
    --- just for demo
    --time.afterFunc(5, function()
    --    w:publish({
    --        id = w.id,
    --        action = actions.process,
    --        nc = "123.nc",
    --    })
    --end)
end

function s_conveyer1_idle:exit(w)
end

function s_conveyer1_idle:onEvent(w, data)
    if data.action == actions.operate and data.id == w.id then
        w:changeState("s_conveyer1_operate")
    end
	   
end

return s_conveyer1_idle