local s_b1_down = {
    comment = "¼Ó¹¤×´Ì¬"
}

function s_b1_down:run(w, ...)
    time.sleep(3000)    
    print(" s_b1_down:run")
    w:publish({
      id = w.id,
      action = actions.process,
        })
    w:changeState("s_b1_idle")
    --
    --local args = { ... }
    --if #args < 1 then
    --    w:changeState("s_idle")
    --    return
    --end
    --if failed(zmc.run(w.handle, args[1])) then
    --    time.sleep(3000)
    --    print("sleep 3......")
    --end
    --w:changeState("s_b1_idle")
end

function s_b1_down:exit(w)
end

function s_b1_down:onEvent(w, data)
    print("s_b1_down.onEvent", w.id, data.a, data.b, data.c)

end

return s_b1_down