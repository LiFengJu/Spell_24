---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by gepeng.
--- DateTime: 2023/4/25 9:50
---
local s_fqc_idle = {
    comment = "空闲状态"
}

function s_fqc_idle:run(fqc)
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

function s_fqc_idle:exit(fqc)
end

function s_fqc_idle:onEvent(fqc, data)
    if data.action == actions.processing and data.id == fqc.id then
        fqc:changeState("s_fqc_process")
    end
end

return s_fqc_idle
