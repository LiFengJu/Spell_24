---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by gepeng.
--- DateTime: 2023/4/25 9:50
---
local s_r2_idle = {
    comment = "空闲状态"
}

function s_r2_idle:run(r2)
    -- 创建定时器
    --r2:createTimer("idle.test", 6000, function()
    --    print("idle.test timeout")
    --end)
    --- just for demo
    --time.afterFunc(5, function()
    --    r2:publish({
    --        id = r2.id,
    --        action = actions.process,
    --        nc = "123.nc",
    --    })
    --end)
end

function s_r2_idle:exit(r2)
end

function s_r2_idle:onEvent(r2, data)
    if data.action == actions.loading and data.id == r2.id then
        r2:changeState("s_r2_loading")
	end
	if data.action == actions.unloading and data.id == r2.id then
        r2changeState("s_r2_unloading")
    end
end

return s_r2_idle