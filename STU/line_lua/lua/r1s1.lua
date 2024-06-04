local r1s1 = {
    name = "idle state"
}

function r1s1:execute(m)
    self.m = m
    print(m.name, self.name)
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
        changeState(m, "r1s2")
        return
    end
end

return r1s1