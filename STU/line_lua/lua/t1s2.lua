local t1s2 = {
    name = "t1 up"
}

function t1s2:execute(m)
    print(self.name, "t1s2.execute")
end

function t1s2:exit(m)
    print("t1s1.exit is called")
end

function t1s2:onEvent(m, event)
    print("t1s2:onEvent", m.name, event.target, event.data.value)
    --changeState(self, "t1s3")
end

return t1s2