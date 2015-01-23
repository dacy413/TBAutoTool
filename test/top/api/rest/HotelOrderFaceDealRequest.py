'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class HotelOrderFaceDealRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.oid = None
		self.oper_type = None
		self.reason_text = None
		self.reason_type = None

	def getapiname(self):
		return 'taobao.hotel.order.face.deal'
