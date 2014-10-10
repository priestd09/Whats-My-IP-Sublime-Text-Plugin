#WhatsMyIP
#Retrieves and Displays the External IP Address and places it at the cursor position
#Author: David Priest

import sublime, sublime_plugin
import urllib2,re

class WhatsMyIpCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		messages = []
		url = "http://checkip.dyndns.com"
		try:
			request = urllib2.Request(url, headers = { "User-Agent" : "Sublime WhatsMyIP" })
			response = urllib2.urlopen(request, timeout = 3)


			# parse ip address
			message = re.search('([0-9]{1,3}\.){3}[0-9]{1,3}',response.read())

			# print message.group()

			#get cursor position
			pos = self.view.sel()[0].begin()
			#for each char display char for while advancing cursor position
			for pos in self.view.sel():
				self.view.insert(edit, pos.begin(), message.group())
			
		except Exception as (e):
			message = "Problem retrieving the IP. "
			messages.append(message)
		return messages

