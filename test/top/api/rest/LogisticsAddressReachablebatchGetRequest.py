'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class LogisticsAddressReachablebatchGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.address_list = None

	def getapiname(self):
		return 'taobao.logistics.address.reachablebatch.get'
