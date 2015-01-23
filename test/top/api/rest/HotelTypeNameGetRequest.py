'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class HotelTypeNameGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.hid = None
		self.name = None

	def getapiname(self):
		return 'taobao.hotel.type.name.get'
