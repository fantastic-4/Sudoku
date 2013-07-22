import os
class Configfile:
	'''doc string for Config_file'''
	def __init__(self, path, name):
		self.name = name
		self.path = path
	
	def ensure_dir(self,f):
		''' This method create new dir if this does not exit'''
		d = os.path.dirname(f)
		if not os.path.exists(d):
			os.makedirs(d)