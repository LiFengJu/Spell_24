---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by gepeng.
--- DateTime: 2023/4/25 9:46
--- 连接状态

local s_fqc_connect = {
    comment = "与zmc建立网络连接"
}

function s_fqc_connect:run(fqc, ...)
	timer.sleep(3000) --
    --w:createTimer("s_connect.test", 6000, function()
    --    print("s_connect.test timeout")
    --end)
    --[[while (self:connect(w) ~= true)
    do
        time.sleep(3000)
    end--]]
    fqc:changeState("s_fqc_idle")
end

function s_fqc_connect:exit(fqc)
    --print("s_connect:exit")
end

function s_fqc_connect:connect(fqc)
    if fqc.handle ~= nil then
        zmc.close(fqc.handle)
        fqc.handle = nil
        return false
    end
    fqc.handle, err = zmc.connect(fqc.ip)
    if failed(err) then
        log(self, err)
        return false
    end
    log("连接到运动控制器", fqc.ip)
    return fqc.handle ~= nil
end

function s_fqc_connect:onEvent(fqc, data)
    --print("s_connect.onEvent", fqc.id, data.a, data.b, data.c)
end

return s_fqc_connect
