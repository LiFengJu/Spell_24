local s_b2_idle = {
    comment = "空闲状态"
}

function s_b2_idle:run(w)
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

function s_b2_idle:exit(w)
end

function s_b2_idle:onEvent(w, data)
    if data.action == actions.up and data.nc ~= nil and data.id == w.id then
        w:changeState("s_b2_up", data.nc)
    end
	    if data.action == actions.down and data.nc ~= nil and data.id == w.id then
        w:changeState("s_b2_down", data.nc)
	end
end

return s_b2_idle