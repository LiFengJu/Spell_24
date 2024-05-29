---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by gepen.
--- DateTime: 2024/5/22 5:12
---
--- line ������
---
local line = {
    machines = { "r1", "r2", "r3", "r4", "w1", "w2", "w3", "w4", "z1", "z2", "t1", "t2", "fqc", "led" },
    name = "am516",
}

function line:execute()
    for _, name in ipairs(self.machines) do
        local m = require(name):execute(self)
        print("==========machine: ", m)
        if has_method(m, "onEvent") then
            self:subscribe(function(event)
                print("onEvent root---------------", event.name, m.name)
                m:onEvent(event)
            end)
        end
    end
    self:subscribe(function(event)
        self:onEvent(event)
    end)
    return self
end

function line:power(b)
    for _, m in ipairs(self.machines) do
        m:execute(self)
    end
end

function line:run()
    state.running = True
    state:setLed("green")
    self:publish({
        name = "run"
    })
end

function line:stop()
    state.running = False
    state.led.color = "yellow"
    self:publish({
        name = "stop"
    })
end

function line:pause()
    self:publish({
        name = "pause"
    })
end

function line:publish(data)
    bus:publish(self.name, data)
end

function line:subscribe(callback)
    bus:subscribe(self.name, callback)
end

function line:onEvent()
    return function(event)
        print(self.name, "onEvent", event.data)
    end
end

return line

