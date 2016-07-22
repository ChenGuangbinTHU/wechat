
# -*- coding: utf-8 -*-
import hashlib
import web
import lxml
import time
import os


class WeixinInterface:

	def __init__(self):
		self.app_root = os.path.dirname(__file__)
		self.templates_root = os.path.join(self.app_root, 'templates')
		self.render = web.template.render(self.templates_root)

	def GET(self):
		
		data = web.input()
		signature=data.signature
		timestamp=data.timestamp
		nonce=data.nonce
		echostr = data.echostr
		
		token="cgb157dnfcf953" 
		
		list=[token,timestamp,nonce]
		list.sort()
		sha1=hashlib.sha1()
		map(sha1.update,list)
		hashcode=sha1.hexdigest()
		
		if hashcode == signature:
			return echostr
			
	def POST(self): 
		str_xml = web.data() 
		xml = lxml.etree.fromstring(str_xml)
		msgType = xml.find("MsgType").text 
		fromUser=xml.find("FromUserName").text 
		toUser=xml.find("ToUserName").text 
		content=xml.find("Content").text
		return self.render.reply_text(fromUser,toUser,int(time.time()), content)
		# if msgType == 'text':
			# content=xml.find("Content").text
			# return self.render.reply_text(fromUser,toUser,int(time.time()), content)
		# elif msgType == 'image':
			# content=xml.find("Content").text
			# return self.render.reply_text(fromUser,toUser,int(time.time()), content)
		# else:
			# content=xml.find("Content").text
			# return self.render.reply_text(fromUser,toUser,int(time.time()), content)
