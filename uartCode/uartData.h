#ifndef UARTDATA_H_
#define UARTDATA_H_

#include <SN8F5829.H>

//Y26's slaveUart is uart2.
#define UART0_OPEN

#define UART_HEADER_FA      0xFA
#define UART_HEADER_FB      0xFB
#define END_LINE_DATA       0x0A

#define RX_DATA_LEN         (7)
#define UART_RX_END_ONCE    RX_DATA_LEN


struct wifi_uart_try_send{
    uint8_t header1;
    
    uint8_t sysStatus;
    uint8_t fyValue;
    uint8_t fyAdStand;
    uint8_t fyAdDistance;
    
    uint8_t curFyFlag;
    uint8_t curTemp;
    uint8_t jumpJudgeTemp;
    uint8_t tempTarget;

    uint8_t MotoData;
    uint8_t HeatData;

    uint8_t motoCurH;
    uint8_t motoCurL;

    uint8_t remainWorkTimeHour;
    uint8_t remainWorkTimeMin;
    uint8_t remainWorkTimeSec;

    uint8_t workedTimeHour;
    uint8_t workedTimeMin;
    uint8_t workedTimeSec;
    
    uint8_t endLineData;
};

#ifdef UART0_OPEN
#define UART0_BAUD_RATE     (9600/100)          //4800 or 9600
#define UART0_MODE          (1)                 //0 or 1
#define UART0_BD0_EN        (0X20)
#define SMOD0_DUBLE_BAUD    (0X20)
#define UART0_PULL_UP       (~(0X04|0X08))

void uart0Init(void);
static void WifiUartTryDataUpdate(struct wifi_uart_try_send * dataToSend);
void WifiUartTrySendData(void);
#endif

#endif