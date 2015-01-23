'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class SubuserDutyAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.duty_level = None
		self.duty_name = None
		self.user_nick = None

	def getapiname(self):
		return 'taobao.subuser.duty.add'
