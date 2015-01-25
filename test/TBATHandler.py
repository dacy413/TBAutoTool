# -*- coding: utf-8 -*-
import top.api
import time

g_url = "gw.api.tbsandbox.com"

def send_goods(client_id="1023079608",client_secret="sandbox0522e2394ad8813381ce7f457",access_token="6101f21f5df655ca131999e3b72ef19b085defe92c85d213651880146"):
    while True:
        print("====>>NEW LOOP")
        #=====================================get all of trades===============================#
        req_get_all_trade = top.api.TradesSoldGetRequest(g_url)
        # req_get_all_trade=top.api.TradesSoldIncrementGetRequest(g_url)
        req_get_all_trade.set_app_info(top.appinfo(client_id, client_secret))
        req_get_all_trade.fields = "seller_nick,buyer_nick,title,type,created,sid,tid,seller_rate,buyer_rate,\
                            status,payment,discount_fee,adjust_fee,post_fee,total_fee,pay_time"
        #=====================================get a trade full info============================#
        req_get_one_trade = top.api.TradeFullinfoGetRequest(g_url)
        req_get_one_trade.set_app_info(top.appinfo(client_id, client_secret))
        req_get_one_trade.fields = "status,buyer_message,tid"
        #=====================================send goods for a trade===========================#
        req_send_goods = top.api.LogisticsDummySendRequest(g_url)
        req_send_goods.set_app_info(top.appinfo(client_id, client_secret))

        try:
            resp_get_all_trade = req_get_all_trade.getResponse(access_token)
            for i in resp_get_all_trade['trades_sold_get_response']['trades']['trade']:
                print("====>>SELECT TRADE STATUS:%s,TID:%s"%(i["status"],i["tid"]))
                if i["status"] == "WAIT_SELLER_SEND_GOODS":
                    print("========>>NEW TRADE NO SEND GOODS TID:%s"%i["tid"])
                    req_send_goods.tid = i["tid"]
                    # import pdb;pdb.set_trace();
                    try:
                        print("========>>BEFORE SEND GOODS TID:%s,STATUS:%s"%(i["tid"],i["status"]))
                        resp_send_goods = req_send_goods.getResponse(access_token)
                        # ====set tid for get trade full info==== #
                        req_get_one_trade.tid = i["tid"]
                        resp_get_one_trade = req_get_one_trade.getResponse(access_token)
                        print("========>>AFTER SEND GOODS TID STATUS:%s"%resp_get_one_trade['trade_fullinfo_get_response']['trade']['status'])
                        time.sleep(5)
                    except Exception as e:
                        print("====>>AN EXCEPTION:",e)
                        break
        except Exception as e:
            print("====>>AN EXCEPTION:",e)
            break
        time.sleep(10)