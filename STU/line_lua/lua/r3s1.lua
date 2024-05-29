local r3s1 = {
    name = "r3 idle state"
}

function r3s1:execute(m)
    print(m.name, self.name)
    print(m.conf)
    --publish({
    --    target = "r1",
    --    data = {
    --        value = 1234455,
    --    }
    --})
end

function r3s1:exit(m)
    print("r3s1.exit is called")
end

function r3s1:moveto(m, x, y)
    print(self.name)
    print("move", x,y)
    --changeState(m, ""{
    --    target= "w1",
    --    name = "wipok",
    --    parr = 1,
    --})
end


return r3s1