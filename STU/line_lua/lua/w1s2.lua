local w1s2 = {
    name = "w1 up"
}

function w1s2:execute(m)
    print(self.name, "w1s2.execute")
end

function w1s2:exit(m)
    print("w1s1.exit is called")
end

function w1s2:onEvent(m, event)
    print("w1s2:onEvent", m.name, event.target, event.data.value)
    --changeState(m, "w1s3")
end

return w1s2