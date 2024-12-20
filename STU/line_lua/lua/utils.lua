---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by gepen.
--- DateTime: 2024/5/27 20:22
---

function changeState(machine, state_name, args)
    local state = require(state_name)
    if machine.currentState ~= Nil then
        machine.currentState:exit(machine)
    end
    machine.currentState = state
    machine.currentState:execute(machine, args)
end

function has_method(object, method_name)
    if type(object) ~= "table" then
        return False
    elseif type(method_name) ~= "string" then
        return False
    end
    local m = object[method_name]
    if type(m) ~= "function" then
        return False
    end
    return True
end
