'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class DdTakeoutExportRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.page_no = None
		self.page_size = None

	def getapiname(self):
		return 'taobao.dd.takeout.export'
