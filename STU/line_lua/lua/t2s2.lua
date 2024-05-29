local t2s2 = {
    name = "t2 up"
}

function t2s2:execute(m)
    print(self.name, "t2s2.execute")
end

function t2s2:exit(m)
    print("t2s1.exit is called")
end

function t2s2:onEvent(m, event)
    print("t2s2:onEvent", m.name, event.target, event.data.value)
    --changeState(m, "t2s3")
end

return t2s2