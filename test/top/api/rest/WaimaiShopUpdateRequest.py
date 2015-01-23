'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class WaimaiShopUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.address = None
		self.name = None
		self.phone = None
		self.pic_url = None
		self.posx = None
		self.posy = None
		self.shopid = None
		self.shopoutid = None

	def getapiname(self):
		return 'taobao.waimai.shop.update'
