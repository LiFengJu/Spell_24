---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by gepeng.
--- DateTime: 2023/4/25 14:58
--- 正在加工

local s_conveyer2_operate = {
    comment = "加工状态"
}

function s_conveyer2_operate:run(conveyer2, ...)
	timer.sleep(3000)
	print("sleep 3......")
	conveyer2:publish({
			id = conveyer2.id,
			action = actions.loading,
		})
	conveyer2:changeState("s_conveyer2_idle")
	
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

function s_conveyer2_operate:exit(conveyer2)
end

function s_conveyer2_operate:onEvent(conveyer2, data)
    --print("s_process.onEvent", w.id, data.a, data.b, data.c)

end

return s_conveyer2_operate