#! /usr/bin/python3

import urllib.request
import xml.etree.ElementTree as ET
import time

def main():
	req = urllib.request.Request("http://cn.bing.com/HPImageArchive.aspx?idx=0&n=1")
	webpage = urllib.request.urlopen(req)
	root = ET.fromstring(webpage.read())#由字符串导入xml数据,返回的是xml的根节点
	#print(root)	
	url = "https://cn.bing.com" + root.find('image').find('url').text
	print(url)
	pic_file_name = time.strftime('%Y-%m-%d',time.localtime(time.time())) + \
	 root.find('image').find('copyright').text   	
	#print(pic_file_name)
	urllib.request.urlretrieve(url , "/home/joy/Pictures/" + pic_file_name + url[-4:]) #url表示下载的路径,pic_file_name表示存储的位置名字
	
	
	

if __name__ == '__main__':
	main()

