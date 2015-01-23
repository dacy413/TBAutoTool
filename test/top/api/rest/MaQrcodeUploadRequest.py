'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class MaQrcodeUploadRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.ext = None
		self.image_name = None
		self.imge = None

	def getapiname(self):
		return 'taobao.ma.qrcode.upload'

	def getMultipartParas(self):
		return ['imge']
