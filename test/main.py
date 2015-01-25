# # -*- coding: utf-8 -*-

# # import sys

# # sys.path.append('/home/dacy/workspace/TBAutoTool/test/top/api')

# import top.api
# req=top.api.TradesSoldGetRequest()
# req.set_app_info(top.appinfo("1023079608", "sandbox0522e2394ad8813381ce7f457"))

# req.fields="total_fee"
# req.start_created="2000-01-01 00:00:00"
# req.end_created="2000-01-01 23:59:59"
# req.status="ALL_WAIT_PAY"
# req.buyer_nick="zhangsan"
# req.type="game_equipment"
# req.ext_type="service"
# req.rate_status="RATE_UNBUYER"
# req.tag="time_card"
# req.page_no=1
# req.page_size=40
# req.use_has_next=True
# try:
#     resp= req.getResponse("610241194d4ef46342d1f6fd96f48c3acd22c0657a42d8f182558410")
#     print(resp)
# except Exception,e:
#     print(e)


# -*- coding: utf-8 -*-
import top.api

#=====================================get all of trades===========================#
req=top.api.TradesSoldGetRequest("gw.api.tbsandbox.com")
req.set_app_info(top.appinfo("1023079608", "sandbox0522e2394ad8813381ce7f457"))

req.fields="seller_nick,buyer_nick,title,type,created,sid,tid,seller_rate,buyer_rate,\
                    status,payment,discount_fee,adjust_fee,post_fee,total_fee,pay_time,\
                    end_time,modified,consign_time,buyer_obtain_point_fee,point_fee,\
                    real_point_fee,received_payment,commission_fee,pic_path,num_iid,\
                    num_iid,num,price,cod_fee,cod_status,shipping_type,receiver_name,\
                    receiver_state,receiver_city,receiver_district,receiver_address,\
                    receiver_zip,receiver_mobile,receiver_phone,orders.title,orders.pic_path,\
                    orders.price,orders.num,orders.iid,orders.num_iid,orders.sku_id,orders.refund_status,\
                    orders.status,orders.oid,orders.total_fee,orders.payment,orders.discount_fee,orders.adjust_fee,\
                    orders.sku_properties_name,orders.item_meal_name,orders.buyer_rate,orders.seller_rate,\
                    orders.outer_iid,orders.outer_sku_id,orders.refund_id,orders.seller_type,buyer_message"
try:
    import pdb;pdb.set_trace()
    resp = req.getResponse("6101f21f5df655ca131999e3b72ef19b085defe92c85d213651880146")
    print("====>>",resp)
    # req=top.api.TradeFullinfoGetRequest("gw.api.tbsandbox.com",80)
    # tid = resp['trades_sold_get_response']['trades']['trade'][0]['tid'];
    # req.fields = "status,buyer_message"
    # req.tid = tid
    # import pdb;pdb.set_trace()
    # resp= req.getResponse("6101801ef126a76ee72479d320b397e3e91ca2072efe04e3651880146")
    # print(resp)

except Exception as e:
    print(e)

#=====================================get full info of one trade===========================#
req1=top.api.TradeFullinfoGetRequest("gw.api.tbsandbox.com")
req1.set_app_info(top.appinfo("1023079608", "sandbox0522e2394ad8813381ce7f457"))

tid = resp['trades_sold_get_response']['trades']['trade'][0]['tid'];
req1.fields="status,buyer_message,tid"
req1.tid = tid
try:
    resp1= req1.getResponse("6101f21f5df655ca131999e3b72ef19b085defe92c85d213651880146")
    print(resp1)
except Exception as e:
    print(e)

#=====================================send goods use tid===========================#
req2 = top.api.LogisticsDummySendRequest("gw.api.tbsandbox.com")
req2.set_app_info(top.appinfo("1023079608", "sandbox0522e2394ad8813381ce7f457"))

req2.tid=tid
import pdb;pdb.set_trace();
try:
    resp2= req.getResponse("6101f21f5df655ca131999e3b72ef19b085defe92c85d213651880146")
    print("==================>>",resp2)
except Exception as e:
    print(e)

#=====================================get all of trades===========================#
req=top.api.TradesSoldGetRequest("gw.api.tbsandbox.com")
req.set_app_info(top.appinfo("1023079608", "sandbox0522e2394ad8813381ce7f457"))

req.fields="seller_nick,buyer_nick,title,type,created,sid,tid,seller_rate,buyer_rate,\
                    status,payment,discount_fee,adjust_fee,post_fee,total_fee,pay_time,\
                    end_time,modified,consign_time,buyer_obtain_point_fee,point_fee,\
                    real_point_fee,received_payment,commission_fee,pic_path,num_iid,\
                    num_iid,num,price,cod_fee,cod_status,shipping_type,receiver_name,\
                    receiver_state,receiver_city,receiver_district,receiver_address,\
                    receiver_zip,receiver_mobile,receiver_phone,orders.title,orders.pic_path,\
                    orders.price,orders.num,orders.iid,orders.num_iid,orders.sku_id,orders.refund_status,\
                    orders.status,orders.oid,orders.total_fee,orders.payment,orders.discount_fee,orders.adjust_fee,\
                    orders.sku_properties_name,orders.item_meal_name,orders.buyer_rate,orders.seller_rate,\
                    orders.outer_iid,orders.outer_sku_id,orders.refund_id,orders.seller_type,buyer_message"
req.status="WAIT_SELLER_SEND_GOODS"
try:
    # import pdb;pdb.set_trace()
    resp= req.getResponse("6101f21f5df655ca131999e3b72ef19b085defe92c85d213651880146")
    print("====>>",resp)

    # req=top.api.TradeFullinfoGetRequest("gw.api.tbsandbox.com",80)
    # tid = resp['trades_sold_get_response']['trades']['trade'][0]['tid'];
    # req.fields = "status,buyer_message"
    # req.tid = tid
    # import pdb;pdb.set_trace()
    # resp= req.getResponse("6101801ef126a76ee72479d320b397e3e91ca2072efe04e3651880146")
    # print(resp)

except Exception as e:
    print(e)
