local s_b1_up = {
    comment = "�ӹ�״̬"
}

function s_b1_up:run(w, ...)
    time.sleep(3000)    
    print(" s_b1_up:run")
    w:publish({
      id = w.id,
      action = actions.process,
          })
    w:changeState("s_b1_idle")
    --
    --local args = { ... }
    --if #args < 1 then
    --    w:changeState("s_b1_idle")
    --    return
    --end
    --if failed(zmc.run(w.handle, args[1])) then
    --    time.sleep(3000)
    --    print("sleep 3......")
    --end
    --w:changeState("s_b1_idle")
end

function s_b1_up:exit(w)
end

function s_b1_up:onEvent(w, data)
    print("s_b1_up.onEvent", w.id, data.a, data.b, data.c)

end

return s_b1_up
