'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class TmallItemSchemaUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.category_id = None
		self.item_id = None
		self.product_id = None
		self.xml_data = None

	def getapiname(self):
		return 'tmall.item.schema.update'
