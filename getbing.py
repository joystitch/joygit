#! /usr/bin/python3

import urllib.request
import re
import time

def main():
	hostname = "http://cn.bing.com/HPImageArchive.aspx?idx=0&n=1"
	req = urllib.request.Request(hostname)
	webpage = urllib.request.urlopen(req)
	content = str(webpage.read())
	url_tail = re.search(r'<url>[^\s]*</url>',content) #[^\s]表示匹配非空字符,*表示匹配前一个字符0次或多次，这里[^\s]* 表示匹配非空字符多次,'r'是防止字符转义的 如果路径中出现'\t'的话 不加r的话\t就会被转义 而加了'r'之后'\t'就能保留原有的样子.
	url = 'http://cn.bing.com' + str(url_tail.group())[5:-6] #group用户提取出正则表达式中想要的字段
	print(url)
	pic_file_name = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	print(url[-4:])
	urllib.request.urlretrieve(url,"/home/joy/Pictures/" + pic_file_name + url[-4:])	

if __name__ == '__main__':
	main()
