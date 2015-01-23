'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class FenxiaoDiscountAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.discount_name = None
		self.discount_types = None
		self.discount_values = None
		self.target_ids = None
		self.target_types = None

	def getapiname(self):
		return 'taobao.fenxiao.discount.add'
