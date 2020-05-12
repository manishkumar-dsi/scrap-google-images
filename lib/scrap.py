from bs4 import BeautifulSoup
import requests
import urllib.parse
import base64

import PIL
from PIL import Image
from io import BytesIO

import random
import string

import urllib.request
import os

class Scrap:
	def __init__(self, resize):
		self.resize = resize

	def randomStringDigits(self, stringLength=6):
		"""Generate a random string of letters and digits """
		lettersAndDigits = string.ascii_letters + string.digits
		return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

	def resize_img(self, orig_path, new_path):
		try:
			img = Image.open(orig_path)
			img = img.resize((self.resize, self.resize), PIL.Image.ANTIALIAS)
			img.save(new_path)
		except Exception as e:
			raise
		else:
			return
		finally:
			return

	def gen_dir(self, dir_name, sub_dir_name = 'orig'):
		path_name = dir_name + '/' + sub_dir_name + '/'

		if not os.path.exists(path_name):
			os.makedirs(path_name)
		

	def start(self, url, base_dir, keyword):
		#url = "https://www.google.com/search?q=ladyfinger+in+plate&tbm=isch&ved=2ahUKEwjxioKQ7JXpAhVXhksFHXqAC5kQ2-cCegQIABAA&oq=ladyfinger+in+plate&gs_lcp=CgNpbWcQA1CgngFY_6UBYM2oAWgAcAB4AIABXIgBtAOSAQE1mAEAoAEBqgELZ3dzLXdpei1pbWc&sclient=img&ei=ucCtXrHKJteMrtoP-oCuyAk&bih=637&biw=1351&hl=en-GB"
		page = requests.get(url)
		soup = BeautifulSoup(page.text, 'html.parser')
		
		veg_path = base_dir + '/' + keyword + '/'
		orig_veg_dir =  veg_path + 'orig/' + keyword + '_'
		resized_veg_dir =  veg_path + str(self.resize) + '/' + keyword + '_'

		images = soup.find_all('img')

		# make dir
		self.gen_dir(veg_path, str(self.resize))

		# print(images)
		for i in range(len(images)):
			src = images[i].get('src')
			#print(src)
			if src and ("gstatic.com" in src):
				print(src)
				img_name = self.randomStringDigits(6) + ".jpg"
				orig_img_path = orig_veg_dir + img_name
				urllib.request.urlretrieve(src, orig_img_path)

				resized_img_path = resized_veg_dir + img_name
				self.resize_img(orig_img_path, resized_img_path)
