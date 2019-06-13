使用说明：
1. usb转串口必须COM5
2. 下位机通信波特率必须9600
3. 必须64位系统
4. 导出图像存于.\sqlite3\image
5. 双击serialPortDataProcess.exe运行

project说明：
1. 程序基于python开发， 源码：databaseProcess.py, matPlotFromDb.py, serialPortDataProcess.py
2. 使用的python进行串口数据获取及可视化，数据库保存数据
3. 兼容了slqite3及progestsql两种数据库。为了更好的可移植性及兼容性，使用的sqlite3，见参考链接1
4. 数据位于.\sqlite3\database\menuDebugData, 使用时务必每天备份，备份方法参考链接2
5. 版本管理使用git，git及python见参考链接3
6. 对每次的数据生成3张图片，工作时间-温度， 工作时间-防溢数据，工作时间-电机电热数据
7. 使用须有对应下位机的串口, 见移植说明

移植说明：
1. 使用须移植串口模块，下位机必须多余的串口
2. 数据排序必须按照.\uartCode\uartCode.h中wifi_uart_try_send结构
3. 最好每秒发送完整一帧数据， 每帧数据间隔不得超过1.5s
4. 详情见.\uartCode\uartCode.c 中注释

参考链接：
1. https://www.sqlite.org/faq.html
2. https://blog.csdn.net/testman007/article/details/26466319
3. https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431608990315a01b575e2ab041168ff0df194698afac000