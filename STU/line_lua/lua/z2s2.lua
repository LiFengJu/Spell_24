local z2s2 = {
    name = "z2 up"
}

function z2s2:execute(m)
    print(self.name, "z2s2.execute")
end

function z2s2:exit(m)
    print("z2s1.exit is called")
end

function z2s2:onEvent(m, event)
    --print("z2s2:onEvent", m.name, event.target, event.data.value)
    --changeState(m, "z2s3")
end

return z2s2