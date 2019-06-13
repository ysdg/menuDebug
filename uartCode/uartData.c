#include "uartData.h"
#include "INCLUDES.H"

#ifdef UART0_OPEN
/**
 * @brief Fcpu should be Fosc = 32MHz and baterate = 9600, interrupt is disable.
 * 
 */
void uart0Init(void)
{
    REN0    = 1;
    S0CON  |= (UART0_MODE<<6);
    S0CON2 |= UART0_BD0_EN;
    S0M20   = 0;
    PCON   &= ~SMOD0_DUBLE_BAUD;
    P0OC   &= UART0_PULL_UP;
    P0M    |= 0X04;
    P0M    &= ~0X08;
    P0     |= 0X04;
    
    S0RELH = L_SRELH_9600;
    S0RELL = L_SRELL_9600;

    EU0RX   = 0;
    EU0TX   = 0;
}

/**
 * @brief: must work 1s once.
 * 
 * @param dataToSend: 
 */
static void WifiUartTryDataUpdate(struct wifi_uart_try_send * dataToSend)
{
    static uint32_t xdata cnt = 0;

    cnt = gBSysType==SysModel_Work ? cnt+1 : 0;

    dataToSend->header1         = UART_HEADER_FA;
    dataToSend->sysStatus       = gBSysType;
    dataToSend->fyValue         = ADCdata.FyValue;
    dataToSend->fyAdStand       = ADCdata.fyAdStand;
    dataToSend->fyAdDistance    = ADCdata.fyAdDistance;
    dataToSend->curFyFlag       = gBFyType;
    dataToSend->curTemp         = ADCdata.DataTure;
    dataToSend->jumpJudgeTemp   = g_MenuCtrl.jumpJudgeTemp;
    dataToSend->tempTarget      = g_MenuCtrl.tempTarget;
    dataToSend->MotoData        = g_SlaveUart.sendDataBuf[3];
    dataToSend->HeatData        = g_SlaveUart.sendDataBuf[4];
    dataToSend->motoCurH        = g_SlaveUart.recvMotoDataH;
    dataToSend->motoCurL        = g_SlaveUart.recvMotoDataL;

    dataToSend->remainWorkTimeHour  = g_MenuMessage.curChoiceMenuRealWorkTime/3600/10;
    dataToSend->remainWorkTimeMin   = (g_MenuMessage.curChoiceMenuRealWorkTime%3600)/60/10;
    dataToSend->remainWorkTimeSec   = (g_MenuMessage.curChoiceMenuRealWorkTime%60)/10;
    dataToSend->workedTimeHour      = cnt/3600;
    dataToSend->workedTimeMin       = (cnt%3600)/60;
    dataToSend->workedTimeSec       = (cnt%60);
    dataToSend->endLineData         = END_LINE_DATA;

}

/**
 * @brief: just for test. should work 5ms once.
 * 
 * @param dataToSend: 
 */
void WifiUartTrySendData(void)
{        
    static struct wifi_uart_try_send xdata dataToSend = {0};
    static uint8_t xdata finishFlag=0, *ptr=(uint8_t*)&dataToSend, fyFlag=0;
    
    fyFlag      = gBFyType ? 1 : (finishFlag ? 0 : 1);
    if(gb1sFlag)
    {
        WifiUartTryDataUpdate(&dataToSend);
        dataToSend.curFyFlag    = fyFlag;
        finishFlag = 0;
        ptr = (uint8_t *)&dataToSend;
    }
    if(finishFlag==0 && gBSysType==SysModel_Work)
    {
        // S0BUF = 0X55;
        S0BUF = *ptr++;
        if( (ptr<(uint8_t*)&dataToSend) || 
            (ptr >= (((uint8_t*)&dataToSend) + sizeof(struct wifi_uart_try_send))))
        {
            ptr = (uint8_t *)&dataToSend;
            finishFlag = 1;
        }
    }
}  


#endif