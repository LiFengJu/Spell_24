local b2 = {
    debug = true,
    stateTimer = {}
}

--- run ����״̬��
function b2:run(conf)
    local client = {
        id = conf.id or "b2",
        ip = conf.ip or "127.0.0.1"
	}
    setmetatable(client, { __index = self })
    client:subscribe()
    timer.afterFunc(3000, function()
        client:changeState("s_b2_connect")
    end)
    return client
end

--- changeState �ı�״̬����ǰ״̬
function b2:changeState(name, ...)
    log(name)
    for _, timerId in pairs(self.stateTimer) do
        time.removeTimer(timerId)
    end
    if self.state ~= nil and self.state.exit ~= nil then
        self.state:exit(self)
    end
    self.state = require(name)
    self.state:run(self, ...)
end

--- subscribe ������Ϣ
function b2:subscribe()
    mqtt:Subscribe(self.id, function(data)
        if self.state ~= nil and self.state.onEvent ~= nil then
            self.state:onEvent(self, data)
        end
    end)
end

--- publish ������Ϣ
function b2:publish(data)
    mqtt:Publish(self.id, data)
end

--- connected �������˶�������
function b2:connected()
    return self.handle ~= nil
end

--- connected �������˶�������
function b2:createTimer(key, interval, callback)
    local id = time.createTimer(interval, callback)
    self.stateTimer[key] = id
end

--- removeTimer ɾ��״̬�����Ķ�ʱ��
---   key ��ʱ������(���Ϊ����ɾ��ȫ��)
function b2:removeTimer(key)
    if key==nil then
        for _, timerId in pairs(self.stateTimer) do
            time.removeTimer(timerId)
        end
        return
    end
    local id = self.stateTimer[key]
    if id~=nil then
        time.removeTimer(id)
    end
end

return b2

