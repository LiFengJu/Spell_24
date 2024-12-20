---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by gepeng.
--- DateTime: 2023/4/25 14:58
--- 正在加工

local s_r1_loading = {
    comment = "加工状态"
}

function s_r1_loading:run(r1, ...)
	timer.sleep(3000)
	print("sleep 3......")
	r1:publish({
			id = r1.id,
			action = actions.loading,
		})
	r1:changeState("s_r1_idle")
	
    --[[local args = { ... }
    if #args < 1 then
        w:changeState("s_idle")
        return
    end
    if failed(zmc.run(w.handle, args[1])) then
        time.sleep(3000)
        print("sleep 3......")
    end
    w:changeState("s_idle")--]]
end

function s_r1_loading:exit(r1)
end

function s_r1_loading:onEvent(r1, data)
    --print("s_process.onEvent", w.id, data.a, data.b, data.c)

end

return s_r1_loading