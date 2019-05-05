概述：
	功能：将破壁菜单程序转换成excel

菜单说明(基于Y35菜单格式)：
	1. 菜单支持格式，如下所示：
		unsigned char code MENU_HUA_GUO_CHA_CB[][5]= {//花果茶
			{OB_Heater|End_Temp   			,TIME_x_M_y_S(24,0)		,HEAT_L1_0_0	,Temp85},
			{OB_Heater|Time_OR_Fy 			,TIME_x_M_y_S(5,40)		,HEAT_L0_3_0	,0},
			{OB_NULL|End_Time     			,TIME_x_M_y_S(0,20)		,0          	,DISP_UPDATE},
			{OB_Heater|End_Time   			,TIME_x_M_y_S(60,0)		,L1				,0},
			{0,0,0,0,0}	 
		};
	2. 控制对象支持格式（第一字节高位）：
		OB_NULL
		OB_Motor
		OB_Heater
		OB_Buz
		OB_Repeat
		OB_H_20S_M_0_1S
		OB_H_30S_M_5S
		OB_H_60S_M_5S
		OB_H_120S_M_5S
		OB_H_CONST_T
		OB_Motor_1Heat
		OB_vacuum
	3. 控制条件支持格式（第一字节低位）：
		End_Time
		End_Temp
		Time_OR_Temp
		Time_AND_Temp
		Time_OR_Fy
		Time_ORTemp_OR_TempCtrl
		Temp_OR_Fy
		Time_OR_Temp_OR_Fy
	4. 调波加热方式支持格式：
		HEAT_L0_1_0
		HEAT_L0_2_0
		HEAT_L0_3_0
		HEAT_L0_4_0
		HEAT_L0_5_0
		HEAT_L0_6_0
		HEAT_L0_7_0
		HEAT_L0_8_0
		HEAT_L0_9_0
		HEAT_L1_0_0
	5. 斩波控制支持格式：
		L0_5
		L0_8
		L1
		L1_5
		L2
		L2_0
		L2_5
		L3
		L3_5
		L4
		L4_5
		L5
		L5_5
		L6
		L6_5
		L7
		L7_5
		L8
		L8_5
		L9
		L9_5
		L10
	6. 时间格式：
		仅支持统一时间宏：
			TIME_x_M_y_S(x, y)
		不支持高低位格式, 请将格式使用宏替换：
			#define TIME_x_M_y_S(x, y) TIME_x_M_y_S_H(x,y), TIME_x_M_y_S_L(x,y)
		PS： 后面高低位时间不得加括号，此宏不要在菜单外使用

程序使用说明：
	1. 将菜单复制至MENU.C
	2. 将dataTransfer.txt中：
		machineName更改为相应机型
		menuNameDict中菜单名及对应中文名更改
	3. 双击fileReadAndDeal.exe运行，看到：
			successfully, input any key to end!
		表示成功，按下enter结束；
		文件夹下出现相应excel，即为所需excel。
程序说明：
	1. 文件包含————fileReadAndDeal.exe, dataTransfer.txt, MENU.C;
	2. 上述文件名称不得更改;
	3. fileReadAndDeal.exe: 程序， 双击执行;
	4. dataTransfer.txt: machineName, menuNameDict；
		machineName: 破壁机代号；
		menuNameDict: 冒号前为MENU.C中菜单名， 冒号后为对应菜单名；
	5. MENU.C： 支持注释，但需剔除菜单外代码；
	6. 注释处理器bug：请不要块注释与行注释混合使用，如//**********/，会导致无法处理；
	7. 仅支持64位系统;
源码说明：
	1. Based on Python3;
	2. Based on libs: openpyxl, sys, os, datetime, re;
	3. Source code in Source.7z;
	4. Code frame as follow:
		a. pretreatment of C file: filePreDeal.py
			deal with space, comment and so on.
			based on https://github.com/Stals/CommentsDeleter, not only for c, but not suitable for big file.
		b. excel opreation based on openpyxl: 
			including excel writing and reading.
		c. transfer C file to excel: 
			transfer code in C file to excel process.
		d. file dealed with:
			deal with file reading, dealing, writing, deleting and store.