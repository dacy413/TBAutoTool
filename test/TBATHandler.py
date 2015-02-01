# -*- coding: utf-8 -*-
import top.api
import time
import ConfigParser
import logger

logger.initLogManager()
g_config = ConfigParser.ConfigParser()
g_config.read("config.ini")
#g_url = "gw.api.tbsandbox.com"
g_url = "gw.api.taobao.com"
g_get_full_info_flag = 1
g_select_interval = 20

def send_goods(client_id="1023079608",client_secret="sandbox0522e2394ad8813381ce7f457",access_token="61025106bd3112dc211ee82e9cd794f0c131fa2608f2253182558410"):
    while True:
        # print("===========================>>NEW LOOP<<==========================")
        logger.log(1,"===========================>>NEW LOOP START<<==========================")
        import pdb;pdb.set_trace()
        #=====================================get all of trades===============================#
        # req_get_all_trade = top.api.TradesSoldGetRequest(g_url)#get all trades
        req_get_all_trade=top.api.TradesSoldIncrementGetRequest(g_url)#get increament trades
        req_get_all_trade.set_app_info(top.appinfo(client_id, client_secret))
        req_get_all_trade.fields = "seller_nick,buyer_nick,title,type,created,sid,tid,seller_rate,buyer_rate,\
                            status,payment,discount_fee,adjust_fee,post_fee,total_fee,pay_time"
        # set start and end time
        t_cur_time = time.time()
        t_start_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(t_cur_time-60*60*12))
        t_end_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(t_cur_time))
        req_get_all_trade.start_modified = t_start_time
        req_get_all_trade.end_modified = t_end_time
        # print("====>>CURRENT TIME %s"%t_end_time)
        logger.log(2,"====>>CURRENT TIME %s"%t_end_time)
        # req_get_all_trade.status = "WAIT_SELLER_SEND_GOODS"#only process WAIT_SELLER_SEND_GOODS trades
        #=====================================get a trade full info============================#
        req_get_one_trade = top.api.TradeFullinfoGetRequest(g_url)
        req_get_one_trade.set_app_info(top.appinfo(client_id, client_secret))
        req_get_one_trade.fields = "status,buyer_message,tid"
        #=====================================send goods for a trade===========================#
        req_send_goods = top.api.LogisticsDummySendRequest(g_url)
        req_send_goods.set_app_info(top.appinfo(client_id, client_secret))

        try:
            resp_get_all_trade = req_get_all_trade.getResponse(access_token)
            # for i in resp_get_all_trade['trades_sold_get_response']['trades']['trade']:
            if resp_get_all_trade['trades_sold_increment_get_response']['total_results'] != 0:
                for i in resp_get_all_trade['trades_sold_increment_get_response']['trades']['trade']:
                    logger.log(2,"====>>SELECT TRADE TID:%s,STATUS:%s"%(i['tid'],i['status']))
                    if i["status"] == "WAIT_SELLER_SEND_GOODS":
                        req_send_goods.tid = i["tid"]
                        # import pdb;pdb.set_trace();
                        try:
                            logger.log(2,"====>>SEND GOODS TID:%s,STATUS:%s"%(i["tid"],i["status"]))
                            resp_send_goods = req_send_goods.getResponse(access_token)
                            # ====set tid for get trade full info==== #
                            if g_get_full_info_flag:
                                req_get_one_trade.tid = i["tid"]
                                resp_get_one_trade = req_get_one_trade.getResponse(access_token)
                                logger.log(1,"===>>AFTER SEND GOODS TID STATUS:%s"%resp_get_one_trade['trade_fullinfo_get_response']['trade']['status'])
                                time.sleep(g_select_interval)
                        except Exception as e:
                            logger.log(3,"====>>AN EXCEPTION:%s IN SEND GOODS"%e)
                            break
        except Exception as e:
            logger.log(3,"====>>AN EXCEPTION:%s"%e)
            break
        time.sleep(g_select_interval)
        logger.log(1,"===========================>>NEW LOOP END<<==========================")

if __name__ == '__main__':
    if int(g_config.get("app","run_mode")) == 1:
        send_goods()
    else:
        send_goods(g_config.get("app","client_id"),g_config.get("app","client_secret"),g_config.get("app","access_token"))
