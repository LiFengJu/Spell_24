local r1s3 = {
    name = "r1s3 上料",
}

function r1s3:execute(m, args)
    self.m = m
    print(self.name, args)
    --if args~=nil then
    --    print("args.name", args.name)
    --end
    timer.push(1, function(id)
        --print("onTimer, 上料完成")
        changeState(m, "r1s3", {
            name = "name123",
        })
        m.line:publish({
            target = "t1",
            data = {
                pid= 1,
            },
        })
    end)
end

function r1s3:exit(m)
    print("r1s3.exit is called")
end

function r1s3:onEvent(m, event)
    print("r1s3:onEvent", m.name, event)
end

return r1s3