---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by gepen.
--- DateTime: 2024/5/22 10:29
---
local db = {
    alarm_word_db3 = {
        w_0_word1 = 0,
        w_2_word2 = 0,
        w_4_word3 = 0,
        s_6_text1 = {
            b_6_0 = false, --- 1号推杆电机上限位
            b_6_1 = false, --- 1号推杆电机下限位
            b_6_2 = false, --- 2号推杆电机上限位
            b_6_3 = false, --- 2号推杆电机下限位
            b_6_4 = false, --- 质量检测推杆电机上限位
            b_6_5 = false, --- 质量检测推杆电机下限位
            b_6_6 = false, --- 急停故障
            b_6_7 = false, --- 上料平台缺料报警
            b_7_0 = false, --- 下料平台料满报警
            b_7_1 = false, --- 上料机器人急停故障
            b_7_2 = false, --- 1号机器人急停故障
            b_7_3 = false, --- 2号机器人急停故障
            b_7_4 = false, --- 下料机器人急停故障
            b_7_5 = false, --- 1号机器人取料失败
            b_7_6 = false, --- 2号机器人取料失败
            b_7_7 = false, --- standby9
        },

        s_8_text2 = {
            b_8_0_standby0 = false,
            b_8_1_standby1 = false,
            b_8_2_standby2 = false,
            b_8_3_standby3 = false,
            b_8_4_standby4 = false,
            b_8_5_standby5 = false,
            b_8_6_standby6 = false,
            b_8_7_standby7 = false,
            b_9_0_standby8 = false,
            b_9_1_standby9 = false,
            b_9_2_standby10 = false,
            b_9_3_standby11 = false,
            b_9_4_standby12 = false,
            b_9_5_standby13 = false,
            b_9_6_standby14 = false,
            b_9_7_standby15 = false,
        },
        w_10_textother = 0,
    },

    public_db7 = {
        run = false,
    },

    auto_db17 = {
        i_0_step = {
            1, ---1 1 上料机器人运行步骤
            1, ---2 1号机器人运行步骤
            1, ---3 2号机器人运行步骤
            1, ---4 下料机器人运行步骤
            1, ---5 质量检测工位运行步骤
            1, ---6 1号写字机器人运行步骤
            1, ---7 2号写字机器人运行步骤
            1, ---8
            1, ---9
            0, ---10
        },
        i_20_product_step = 1,
        i_22 = 0, --- 放料计数 --- 上料机器人完成上料技术
        i_24 = 0, --- 产品数量 --- 下单的产品数量
        i_26 = 0, --- 下料计数 --- 下料机器人完成下料计数
        i_28 = 0, --- 1号工位产品计数         i22 = 0, --- 质量检测计数
        i_30 = 0, --- 检测工位产品计数
        f_32 = 0, --- 质量检测获取到的分数
        b_36 = false, --- 质量检测获取到的结果 = false,
        b_38_0_w1_1 = false, --- 1号写字机器人有无产品
        b_38_1_w2_1 = false, --- 2号写字机器人有无产品
        b_38_2_w3_1 = false, --- 3号写字机器人有无产品
        b_38_3_w4_1 = false, --- 4号写字机器人有无产品
        b_38_4 = true, --- 产品已被下料机器人取走
        i_40_standby = 0,
        i_42_w1_state = 0, --- 1号写字机器人运行状态, { 1: 表示写字机器人运行, 2: 表示写字机器人空闲 }
        i_44_w2_state = 0, --- 2号写字机器人运行状态, { 1: 表示写字机器人运行, 2: 表示写字机器人空闲 }
        i_46_w3_state = 0, --- 3号写字机器人运行状态, { 1: 表示写字机器人运行, 2: 表示写字机器人空闲 }
        i_48_w4_state = 0, --- 4号写字机器人运行状态, { 1: 表示写字机器人运行, 2: 表示写字机器人空闲 }
    },

    auto_hmi_db27 = {
        --- 延时参数
        s_0_delay = {
            tm_0 = 0, --- 1号输送线停止延时PT
            tm_4 = 0, --- 2号输送线停止延时PT
            tm_8 = 0, --- 质量检测延时拍照
            tm_12 = 0, --- 质量检测延时放行
        },
        i_16_led_status = 0, --- 三色灯状态, { 0:黄灯, 1:绿灯, 2:红灯 }
    },
    recipe_one_db26 = {
        c_0_name = "", --- 名称
        c_8_no = "", --- 合同号
        i_16 = 0, ---订单序号
        i_18_w1_station = 0, ---1号工位放置位置
        i_20_w1_nc = 0, ---1号工位加工文件序号
        i_22_w2_station = 0, ---2号工位放置位置
        i_24_w2_nc = 0, ---2号工位文件加工序号
        i_26_w3_station = 0, ---3号工位放置位置
        i_28_w3_nc = 0, ---3号工位加工文件序号
        i_30_w4_station = 0, ---4号工位放置位置
        i_32_w4_nc = 0, ---4号工位文件加工序号
        i_34_count = 0, ---产品数量
    },

    write_robot1_db51 = {
        i_0_ctr_status = 0, --- 1号写字机器人控制流程(1收到写字机器人准备好,2让写字机器人运行,3,写字机器人运行完成,4让写字机器人暂停,5让写字机器人继续)
        i_2_nc = 0, --- 1号写字机器人文件号
        i_4_run_status_ = 0, --- 1号写字机器人运行状态(1表示运行,2表示停止)
    },
    write_robot1_db52 = {
        i_0_ctr_status = 0, --- 2号写字机器人控制流程(1收到写字机器人准备好,2让写字机器人运行,3,写字机器人运行完成,4让写字机器人暂停,5让写字机器人继续)
        i_2_nc = 0, --- 2号写字机器人文件号
        i_4_run_status_ = 0, --- 2号写字机器人运行状态(1表示运行,2表示停止)
    },
    write_robot1_db53 = {
        i_0_ctr_status = 0, --- 23号写字机器人控制流程(1收到写字机器人准备好,2让写字机器人运行,3,写字机器人运行完成,4让写字机器人暂停,5让写字机器人继续)
        i_2_nc = 0, --- 3号写字机器人文件号
        i_4_run_status_ = 0, --- 3号写字机器人运行状态(1表示运行,2表示停止)
    },
    write_robot1_db54 = {
        i_0_ctr_status = 0, --- 4号写字机器人控制流程(1收到写字机器人准备好,2让写字机器人运行,3,写字机器人运行完成,4让写字机器人暂停,5让写字机器人继续)
        i_2_nc = 0, --- 4号写字机器人文件号
        i_4_run_status_ = 0, --- 4号写字机器人运行状态(1表示运行,2表示停止)
    },

    vtable = {
        I0_2  = false, ---  Star_Button
        I0_3  = false, ---  Stop_Button
        I0_4  = false, ---  Reset_Button
        I0_5  = false, ---  E-Stop_Button
        I1_0  = false, ---  进料物料检测
        I1_1  = false, ---  1号推杆电机上限位检测
        I1_2  = false, ---  1号推杆电机下限位检测
        I1_3  = false, ---  1号工位物料检测
        I3_0  = false, ---  2号工位物料检测
        I3_1  = false, ---  2号推杆电机上限位检测
        I3_2  = false, ---  2号推杆电机下限位检测
        I3_3  = false, ---  质量检测工位推杆电机下限位检测
        I3_4  = false, ---  质量检测工位推杆电机上限位检测
        I3_5  = false, ---  质量工位检测
        I3_6  = false, ---  下料工位检测
        Q0_3  = false, ---  三色灯红
        Q1_0  = false, ---  1号物料检测推杆电机正转
        Q1_1  = false, ---  1号物料检测推杆电机反转
        Q1_2  = false, ---  1号输送线启动
        Q3_0  = false, ---  2号物料检测推杆电机正转
        Q3_1  = false, ---  2号物料检测推杆电机反转
        Q3_2  = false, ---  质量检测推杆电机正转
        Q3_3  = false, ---  质量检测推杆电机反转
        Q3_4  = false, ---  2号输送线启动
        Q0_4  = false, ---  三色灯黄
        Q0_5  = false, ---  三色灯绿
        Q0_0  = false, ---  X_脉冲
        Q0_1  = false, ---  X_方向
        QB1  = false ,---  QB1
        QB3  = false ,---  QB3
        MB1  = false ,---  System_Byte
        M1_0  = false, ---  FirstScan
        M1_1  = false, ---  DiagStatusUpdate
        M1_2  = true ,---  AlwaysTRUE
        M1_3  = false, ---  AlwaysFALSE
        MB0  = false ,---  Clock_Byte
        M0_0  = false, ---  Clock_10Hz
        M0_1  = false, ---  Clock_5Hz
        M0_2  = false, ---  Clock_2.5Hz
        M0_3  = false, ---  Clock_2Hz
        M0_4  = false, ---  Clock_1.25Hz
        M0_5  = false, ---  Clock_1Hz
        M0_6  = false, ---  Clock_0.625Hz
        M0_7  = false, ---  Clock_0.5Hz
        M10_0  = false ,---  HMI手/自动
        M10_1  = false ,---  HMI启动
        M10_2  = false ,---  HMI停止
        M10_3  = false ,---  HMI复位
        M10_4  = false ,---  HMI1号工位初始化， 上料报缺料故障后启动按钮继续
        M10_5  = false ,---  HMI上料继续， 下料报缺料故障后启动按钮继续
        M10_6  = false ,---  HMI下料继续
        M10_7  = false ,---  HMI触发记录
        M11_0  = false ,---  HMI2号工位初始化
        M11_1  = false ,---  HMI上料工位初始化
        M11_2  = false ,---  HMI下料工位初始化
        I4_2  = false ,---  质量工位前端检测，防止检测工位有多个物料
        I4_0  = false ,---  下料机器人急停
        I3_7  = false ,---  2号机器人急停
        I1_4  = false ,---  上料机器人急停
        I1_5  = false ,---  1号机器人急停
        M11_3  = false, ---  隐藏上料位置重启按钮
        M11_4  = false, ---  隐藏下料位置重启按钮
        M11_5  = false, ---  1号机器人取料失败重启
        M11_6  = false, ---  2号机器人取料失败重启
    },
}

return db