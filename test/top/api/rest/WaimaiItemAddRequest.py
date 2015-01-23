'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class WaimaiItemAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.auctiondesc = None
		self.auctionstatus = None
		self.categoryid = None
		self.categoryids = None
		self.goodsno = None
		self.limitbuy = None
		self.oriprice = None
		self.picurl = None
		self.price = None
		self.quantity = None
		self.rule_id = None
		self.shopids = None
		self.sku_info = None
		self.title = None
		self.viceimage = None

	def getapiname(self):
		return 'taobao.waimai.item.add'
