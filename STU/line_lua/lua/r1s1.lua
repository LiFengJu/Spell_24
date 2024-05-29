local r1s1 = {
    name = "idle state"
}

function r1s1:execute(m)
    self.m = m
    --print("三色灯状态", m.conf.plc:readI16(27,16))
    --print("订单号", m.conf.plc:readString(26,0,8))
end

function r1s1:exit(m)
    print("r1s1.exit is called")
end

function r1s1:onTimer()
    return function(id)
        changeState(self.m, "r1s2", {
            name = "name123",
        })
    end
end

function r1s1:onEvent(m, event)
    if event.name == "run" then
        print("in s1 r1s1 ---> r1s2")
        changeState(m, "r1s2")
        return
    end
    print("r1s1 do nothing")
end

return r1s1