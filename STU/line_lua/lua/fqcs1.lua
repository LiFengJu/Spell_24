local fqcs1 = {
    name = "fqc down"
}

function fqcs1:execute(m)
    --print("三色灯状态", m.conf.plc:readI16(27,16))
    --print("订单号", m.conf.plc:readString(26,0,8))
    return self
end

function fqcs1:exit(m)
    print("fqcs1.exit is called")
end

function fqcs1:onEvent(m, event)
    --print("---------", m.name, event.target, event.data.value)
    changeState(m, "fqcs2")
end

return fqcs1