'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class VideoAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cover_url = None
		self.description = None
		self.tags = None
		self.title = None
		self.upload_id = None
		self.uploader_id = None
		self.video_app_key = None

	def getapiname(self):
		return 'taobao.video.add'
