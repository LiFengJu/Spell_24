---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by gepeng.
--- DateTime: 2023/4/25 9:46
--- 连接状态

local s_r4_connect = {
    comment = "与zmc建立网络连接"
}

function s_r4_connect:run(r4, ...)
	timer.sleep(3000)
	r4:changeState("s_r4_homing")
    --r4:createTimer("s_r4_connect.test", 6000, function()
    --    print("s_r4_connect.test timeout")
    --end)
    --[[while (self:connect(r4) ~= true)
    do
        time.sleep(3000)
    end
    r4:changeState("s_r4_homing")--]]
end
function s_r4_connect:exit(r4)
    --print("s_r4_connect:exit")
end

--[[function s_r4_connect:connect(r4)
    if r4.handle ~= nil then
        zmc.close(r4.handle)
        r4.handle = nil
        return false
    end
    r4.handle, err = zmc.connect(r4.ip)
    if failed(err) then
        log(self, err)
        return false
    end
    log("连接到运动控制器", r4.ip)
    return r4.handle ~= nil
end--]]

function s_r4_connect:onEvent(r4, data)
    --print("s_r4_connect.onEvent", r4.id, data.a, data.b, data.c)
end

return s_r4_connect
