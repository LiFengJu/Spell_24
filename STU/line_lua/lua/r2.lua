---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by gepeng.
--- DateTime: 2021/10/21 17:51
---

local r2 = {
    name = "robot 2",
}

function r2:execute(line)
    self.line = line
    changeState(self, "r2s1")
    return self
end


function r2:onEvent(event)
    print("onevent", self.name, event)
end

return r2