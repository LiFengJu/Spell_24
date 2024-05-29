local r3s2 = {
    name = "r3s2 探料"
}

function r3s2:execute(m)
    print(self.name, "r3s2.execute")
end

function r3s2:exit(m)
    print("r3s2.exit is called")
end

function r3s2:onEvent(m, event)
    print("r3s2:onEvent", m.name, event.target, event.data.value)
    --changeState(m, "r3s3")
end

return r3s2