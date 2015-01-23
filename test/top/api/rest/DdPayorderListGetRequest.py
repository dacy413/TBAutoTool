'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class DdPayorderListGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.ends = None
		self.order_no = None
		self.order_type = None
		self.pay_status = None
		self.pn = None
		self.ps = None
		self.show = None
		self.starts = None
		self.store_id = None

	def getapiname(self):
		return 'taobao.dd.payorder.list.get'
