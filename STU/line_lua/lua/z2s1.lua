local z2s1 = {
    name = "z2 down"
}

function z2s1:execute(m)
    print("z2s1.execute")
    print(m.name, self.name)
    --print("三色灯状态", m.conf.plc:readI16(27,16))
    --print("订单号", m.conf.plc:readString(26,0,8))
end

function z2s1:exit(m)
    print("z2s1.exit is called")
end

function z2s1:onEvent(m, event)
    --print("---------", m.name, event.target, event.data.value)
    changeState(m, "z2s2")
end

return z2s1