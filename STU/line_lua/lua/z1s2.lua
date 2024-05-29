local z1s2 = {
    name = "z1 up"
}

function z1s2:execute(m)
    print(self.name, "z1s2.execute")
end

function z1s2:exit(m)
    print("z1s1.exit is called")
end

function z1s2:onEvent(m, event)
    print("z1s2:onEvent", m.name, event.target, event.data.value)
    --changeState(m, "z1s3")
end

return z1s2