local s_conveyer2_connect = {
    comment = "���ʹ�2��������״̬"
}

function s_conveyer2_connect:run(conveyer2, ...)
    timer.sleep(3000)
    conveyer2:changeState("s_conveyer2_idle")
end

function s_conveyer2_connect:exit(conveyer2)
    -- ���˳�״̬ʱִ�е��߼�
end

function s_conveyer2_connect:connect(conveyer2)
    -- �����߼�������ʵ���������ʵ��
    -- ������ӳɹ������� true�����򷵻� false
    -- ����ʹ�� r2.ip �� r2.id �������Ӳ���
end

function s_conveyer2_connect:onEvent(conveyer2, data)
    -- �ڽ��յ��¼�ʱ���߼�����
end

return s_conveyer2_connect