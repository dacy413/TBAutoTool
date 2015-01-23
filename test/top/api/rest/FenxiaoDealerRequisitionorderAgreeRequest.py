'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class FenxiaoDealerRequisitionorderAgreeRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.dealer_order_id = None

	def getapiname(self):
		return 'taobao.fenxiao.dealer.requisitionorder.agree'
