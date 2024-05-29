local r4s1 = {
    name = "idle state"
}

function r4s1:execute(m)
    print("r4s1.execute")
    print(m.name, self.name)
    --print("三色灯状态", m.conf.plc:readI16(27,16))
    --print("订单号", m.conf.plc:readString(26,0,8))
end

function r4s1:exit(m)
    print("r4s1.exit is called")
end

function r4s1:onEvent(m, event)
    print("---------", m, event)
    changeState(m, "r4s2")
end

return r4s1