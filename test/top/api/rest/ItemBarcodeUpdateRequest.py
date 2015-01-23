'''
Created by auto_sdk on 2015-01-20 12:36:26
'''
from top.api.base import RestApi
class ItemBarcodeUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.isforce = None
		self.item_barcode = None
		self.item_id = None
		self.sku_barcodes = None
		self.sku_ids = None
		self.src = None

	def getapiname(self):
		return 'taobao.item.barcode.update'
