import os
from lib.load import Load
from lib.config import Config
from lib.scrap import Scrap

class Data(Load):
	def __init__(self):
		self.file_name = Config().get_data_json_path()
		Load.__init__(self, self.file_name)
		self.data = self.__get()
		self.base_url = Config().get_base_url()
		self.download_base_dir = Config().get_download_base_dir()
		
	def __get(self):
		return Load(self.file_name).read_file()

	def gen(self, img_size=256):
		search_list = self.data['search']
		pre_varience = self.data['pre_varience']
		post_varience = self.data['post_varience']
		
		# make scrap object
		obj = Scrap(img_size)

		for search in search_list:
			temp_pre_var = []
			temp_post_var = []

			keyword_name = search["keyword"]
			keyword = [keyword_name]
			
			temp_pre_var = pre_varience + search["varience"]
			temp_pre_var = [(i + ' ' + keyword_name).replace(' ', '+') for i in temp_pre_var]
			temp_post_var = [(keyword_name + ' ' + i).replace(' ', '+') for i in post_varience]
			
			variences = temp_pre_var + temp_post_var
			
			print(variences)
			
			obj.gen_dir(self.download_base_dir + '/' +keyword_name)
			
			for item in variences:
				url = self.base_url + self.download_base_dir + '/' + item + '&tbm=isch'
				obj.start(url, self.download_base_dir, keyword_name)