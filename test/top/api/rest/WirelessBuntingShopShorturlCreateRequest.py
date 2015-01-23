'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class WirelessBuntingShopShorturlCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.shop_id = None

	def getapiname(self):
		return 'taobao.wireless.bunting.shop.shorturl.create'
