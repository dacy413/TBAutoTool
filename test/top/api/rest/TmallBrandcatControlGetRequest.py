'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class TmallBrandcatControlGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)

	def getapiname(self):
		return 'tmall.brandcat.control.get'
