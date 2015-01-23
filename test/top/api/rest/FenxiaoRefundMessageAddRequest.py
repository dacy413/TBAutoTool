'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class FenxiaoRefundMessageAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.image = None
		self.message_content = None
		self.sub_order_id = None

	def getapiname(self):
		return 'taobao.fenxiao.refund.message.add'

	def getMultipartParas(self):
		return ['image']
