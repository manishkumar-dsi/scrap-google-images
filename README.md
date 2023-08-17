# Scrap google images
A small python based library for scrapping Google images for different search variances. This is a command line tool. It will scrap the image and resize it based on the parameter passed to the command line. If there is no parameter passed then by default it will resize the image to 128x128 px.

# How to search
Add multiple parameters in data.json and this library will search and download data as per the configuration. See the data.json example.

This JSON has the following keys:
- search: This is an array of JSON and it contains the search keyword with some variance 
  - keyword: What do you want to search
  - variance: What variance do you want to put in the search? This could be color, size, etc. This is an array.
- post_varience: This will add extra parameters to the search keyword. This will be added after the search keyword
- pre_varience: Same as post_varience but parameters will be added before the search keyword.

# How to configure the download directory
This tool is very configurable. 
You can configure:
- Image download directory
- data.json path

This can be configured from config.json. 
Path for this file: **lib > config.py**
