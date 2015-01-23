# -*- coding: utf-8 -*-

import sys

sys.path.append('/home/dacy/workspace/TBAutoTool/test/top/api')

import top.api
req=top.api.TradesSoldGetRequest("gw.api.tbsandbox.com",80)
req.set_app_info(top.appinfo("1023079608", "sandbox0522e2394ad8813381ce7f457"))

req.fields="total_fee"
req.start_created="2015-01-01 00:00:00"
req.end_created="2015-01-20 23:59:59"
req.status="ALL_WAIT_PAY"
req.buyer_nick="zhangsan"
req.type="game_equipment"
req.ext_type="service"
req.rate_status="RATE_UNBUYER"
req.tag="time_card"
req.page_no=1
req.page_size=40
req.use_has_next=true
try:
    resp= req.getResponse("610241194d4ef46342d1f6fd96f48c3acd22c0657a42d8f182558410")
    print(resp)
except Exception,e:
    print(e)
