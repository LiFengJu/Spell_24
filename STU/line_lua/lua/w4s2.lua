local w4s2 = {
    name = "w4 up"
}

function w4s2:execute(m)
    print(self.name, "w4s2.execute")
end

function w4s2:exit(m)
    print("w4s1.exit is called")
end

function w4s2:onEvent(m, event)
    print("w4s2:onEvent", m.name, event.target, event.data.value)
    --changeState(m, "w4s3")
end

return w4s2