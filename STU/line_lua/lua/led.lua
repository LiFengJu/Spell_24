
local led = {
    name = "led",
    clYellow = 1,
    clGreen = 2,
    clRed = 3,
    color = 0,
}

function led:execute()
    changeState(self, "led_s1")
    return self
end

function led:onEvent(event)
    --print("ÈýÉ«µÆ×´Ì¬", event.conf.plc:readI16(27,16))
end

return led