---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by gepeng.
--- DateTime: 2023/4/25 14:58
--- 正在加工

local s_r4_reset = {
    comment = "复位状态"
}

function s_r4_reset:run(r4, ...)
	 time.sleep(3000)
	 r4:changeState("s_r4_idle")
    --[[local args = { ... }
    if #args < 1 then
        r4:changeState("s_r4_idle")
        return
    end
    if failed(zmc.run(r4.handle, args[1])) then
        time.sleep(3000)
        print("sleep 3......")
    end
    r4:changeState("s_r4_idle")--]]
end

function s_r4_reset:exit(r4)
end

function s_r4_reset:onEvent(r4, data)
    --print("s_r4_reset.onEvent", r4.id, data.a, data.b, data.c)

end

return s_r4_reset