local fqcs2 = {
    name = "fqc up"
}

function fqcs2:execute(m)
    return self
end

function fqcs2:exit(m)
    print("fqcs1.exit is called")
end

function fqcs2:onEvent(m, event)
    --print("fqcs2:onEvent", m.name, event.target, event.data.value)
    --changeState(m, "fqcs3")
end

return fqcs2