local b2_connect = {
    comment = "������1��������״̬"
}

function b2_connect:run(b2, ...)
    timer.sleep(3000)
    b2:changeState("b2_idle")
end

function b2_connect:exit(r1)
    -- ���˳�״̬ʱִ�е��߼�
end

function b2_connect:connect(b2)
    -- �����߼�������ʵ���������ʵ��
    -- ������ӳɹ������� true�����򷵻� false
    -- ����ʹ�� r1.ip �� r1.id �������Ӳ���
end

function b2_connect:onEvent(b2, data)
    -- �ڽ��յ��¼�ʱ���߼�����
end

return b2_connect