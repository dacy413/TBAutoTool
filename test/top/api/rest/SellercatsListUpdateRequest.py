'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class SellercatsListUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cid = None
		self.name = None
		self.pict_url = None
		self.sort_order = None

	def getapiname(self):
		return 'taobao.sellercats.list.update'
