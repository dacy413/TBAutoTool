'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class InventoryQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.sc_item_codes = None
		self.sc_item_ids = None
		self.seller_nick = None
		self.store_codes = None

	def getapiname(self):
		return 'taobao.inventory.query'
