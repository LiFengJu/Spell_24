local s_b1_idle = {
    comment = "����״̬"
}

function s_b1_idle:run(w)
    -- ������ʱ��
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

function s_b1_idle:exit(w)
end

function s_b1_idle:onEvent(w, data)
    if data.action == actions.up and data.nc ~= nil and data.id == w.id then
        w:changeState("s_b1_up", data.nc)
    end
	    if data.action == actions.down and data.nc ~= nil and data.id == w.id then
        w:changeState("s_b1_down", data.nc)
	end
end

return s_b1_idle