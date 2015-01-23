'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class FenxiaoRefundQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_date = None
		self.page_no = None
		self.page_size = None
		self.query_seller_refund = None
		self.start_date = None

	def getapiname(self):
		return 'taobao.fenxiao.refund.query'
