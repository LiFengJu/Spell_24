local w2s2 = {
    name = "w2 up"
}

function w2s2:execute(m)
    print(self.name, "w2s2.execute")
end

function w2s2:exit(m)
    print("w2s1.exit is called")
end

function w2s2:onEvent(m, event)
    print("w2s2:onEvent", m.name, event.target, event.data.value)
    --changeState(m, "w2s3")
end

return w2s2