from lib.load import Load
import os

class Config(Load):
	def __init__(self):
		self.dirname = os.path.dirname(__file__)
		self.file_name = os.path.join(self.dirname, 'config.json')
		Load.__init__(self, self.file_name)
		self.data = self.__get()
		
	def __get(self):
		config = Load(self.file_name).read_file()
		return config['config']

	def get_base_url(self):
		return self.data['base_url']

	def get_download_base_dir(self):
		return os.path.join(self.dirname, self.data['download_dir'])
	
	def get_data_json_path(self):
		return os.path.join(self.dirname, self.data['data_json_path'])
