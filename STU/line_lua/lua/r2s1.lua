local r2s1 = {
    name = "r2 idle state"
}

function r2s1:execute(m)
    self.m = m
   m.line:publish( {
            value = 1234455,
        })
end

function r2s1:exit(m)
    print("r2s1.exit is called")
end

function r2s1:moveto(m, x, y)
    changeState(m, "r2s2", {
        target= "w1",
        name = "wipok",
        parr = 1,
    })
end


return r2s1