'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class ItemJointImgRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.id = None
		self.is_major = None
		self.num_iid = None
		self.pic_path = None
		self.position = None

	def getapiname(self):
		return 'taobao.item.joint.img'
