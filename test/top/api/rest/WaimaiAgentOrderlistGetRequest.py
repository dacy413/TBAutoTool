'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class WaimaiAgentOrderlistGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.order_status = None
		self.page_no = None
		self.page_size = None
		self.shop_id = None
		self.start_time = None

	def getapiname(self):
		return 'taobao.waimai.agent.orderlist.get'
