'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class WaimaiShopListRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.keywords = None
		self.page = None
		self.page_size = None
		self.status = None

	def getapiname(self):
		return 'taobao.waimai.shop.list'
