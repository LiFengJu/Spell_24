local s_conveyer1_connect = {
    comment = "���ʹ�1��������״̬"
}

function s_conveyer1_connect:run(conveyer1, ...)
    timer.sleep(3000)
    conveyer1:changeState("s_conveyer1_idle")
end

function s_conveyer1_connect:exit(conveyer1)
    -- ���˳�״̬ʱִ�е��߼�
end

function s_conveyer1_connect:connect(conveyer1)
    -- �����߼�������ʵ���������ʵ��
    -- ������ӳɹ������� true�����򷵻� false
    -- ����ʹ�� r1.ip �� r1.id �������Ӳ���
end

function s_conveyer1_connect:onEvent(conveyer1, data)
    -- �ڽ��յ��¼�ʱ���߼�����
end

return s_conveyer1_connect