local b1_connect = {
    comment = "������1��������״̬"
}

function b1_connect:run(b1, ...)
    timer.sleep(3000)
    b1:changeState("b1_idle")
end

function b1_connect:exit(r1)
    -- ���˳�״̬ʱִ�е��߼�
end

function b1_connect:connect(b1)
    -- �����߼�������ʵ���������ʵ��
    -- ������ӳɹ������� true�����򷵻� false
    -- ����ʹ�� r1.ip �� r1.id �������Ӳ���
end

function b1_connect:onEvent(b1, data)
    -- �ڽ��յ��¼�ʱ���߼�����
end

return b1_connect