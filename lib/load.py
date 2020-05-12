import json

class Load:
	def __init__(self, file_name):
		self.file_name = file_name

	def read_file(self):
		try:
			fp = open(self.file_name)
		except Exception as e:
			print(e)
			raise
		else:
			# load data and return
			return json.load(fp)
		finally:
			fp.close()