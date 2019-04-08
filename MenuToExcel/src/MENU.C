unsigned char code MENU01[][5]= {//浓浆
	{OB_H_30S_M_5S|END_TIME_OR_TEMP	,MENU_TIME_x_M_y_S(20,00)	,HEAT_L10		,60			},
	{OB_H_30S_M_5S|END_TIME_OR_TEMP	,MENU_TIME_x_M_y_S(20,00)	,HEAT_L9 		,80			},
	{OB_HEATER|END_TIME_OR_TEMP_OR_FY,MENU_TIME_x_M_y_S(3,00)	,HEAT_L8 		,87			},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,5)		,MOTOR_MODE 	,MOTO_L2		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,5)		,0           	,0				},
	{OB_HEATER|END_TIME_OR_TEMP_OR_FY,MENU_TIME_x_M_y_S(2,00)	,HEAT_L8 		,91			},
	{OB_HEATER|END_TIME_OR_FY   		,MENU_TIME_x_M_y_S(5,00)	,HEAT_L5			,100			},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,DISP_UPDATE},
	{OB_HEATER|END_TIME   				,MENU_TIME_x_M_y_S(2,30)	,HEAT_L1			,100			},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,40)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L3		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L4		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,20)	,MOTOR_MODE 	,MOTO_L5		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,20)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,20)	,MOTOR_MODE 	,MOTO_L6		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,15)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,25)	,MOTOR_MODE 	,MOTO_L6		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,5)		,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,15)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,25)	,MOTOR_MODE 	,MOTO_L7		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_REPEAT|END_TIME        		,MENU_TIME_x_M_y_S(5,50)	,3           	,1 			},
	{OB_HEATER|END_TIME   				,MENU_TIME_x_M_y_S(1,00)	,HEAT_L1			,0				},
	{0,0,0,0,0},
};  
unsigned char code MENU02[][5]= {//浓汤
	{0,0,0,0,0},
};
unsigned char code MENU03[][5]= {//花果�?
	{0,0,0,0,0}	 
};
unsigned char code MENU04[][5]= {//滋补�?
	{0,0,0,0,0}	 	
};
unsigned char code MENU05[][5]= {//养生�?
	{0,0,0,0,0}	 	
};
unsigned char code MENU06[][5] = {//酱料
	{0,0,0,0,0}	
};
unsigned char code MENU07[][5] = {//西洋参粉
	{0,0,0,0,0}	
};
unsigned char code MENU08[][5] = {//果蔬�?
	{0,0,0,0,0}		
};
unsigned char code MENU09[][5]={//奶昔
	{0,0,0,0,0}																					
};
unsigned char code MENU10[][5]={//冰沙
	{0,0,0,0,0}																					
};
unsigned char code MENU11[][5]= {//清洗
	{0,0,0,0,0}		
};