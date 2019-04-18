//*********************热杯**********************
uchar code MENU_CB_HOT_10_FKJ_BIG[][5] = {//10分快浆 高水位
	{OB_H_30S_M_5S|END_TIME_OR_TEMP	,MENU_TIME_x_M_y_S(20,00)	,HEAT_L10		,60			},
	{OB_H_30S_M_5S|END_TIME_OR_TEMP	,MENU_TIME_x_M_y_S(20,00)	,HEAT_L9 		,80			},
	{OB_HEATER|END_TIME_OR_TEMP_OR_FY,MENU_TIME_x_M_y_S(3,00)	,HEAT_L8 		,87			},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,5)		,MOTOR_MODE 	,MOTO_L2		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,5)		,0           	,0				},
	{OB_HEATER|END_TIME_OR_TEMP_OR_FY,MENU_TIME_x_M_y_S(2,00)	,HEAT_L7 		,91			},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_HEATER|END_TIME_OR_FY   		,MENU_TIME_x_M_y_S(5,00)	,HEAT_L6			,100			},
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
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,25)	,MOTOR_MODE 	,MOTO_L7		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,25)	,MOTOR_MODE 	,MOTO_L7		},
	{0,0,0,0,0},
};
uchar code MENU_CB_HOT_10_FKJ_MID[][5] = {//10分快浆 中水位
	{OB_H_30S_M_5S|END_TIME_OR_TEMP	,MENU_TIME_x_M_y_S(20,00)	,HEAT_L10 		,60			},
	{OB_H_30S_M_5S|END_TIME_OR_TEMP	,MENU_TIME_x_M_y_S(20,00)	,HEAT_L9 		,80			},
	{OB_HEATER|END_TIME_OR_TEMP_OR_FY,MENU_TIME_x_M_y_S(2,00)	,HEAT_L8 		,87			},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,5)		,MOTOR_MODE 	,MOTO_L2		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,5)		,0           	,0				},
	{OB_HEATER|END_TIME_OR_TEMP_OR_FY,MENU_TIME_x_M_y_S(1,00)	,HEAT_L7 		,91			},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_HEATER|END_TIME_OR_FY   		,MENU_TIME_x_M_y_S(3,00)	,HEAT_L6 		,100			},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,DISP_UPDATE},
	{OB_HEATER|END_TIME   				,MENU_TIME_x_M_y_S(2,00)	,HEAT_L1 		,100			},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,40)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L3		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L4		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L5		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L6		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L6		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L7		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L6		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L6		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L7		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,40)	,MOTOR_MODE 	,MOTO_L7		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,40)	,MOTOR_MODE 	,MOTO_L6		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,25)	,MOTOR_MODE 	,MOTO_L7		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,25)	,MOTOR_MODE 	,MOTO_L7		},
	{0,0,0,0,0},
};
uchar code MENU_CB_HOT_10_FKJ_SMALL[][5] = {//10分快浆 低水位
	{OB_H_30S_M_5S|END_TIME_OR_TEMP	,MENU_TIME_x_M_y_S(20,0)	,HEAT_L10		,60			},
	{OB_H_30S_M_5S|END_TIME_OR_TEMP  ,MENU_TIME_x_M_y_S(20,0)	,HEAT_L9			,80			},
	{OB_HEATER|END_TIME_OR_TEMP_OR_FY,MENU_TIME_x_M_y_S(2,00)	,HEAT_L9			,87			},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,5)		,MOTOR_MODE 	,MOTO_L2		},
	{OB_HEATER|END_TIME_OR_TEMP		,MENU_TIME_x_M_y_S(0,10)	,HEAT_L9			,93			},
	{OB_HEATER|END_TIME_OR_TEMP		,MENU_TIME_x_M_y_S(0,20)	,HEAT_L8			,93			},
	{OB_HEATER|END_TIME_OR_FY			,MENU_TIME_x_M_y_S(0,30)	,HEAT_L7			,100			},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,5)		,0           	,DISP_UPDATE},
	{OB_MOTO_HEAT_1|END_TIME			,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L5		},
	{OB_HEATER|END_TIME					,MENU_TIME_x_M_y_S(0,5)		,HEAT_L6			,0				},
	{OB_HEATER|END_TIME					,MENU_TIME_x_M_y_S(0,20)	,HEAT_L6			,0				},
	{OB_MOTO_HEAT_1|END_TIME			,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L3		},
	{OB_HEATER|END_TIME					,MENU_TIME_x_M_y_S(0,5)		,HEAT_L2			,0				},
	{OB_MOTO_HEAT_1|END_TIME			,MENU_TIME_x_M_y_S(0,20)	,MOTOR_MODE 	,MOTO_L6		},
	{OB_HEATER|END_TIME					,MENU_TIME_x_M_y_S(0,5)		,HEAT_L2			,0				},
	{OB_MOTOR|END_TIME					,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L7		},
	{OB_HEATER|END_TIME					,MENU_TIME_x_M_y_S(0,5)		,HEAT_L2			,0				},
	{OB_MOTOR|END_TIME					,MENU_TIME_x_M_y_S(0,20)	,MOTOR_MODE 	,MOTO_L4		},
	{OB_MOTOR|END_TIME					,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L8		},
	{OB_HEATER|END_TIME					,MENU_TIME_x_M_y_S(0,5)		,HEAT_L2			,0				},
	{OB_MOTOR|END_TIME					,MENU_TIME_x_M_y_S(0,20)	,MOTOR_MODE 	,MOTO_L5		},
	{OB_MOTOR|END_TIME					,MENU_TIME_x_M_y_S(0,5)		,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME					,MENU_TIME_x_M_y_S(0,40)	,MOTOR_MODE 	,MOTO_L8		},
	{OB_MOTOR|END_TIME					,MENU_TIME_x_M_y_S(0,5)		,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME					,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L7		},
	{OB_MOTOR|END_TIME					,MENU_TIME_x_M_y_S(0,5)		,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME					,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L7		},
	{OB_MOTOR|END_TIME					,MENU_TIME_x_M_y_S(0,20)	,MOTOR_MODE 	,MOTO_L4		},	
	{OB_MOTOR|END_TIME					,MENU_TIME_x_M_y_S(0,5)		,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME					,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L7		},	
	{0,0,0,0,0},
};
uchar code MENU_CB_HOT_SHI_FNT[][5] = {//十分浓汤
	{OB_HEATER|END_TIME_OR_TEMP   	,MENU_TIME_x_M_y_S(20,00)	,HEAT_L10		,75			}, 	
	{OB_HEATER|END_TIME_OR_TEMP   	,MENU_TIME_x_M_y_S(20,00)	,HEAT_L9			,83			}, 
	{OB_HEATER|END_TIME_OR_FY			,MENU_TIME_x_M_y_S(4,00)	,HEAT_L5			,0				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0           	,DISP_UPDATE},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE 	,MOTO_L3		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0           	,0				}, 
	{OB_HEATER|END_TIME   		   	,MENU_TIME_x_M_y_S(2,00)	,HEAT_L2			,0				},
	{OB_HEATER|END_TIME   		   	,MENU_TIME_x_M_y_S(1,30)	,HEAT_L1			,0				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,40)	,MOTOR_MODE		,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE		,MOTO_L4		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE		,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,20)	,MOTOR_MODE		,MOTO_L5		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_REPEAT|END_TIME        		,MENU_TIME_x_M_y_S(2,40)   ,3           	,1				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				}, 
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,25)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,25)	,MOTOR_MODE 	,MOTO_L7		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0           	,0				},
	{OB_REPEAT|END_TIME        		,MENU_TIME_x_M_y_S(12,50)	,3           	,1 			},
	{OB_H_30S_M_5S|END_TIME				,MENU_TIME_x_M_y_S(1,0)		,HEAT_L2			,0				},
	{OB_NULL|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_H_60S_M_5S|END_TIME				,MENU_TIME_x_M_y_S(3,0)		,HEAT_L1			,0				},
	{0,0,0,0,0}
}; 
uchar code MENU_CB_HOT_YANG_SZ[][5] = {//养生粥
	{OB_H_30S_M_5S|END_TIME_OR_TEMP	,MENU_TIME_x_M_y_S(20,00)	,HEAT_L8			,75			}, 	
	{OB_H_30S_M_5S|END_TIME_OR_TEMP	,MENU_TIME_x_M_y_S(20,00)	,HEAT_L8			,87			}, 
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0           	,0				},
	{OB_HEATER|END_TIME_OR_FY			,MENU_TIME_x_M_y_S(4,00)	,HEAT_L5			,0				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,25)	,0           	,DISP_UPDATE},
	{OB_HEATER|END_TIME   		   	,MENU_TIME_x_M_y_S(4,00)	,HEAT_L2			,0				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE		,MOTO_L1		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0           	,0				},
	{OB_H_120S_M_5S|END_TIME			,MENU_TIME_x_M_y_S(6,00)	,HEAT_L2			,0				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(1,00)	,0           	,0				},
	{OB_HEATER|END_TIME   		   	,MENU_TIME_x_M_y_S(0,35)	,HEAT_L1			,0				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,25)	,0           	,0				},
	{OB_REPEAT|END_TIME        		,MENU_TIME_x_M_y_S(12,00)  ,2           	,1				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,30)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,5)		,MOTOR_MODE		,MOTO_L1		},
	{0,0,0,0,0}	       
}; 
uchar code MENU_CB_HOT_ZI_BH[][5] = {//滋补糊
	{OB_H_60S_M_5S|END_TIME_OR_TEMP  ,MENU_TIME_x_M_y_S(20,00)	,HEAT_L10      ,75			},
	{OB_H_30S_M_5S|END_TIME_OR_TEMP  ,MENU_TIME_x_M_y_S(20,00)	,HEAT_L8       ,87			},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_HEATER|END_TIME_OR_FY   		,MENU_TIME_x_M_y_S(6,00)	,HEAT_L5      	,100			},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0           	,DISP_UPDATE},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,30)	,0           	,0				},
	{OB_HEATER|END_TIME   				,MENU_TIME_x_M_y_S(2,00)	,HEAT_L2      	,100			},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,30)	,0           	,0				},
	{OB_HEATER|END_TIME   				,MENU_TIME_x_M_y_S(2,00)	,HEAT_L1      	,100			},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(2,00)	,0           	,0				},

	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,25)	,MOTOR_MODE 	,MOTO_L8		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,15)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,15)	,0           	,0				},
	{OB_REPEAT|END_TIME					,MENU_TIME_x_M_y_S(10,05)	,3 				,1				},
	{0,0,0,0,0}
}; 
uchar code MENU_CB_HOT_DUN_Z[][5] = {//炖煮
	{OB_HEATER|END_TEMP  				,MENU_TIME_x_M_y_S(24,00)	,HEAT_L10 		,85			},
	{OB_HEATER|END_TIME_OR_FY   		,MENU_TIME_x_M_y_S(5,40)	,HEAT_L3 		,0				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0      			,DISP_UPDATE},
	{OB_HEATER|END_TIME		   		,MENU_TIME_x_M_y_S(60,0)	,HEAT_L1 		,0				},
	{0,0,0,0,0}
}; 
uchar code MENU_CB_HOT_GUO_RL[][5] = {//果仁露
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,5) 	,MOTOR_MODE 	,MOTO_L2		},
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,28)	,MOTOR_MODE 	,MOTO_L8		},
	{OB_NULL|END_TIME    				,MENU_TIME_x_M_y_S(0,2) 	,0           	,0 			},
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,5) 	,MOTOR_MODE 	,MOTO_L2		},
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,28)	,MOTOR_MODE 	,MOTO_L8		},
	{OB_NULL|END_TIME    				,MENU_TIME_x_M_y_S(0,2) 	,0           	,0 			},
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,5) 	,MOTOR_MODE 	,MOTO_L2		},
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,28)	,MOTOR_MODE 	,MOTO_L8		},
	{OB_NULL|END_TIME    				,MENU_TIME_x_M_y_S(0,2) 	,0           	,0 			},
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,5) 	,MOTOR_MODE 	,MOTO_L2		},
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L8		},
	{0,0,0,0,0}	  						 
};
uchar code MENU_CB_HOT_SHI_HYS[][5] = {//石斛药膳
	{OB_H_60S_M_5S|END_TIME_OR_TEMP  ,MENU_TIME_x_M_y_S(20,00)	,HEAT_L10      ,75			},
	{OB_H_30S_M_5S|END_TIME_OR_TEMP  ,MENU_TIME_x_M_y_S(20,00)	,HEAT_L8       ,87			},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_HEATER|END_TIME_OR_FY   		,MENU_TIME_x_M_y_S(6,00)	,HEAT_L5      	,100			},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0           	,DISP_UPDATE},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,30)	,0           	,0				},
	{OB_HEATER|END_TIME   				,MENU_TIME_x_M_y_S(2,00)	,HEAT_L2      	,100			},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,30)	,0           	,0				},
	{OB_HEATER|END_TIME   				,MENU_TIME_x_M_y_S(2,00)	,HEAT_L1      	,100			},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(2,00)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,15)	,MOTOR_MODE 	,MOTO_L4		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,30)	,0           	,0				},
	{OB_REPEAT|END_TIME					,MENU_TIME_x_M_y_S(5,30)	,3 				,1				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,5)		,MOTOR_MODE 	,MOTO_L1		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,30)	,0           	,0				},
	{OB_HEATER|END_TIME   				,MENU_TIME_x_M_y_S(1,00)	,HEAT_L1      	,0				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,30)	,0           	,0				},
	{OB_HEATER|END_TIME   				,MENU_TIME_x_M_y_S(0,30)	,HEAT_L1      	,0				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,30)	,0           	,0				},
	{OB_HEATER|END_TIME   				,MENU_TIME_x_M_y_S(0,30)	,HEAT_L1      	,0				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,30)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L1		},
	{0,0,0,0,0},
}; 
uchar code MENU_CB_HOT_YIN_EG[][5] = {//银耳羹
	{OB_HEATER|END_TEMP					,MENU_TIME_x_M_y_S(24,00)	,HEAT_L10 		,83			},
	{OB_HEATER|END_TIME_OR_FY   		,MENU_TIME_x_M_y_S(5,40)	,HEAT_L4 		,0				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0      			,DISP_UPDATE},
	{OB_HEATER|END_TIME		   		,MENU_TIME_x_M_y_S(90,0)	,HEAT_L1 		,0				},
	{0,0,0,0,0}		 	  						 
}; 
uchar code MENU_CB_HOT_YU_MZ[][5] = {//玉米汁
	{OB_H_30S_M_5S|END_TIME_OR_TEMP	,MENU_TIME_x_M_y_S(20,00)	,HEAT_L9      	,83			},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_HEATER|END_TIME_OR_FY   		,MENU_TIME_x_M_y_S(4,00)	,HEAT_L4      	,100			},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,20)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_HEATER|END_TIME   				,MENU_TIME_x_M_y_S(2,00)	,HEAT_L2      	,100			},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0           	,DISP_UPDATE},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(1,00)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L3		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L3		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,20)	,MOTOR_MODE 	,MOTO_L7		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0           	,0				},
	{OB_REPEAT|END_TIME					,MENU_TIME_x_M_y_S(1,40)	,3 				,1				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,20)	,MOTOR_MODE 	,MOTO_L6		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0           	,0				},
	{OB_REPEAT|END_TIME					,MENU_TIME_x_M_y_S(4,10)	,3 				,1				},
	{OB_HEATER|END_TIME   				,MENU_TIME_x_M_y_S(1,00)	,HEAT_L1      	,0				},
	{0,0,0,0,0}
}; 
uchar code MENU_CB_HOT_BING_QL[][5] = {//冰淇淋
	{OB_MOTOR|END_TIME     			 	,MENU_TIME_x_M_y_S(0,40) 	,MOTOR_MODE 	,MOTO_L8		}, 
	{OB_NULL|END_TIME        			,MENU_TIME_x_M_y_S(0,3)  	,0           	,0 			}, 
	{OB_MOTOR|END_TIME     			 	,MENU_TIME_x_M_y_S(0,40) 	,MOTOR_MODE 	,MOTO_L8		}, 
	{0,0,0,0,0}	 	  						 
}; 
uchar code MENU_CB_HOT_JING_LT[][5] = {//精力汤
	{OB_MOTOR|END_TIME     			 	,MENU_TIME_x_M_y_S(0,27) 	,MOTOR_MODE 	,MOTO_L10	}, 
	{OB_NULL|END_TIME        			,MENU_TIME_x_M_y_S(0,3)  	,0           	,0 			}, 
	{OB_REPEAT|END_TIME					,MENU_TIME_x_M_y_S(2,30)	,2 				,1				},
	{0,0,0,0,0}		 	  						 
}; 
uchar code MENU_CB_HOT_SETTING[][5] = {//设置
	{0,0,0,0,0}		 	  						 
}; 
uchar code MENU_CB_HOT_RE_HCJ[][5] = {//热烘除菌
	{OB_HEATER|END_TIME_OR_TEMP_OR_TEMP_CTRL	,MENU_TIME_x_M_y_S(20,00)	,HEAT_L2		,114			},
	{OB_MOTOR|END_TIME     			 				,MENU_TIME_x_M_y_S(0,20) 	,MOTOR_MODE ,MOTO_L1		},
	{OB_NULL|END_TIME        						,MENU_TIME_x_M_y_S(0,10)  	,0          ,0 			},
	{OB_MOTOR|END_TIME     			 				,MENU_TIME_x_M_y_S(0,20) 	,MOTOR_MODE ,MOTO_L1		},
	{OB_HEATER|END_TIME_OR_TEMP_OR_TEMP_CTRL	,MENU_TIME_x_M_y_S(5,00)	,HEAT_L1		,114			},
	{OB_MOTOR|END_TIME     			 				,MENU_TIME_x_M_y_S(0,20) 	,MOTOR_MODE ,MOTO_L1		},
	{OB_HEATER|END_TIME_OR_TEMP_OR_TEMP_CTRL	,MENU_TIME_x_M_y_S(3,50)	,HEAT_L1		,114			},
	{OB_NULL|END_TIME        						,MENU_TIME_x_M_y_S(2,00)  	,0          ,DISP_UPDATE},
	{0,0,0,0,0}
}; 
uchar code MENU_CB_HOT_SHI_FNJ[][5] = {//十分浓浆
	{OB_H_30S_M_5S|END_TIME_OR_TEMP  ,MENU_TIME_x_M_y_S(20,00)	,HEAT_L10      ,80			},
	{OB_H_30S_M_5S|END_TIME_OR_TEMP  ,MENU_TIME_x_M_y_S(20,00)	,HEAT_L9       ,87			},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_HEATER|END_TIME_OR_FY   		,MENU_TIME_x_M_y_S(5,00)	,HEAT_L6      	,100			},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,DISP_UPDATE},
	{OB_HEATER|END_TIME   				,MENU_TIME_x_M_y_S(3,0)		,HEAT_L2      	,100			},
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
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,20)	,MOTOR_MODE 	,MOTO_L6		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,10)	,0           	,0				},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,20)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME          		,MENU_TIME_x_M_y_S(0,20)	,MOTOR_MODE 	,MOTO_L7		},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,5)		,0           	,0				},
	{OB_REPEAT|END_TIME					,MENU_TIME_x_M_y_S(18,0)	,3 				,1				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,30)	,0           	,0				},
	{OB_HEATER|END_TIME   				,MENU_TIME_x_M_y_S(1,00)	,HEAT_L1      	,0				},
	{0,0,0,0,0},
}; 
uchar code MENU_CB_HOT_10_FKH_BIG[][5] = {//10分快糊 高水位
   {OB_H_30S_M_5S|END_TIME_OR_TEMP	,MENU_TIME_x_M_y_S(20,00)	,HEAT_L10      ,60         },
   {OB_H_30S_M_5S|END_TIME_OR_TEMP	,MENU_TIME_x_M_y_S(20,00)	,HEAT_L9       ,80         },
   {OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(0,30)   ,MOTOR_MODE    ,MOTO_L1    },
   {OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,10)   ,0             ,0          }, 
   {OB_HEATER|END_TIME_OR_TEMP_OR_FY,MENU_TIME_x_M_y_S(3,00)   ,HEAT_L8       ,87         },
	{OB_HEATER|END_TIME					,MENU_TIME_x_M_y_S(0,5)		,HEAT_L6			,0				},
   {OB_HEATER|END_TIME_OR_FY        ,MENU_TIME_x_M_y_S(6,00)   ,HEAT_L5       ,0          },
   {OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,20)   ,0             ,DISP_UPDATE}, 
   {OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(0,50)   ,MOTOR_MODE    ,MOTO_L1    },
   {OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(1,00)   ,MOTOR_MODE    ,MOTO_L4    },
   {OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,20)   ,0             ,0          }, 
   {OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(1,00)   ,MOTOR_MODE    ,MOTO_L5    },
   {OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,20)   ,0             ,0          },
	{OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(1,00)   ,MOTOR_MODE    ,MOTO_L1    },
   {OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,20)   ,0             ,0          },
	{OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(1,00)   ,MOTOR_MODE    ,MOTO_L4    },
   {OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,20)   ,0             ,0          }, 
	{OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(1,00)   ,MOTOR_MODE    ,MOTO_L5    },
   {OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,20)   ,0             ,0          }, 
   {OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(0,30)   ,MOTOR_MODE    ,MOTO_L4    },
   {0,0,0,0,0}                          
};
uchar code MENU_CB_HOT_10_FKH_MID[][5] = {//10分快糊 中水位
	{OB_H_30S_M_5S|END_TIME_OR_TEMP	,MENU_TIME_x_M_y_S(20,00)	,HEAT_L10		,60			},
	{OB_H_30S_M_5S|END_TIME_OR_TEMP	,MENU_TIME_x_M_y_S(20,00)	,HEAT_L9			,80			},
	{OB_HEATER|END_TIME_OR_TEMP_OR_FY,MENU_TIME_x_M_y_S(3,00)	,HEAT_L8			,87			},
	{OB_HEATER|END_TIME					,MENU_TIME_x_M_y_S(0,5)		,HEAT_L6			,0				},
	{OB_HEATER|END_TIME_OR_FY			,MENU_TIME_x_M_y_S(4,00)	,HEAT_L5			,0				},
	{OB_NULL|END_TIME    				,MENU_TIME_x_M_y_S(0,20)	,0           	,DISP_UPDATE}, 
	{OB_MOTOR|END_TIME					,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME					,MENU_TIME_x_M_y_S(1,00)	,MOTOR_MODE 	,MOTO_L4		},
	{OB_HEATER|END_TIME   				,MENU_TIME_x_M_y_S(0,5)		,HEAT_L3      	,0				},
	{OB_NULL|END_TIME    				,MENU_TIME_x_M_y_S(0,10)	,0           	,0 			}, 
	{OB_MOTOR|END_TIME					,MENU_TIME_x_M_y_S(1,00)	,MOTOR_MODE 	,MOTO_L5		},
	{OB_HEATER|END_TIME   				,MENU_TIME_x_M_y_S(0,5)		,HEAT_L3      	,0				},
	{OB_NULL|END_TIME    				,MENU_TIME_x_M_y_S(0,10)	,0           	,0 			}, 
	{OB_MOTOR|END_TIME					,MENU_TIME_x_M_y_S(1,00)	,MOTOR_MODE 	,MOTO_L4		},
	{0,0,0,0,0}		 	  						 
};
uchar code MENU_CB_HOT_10_FKH_SMALL[][5] = {//10分快糊 低水位
	{OB_H_30S_M_5S|END_TIME_OR_TEMP	,MENU_TIME_x_M_y_S(20,00)	,HEAT_L10		,60			},
	{OB_H_30S_M_5S|END_TIME_OR_TEMP	,MENU_TIME_x_M_y_S(20,00)	,HEAT_L9			,80			},
	{OB_HEATER|END_TIME_OR_TEMP_OR_FY,MENU_TIME_x_M_y_S(2,00)	,HEAT_L8			,87			},
	{OB_HEATER|END_TIME					,MENU_TIME_x_M_y_S(0,5)		,HEAT_L8			,0				},
	{OB_HEATER|END_TIME_OR_FY			,MENU_TIME_x_M_y_S(1,00)	,HEAT_L5			,0				},
	{OB_NULL|END_TIME    				,MENU_TIME_x_M_y_S(0,10)	,0           	,DISP_UPDATE}, 
	{OB_MOTOR|END_TIME					,MENU_TIME_x_M_y_S(0,10)	,MOTOR_MODE 	,MOTO_L1		},
	{OB_MOTOR|END_TIME					,MENU_TIME_x_M_y_S(1,00)	,MOTOR_MODE 	,MOTO_L4		},
	{OB_HEATER|END_TIME   				,MENU_TIME_x_M_y_S(0,20)	,HEAT_L3      	,0				},
	{OB_NULL|END_TIME    				,MENU_TIME_x_M_y_S(0,10)	,0           	,0 			}, 
	{OB_MOTOR|END_TIME					,MENU_TIME_x_M_y_S(1,00)	,MOTOR_MODE 	,MOTO_L5		},
	{OB_HEATER|END_TIME   				,MENU_TIME_x_M_y_S(0,5)		,HEAT_L3      	,0				},
	{OB_NULL|END_TIME    				,MENU_TIME_x_M_y_S(0,10)	,0           	,0 			}, 
	{OB_MOTOR|END_TIME					,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE 	,MOTO_L4		},
	{0,0,0,0,0}		 	  						 
};
uchar code MENU_CB_HOT_GUO_SZ[][5] = {//果蔬汁
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,20)	,MOTOR_MODE 	,MOTO_L8		}, 
	{OB_NULL|END_TIME    				,MENU_TIME_x_M_y_S(0,2)		,0           	,0 			}, 
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,20)	,MOTOR_MODE 	,MOTO_L2		}, 
	{OB_NULL|END_TIME    				,MENU_TIME_x_M_y_S(0,2) 	,0           	,0 			}, 
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,45)	,MOTOR_MODE 	,MOTO_L10	}, 
	{OB_NULL|END_TIME    				,MENU_TIME_x_M_y_S(0,2) 	,0           	,0 			}, 
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,25)	,MOTOR_MODE 	,MOTO_L10	}, 
	{OB_NULL|END_TIME    				,MENU_TIME_x_M_y_S(0,2) 	,0           	,0 			}, 
	{0,0,0,0,0}		 	 
}; 
uchar code MENU_CB_HOT_NAI_X[][5] = {//奶昔
   {OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(1,4)    ,MOTOR_MODE		,MOTO_L5		},
   {OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,2)    ,0         		,0      		},
   {OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(0,25)   ,MOTOR_MODE		,MOTO_L2		},
   {OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,2)    ,0         		,0      		},
   {OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(0,25)   ,MOTOR_MODE		,MOTO_L5		},
   {OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,2)    ,0         		,0      		},
   {0,0,0,0,0}
}; 
uchar code MENU_CB_HOT_QING_X[][5] = {//清洗
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,48)	,MOTOR_MODE		,MOTO_L10 	},
   {OB_NULL|END_TIME						,MENU_TIME_x_M_y_S(0,2)		,0					,0				},
   {0,0,0,0,0}
}; 
uchar code MENU_CB_HOT_DIY_TW[][5] = {//DIY调温
	{OB_H_30S_M_5S|END_TEMP				,MENU_TIME_x_M_y_S(30,0)	,HEAT_L10		,70			},
	{0,0,0,0,0}
}; 
uchar code MENU_CB_HOT_DIY_TS[][5] = {//DIY调速
	{OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(0,30)   ,MOTOR_MODE		,MOTO_L5		},
	{0,0,0,0,0}
};    
//******************真空冷杯*********************
uchar code MENU_CB_COLD_SHU_LDJ[][5] = {//熟料豆浆
	{OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(0,5)		,MOTOR_MODE		,MOTO_L2		},
	{OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(0,25)	,MOTOR_MODE		,MOTO_L10	},
	{OB_REPEAT|END_TIME        		,MENU_TIME_x_M_y_S(4,30)  ,2           	,1				},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_COLD_RUAN_GSZ[][5] = {//软果蔬汁
	{OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,2)    ,0         		,0      		},
	{OB_VACUUM|END_TIME              ,MENU_TIME_x_M_y_S(1,26)	,0					,0				},
	{OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,2)    ,0         		,0      		},
	{OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(0,24)	,MOTOR_MODE		,MOTO_L7		},
	{OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,4)    ,0         		,0      		},
	{OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(0,24)	,MOTOR_MODE		,MOTO_L7		},
	{OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,4)    ,0         		,0      		},
	{OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(0,28)	,MOTOR_MODE		,MOTO_L10	},
	{OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,4)    ,0         		,0      		},
	{OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(0,26)	,MOTOR_MODE		,MOTO_L10	},
	{OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,2)    ,0         		,0      		},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_COLD_GUO_RL[][5] = {//果仁露
	{OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(0,5)		,MOTOR_MODE		,MOTO_L2		},
	{OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(0,28)	,MOTOR_MODE		,MOTO_L8		},
	{OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,2)    ,0         		,0      		},
	{OB_REPEAT|END_TIME        		,MENU_TIME_x_M_y_S(1,45)  ,3           	,1				},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_COLD_ZHEN_KBX[][5] = {//真空保鲜
	{OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,2)    ,0         		,0      		},
	{OB_VACUUM|END_TIME              ,MENU_TIME_x_M_y_S(1,26)	,0					,0				},
	{OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,2)    ,0         		,0      		},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_COLD_GUO_CN[][5] = {//果菜泥
	{OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,2)    ,0         		,0      		},
	{OB_VACUUM|END_TIME              ,MENU_TIME_x_M_y_S(1,26)	,0					,0				},
	{OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,2)    ,0         		,0      		},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_COLD_JIANG_L[][5] = {//酱料
	{OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(1,00)	,MOTOR_MODE		,MOTO_L6		},
	{OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,2)    ,0         		,0      		},
	{OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(1,00)	,MOTOR_MODE		,MOTO_L7		},
	{OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,2)    ,0         		,0      		},
	{OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(1,00)	,MOTOR_MODE		,MOTO_L5		},
	{OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,2)    ,0         		,0      		},
	{OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(1,00)	,MOTOR_MODE		,MOTO_L8		},
	{OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,2)    ,0         		,0      		},
	{OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(1,00)	,MOTOR_MODE		,MOTO_L8		},
	{OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,2)    ,0         		,0      		},
	{OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(0,48)	,MOTOR_MODE		,MOTO_L8		},
	{OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,2)    ,0         		,0      		},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_COLD_BING_QL[][5] = {//冰淇淋
	{OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(0,40)	,MOTOR_MODE		,MOTO_L8		},
	{OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,3)    ,0         		,0      		},
	{OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(0,40)	,MOTOR_MODE		,MOTO_L8		},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_COLD_JING_LT[][5] = {//精力汤
	{OB_MOTOR|END_TIME     			 	,MENU_TIME_x_M_y_S(0,27) 	,MOTOR_MODE 	,MOTO_L10	}, 
	{OB_NULL|END_TIME        			,MENU_TIME_x_M_y_S(0,3)  	,0           	,0 			}, 
	{OB_REPEAT|END_TIME					,MENU_TIME_x_M_y_S(2,30)	,2 				,1				},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_COLD_SETTING[][5] = {//设置
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_COLD_GUO_SZ[][5] = {//果蔬汁
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,20)	,MOTOR_MODE 	,MOTO_L8		}, 
	{OB_NULL|END_TIME    				,MENU_TIME_x_M_y_S(0,2)		,0           	,0 			}, 
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,20)	,MOTOR_MODE 	,MOTO_L2		}, 
	{OB_NULL|END_TIME    				,MENU_TIME_x_M_y_S(0,2) 	,0           	,0 			}, 
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,45)	,MOTOR_MODE 	,MOTO_L10	}, 
	{OB_NULL|END_TIME    				,MENU_TIME_x_M_y_S(0,2) 	,0           	,0 			}, 
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,25)	,MOTOR_MODE 	,MOTO_L10	}, 
	{OB_NULL|END_TIME    				,MENU_TIME_x_M_y_S(0,2) 	,0           	,0 			}, 
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_COLD_NAI_X[][5] = {//奶昔
   {OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(1,4)    ,MOTOR_MODE		,MOTO_L5		},
   {OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,2)    ,0         		,0      		},
   {OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(0,25)   ,MOTOR_MODE		,MOTO_L2		},
   {OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,2)    ,0         		,0      		},
   {OB_MOTOR|END_TIME               ,MENU_TIME_x_M_y_S(0,25)   ,MOTOR_MODE		,MOTO_L5		},
   {OB_NULL|END_TIME                ,MENU_TIME_x_M_y_S(0,2)    ,0         		,0      		},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_COLD_QING_X[][5] = {//清洗
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,48)	,MOTOR_MODE		,MOTO_L10 	},
   {OB_NULL|END_TIME						,MENU_TIME_x_M_y_S(0,2)		,0					,0				},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_COLD_DIY_TS[][5] = {//DIY调速
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE		,MOTO_L5 	},
	{0,0,0,0,0}			 	  						 
}; 
//***********************养生杯******************
uchar code MENU_CB_YS_YANG_SC[][5] = {//养生茶
	{OB_HEATER|END_TEMP					,MENU_TIME_x_M_y_S(24,00)	,HEAT_L10 		,83			},
	{OB_HEATER|END_TIME		   		,MENU_TIME_x_M_y_S(5,40)	,HEAT_L4 		,0				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0      			,DISP_UPDATE},
	{OB_HEATER|END_TIME		   		,MENU_TIME_x_M_y_S(90,0)	,HEAT_L1 		,0				},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_YS_YIN_EG[][5] = {//银耳羹
	{OB_HEATER|END_TEMP					,MENU_TIME_x_M_y_S(24,00)	,HEAT_L10 		,83			},
	{OB_HEATER|END_TIME		   		,MENU_TIME_x_M_y_S(5,40)	,HEAT_L4 		,0				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0      			,DISP_UPDATE},
	{OB_HEATER|END_TIME		   		,MENU_TIME_x_M_y_S(90,0)	,HEAT_L1 		,0				},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_YS_45DU_CN[][5] = {//45度冲奶
	{OB_HEATER|END_TEMP					,MENU_TIME_x_M_y_S(24,00)	,HEAT_L10 		,83			},
	{OB_HEATER|END_TIME		   		,MENU_TIME_x_M_y_S(5,40)	,HEAT_L4 		,0				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0      			,DISP_UPDATE},
	{OB_HEATER|END_TIME		   		,MENU_TIME_x_M_y_S(90,0)	,HEAT_L1 		,0				},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_YS_HUA_GC[][5] = {//花果茶
	{OB_HEATER|END_TEMP					,MENU_TIME_x_M_y_S(24,00)	,HEAT_L10 		,83			},
	{OB_HEATER|END_TIME		   		,MENU_TIME_x_M_y_S(5,40)	,HEAT_L4 		,0				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0      			,DISP_UPDATE},
	{OB_HEATER|END_TIME		   		,MENU_TIME_x_M_y_S(90,0)	,HEAT_L1 		,0				},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_YS_YAO_S[][5] = {//药膳
	{OB_HEATER|END_TEMP					,MENU_TIME_x_M_y_S(24,00)	,HEAT_L10 		,83			},
	{OB_HEATER|END_TIME		   		,MENU_TIME_x_M_y_S(5,40)	,HEAT_L4 		,0				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0      			,DISP_UPDATE},
	{OB_HEATER|END_TIME		   		,MENU_TIME_x_M_y_S(90,0)	,HEAT_L1 		,0				},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_YS_YAN_W[][5] = {//燕窝
	{OB_HEATER|END_TEMP					,MENU_TIME_x_M_y_S(24,00)	,HEAT_L10 		,83			},
	{OB_HEATER|END_TIME		   		,MENU_TIME_x_M_y_S(5,40)	,HEAT_L3 		,0				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0      			,DISP_UPDATE},
	{OB_HEATER|END_TIME		   		,MENU_TIME_x_M_y_S(90,0)	,HEAT_L1 		,0				},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_YS_ZHOU_P[][5] = {//粥品
	{OB_HEATER|END_TEMP					,MENU_TIME_x_M_y_S(24,00)	,HEAT_L10 		,83			},
	{OB_HEATER|END_TIME		   		,MENU_TIME_x_M_y_S(5,40)	,HEAT_L3 		,0				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0      			,DISP_UPDATE},
	{OB_HEATER|END_TIME		   		,MENU_TIME_x_M_y_S(90,0)	,HEAT_L1 		,0				},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_YS_ZI_BH[][5] = {//滋补糊
	{OB_HEATER|END_TEMP					,MENU_TIME_x_M_y_S(24,00)	,HEAT_L10 		,83			},
	{OB_HEATER|END_TIME		   		,MENU_TIME_x_M_y_S(5,40)	,HEAT_L3 		,0				},
	{OB_NULL|END_TIME           		,MENU_TIME_x_M_y_S(0,20)	,0      			,DISP_UPDATE},
	{OB_HEATER|END_TIME		   		,MENU_TIME_x_M_y_S(90,0)	,HEAT_L1 		,0				},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_YS_SETTING[][5] = {//设置
	{0,0,0,0,0}
}; 
uchar code MENU_CB_YS_DIY_TW[][5] = {//DIY加热
	{OB_HEATER|END_TEMP				   ,MENU_TIME_x_M_y_S(30,0)	,HEAT_L10			,100		},
	{0,0,0,0,0}			 	  						 
}; 
//********************研磨杯********************
uchar code MENU_CB_YM_YAO_SF[][5] = {//药膳粉
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(1,00)	,MOTOR_MODE		,MOTO_L9 	},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_YM_WU_GF[][5] = {//五谷粉
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(1,00)	,MOTOR_MODE		,MOTO_L7 	},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_YM_TIAO_LF[][5] = {//调料粉
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(1,00)	,MOTOR_MODE		,MOTO_L7 	},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_YM_MI_F[][5] = {//米粉
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(2,00)	,MOTOR_MODE		,MOTO_L7 	},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_YM_DOU_F[][5] = {//豆粉
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(1,00)	,MOTOR_MODE		,MOTO_L7 	},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_YM_BING_TF[][5] = {//冰糖粉
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(1,00)	,MOTOR_MODE		,MOTO_L7 	},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_YM_REN_SF[][5] = {//人参粉
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(1,00)	,MOTOR_MODE		,MOTO_L7 	},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_YM_E_J[][5] = {//阿胶粉
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(1,00)	,MOTOR_MODE		,MOTO_L7 	},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_YM_SETTING[][5] = {//设置
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_YM_DIY_TS[][5] = {//DIY调速
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE		,MOTO_L5 	},
	{0,0,0,0,0}			 	  						 
}; 
//********************多功能杯******************
uchar code MENU_CB_DGNB_QIE_S[][5] = {
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(2,0)		,MOTOR_MODE		,MOTO_L4 	},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_DGNB_JIAO_R[][5] = {
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,30)	,MOTOR_MODE		,MOTO_L4 	},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_DGNB_HUO_M[][5] = {
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(10,0)	,MOTOR_MODE		,MOTO_L1 	},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_DGNB_QIE_P[][5] = {
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(2,0)		,MOTOR_MODE		,MOTO_L4 	},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_DGNB_JIAO_C[][5] = {
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(0,15)	,MOTOR_MODE		,MOTO_L3 	},
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_DGNB_SETTING[][5] = {
	{0,0,0,0,0}			 	  						 
}; 
uchar code MENU_CB_DGNB_DIY_TS[][5] = {//打发
	{OB_MOTOR|END_TIME   				,MENU_TIME_x_M_y_S(2,0)		,MOTOR_MODE		,MOTO_L5 	},
	{0,0,0,0,0}			 	  						 
}; 