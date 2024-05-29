local w3s2 = {
    name = "w3 up"
}

function w3s2:execute(m)
    print(self.name, "w3s2.execute")
end

function w3s2:exit(m)
    print("w3s1.exit is called")
end

function w3s2:onEvent(m, event)
    print("w3s2:onEvent", m.name, event.target, event.data.value)
    --changeState(m, "w3s3")
end

return w3s2