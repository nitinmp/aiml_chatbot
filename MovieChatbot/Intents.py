from abc import ABCMeta, abstractmethod
class Intent(object):


	def __init__(self, name,englishname,params, action):
		self.name = name
		self.englishname = englishname
		self.action = action
		self.params = []
		for param in params:
			# print param['required']
			self.params += [Parameter(param)]

class Parameter():
	def __init__(self, info):
		self.name = info['name']
		self.placeholder = info['placeholder']
		self.prompts = info['prompts']
		self.defaultprompts = info['defaultprompts']        
		self.required = info['required']
		self.context = info['context']