---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by gepeng.
--- DateTime: 2023/4/25 9:50
---
local s_idle = {
    comment = "空闲状态"
}

function s_idle:run(w)
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

function s_idle:exit(w)
end

function s_idle:onEvent(w, data)
    if data.action == actions.process and data.nc ~= nil and data.id == w.id then
        w:changeState("s_process", data.nc)
    end
end

return s_idle