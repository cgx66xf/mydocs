import requests
import re
from urllib.parse import urlparse
from urllib.parse import urljoin 

url= 'https://docs.python.org/3/library/re.html'


def request_page(url):
	response= requests.get(url)
	web_source= response.text
	print("Requested page:",url)
	return web_source

web_source= request_page(url)

def find_href():
	pattern= re.compile(r'<a\shref="([^"]+)"')
	matches= pattern.finditer(web_source)
	match_list= list()
	for match in matches:
		match=(match.group(1))
		match_list.append(match)
	return match_list

match_list= find_href()

dotdot= list()
external= list()
current_dir= list()
def make_list_url():
	#print(match_list)
	for i in match_list:				
		if (i[0:2]=='..'):
			dotdot.append(urljoin(url, i))
			print(i,"************",dotdot)
			
			  			


		elif (i[0:4]=='http' or i[0:5]=='https'):
			#print("it starts with http/https",i)
			pass

		elif (i[0]=='/'):
			print("wtf"* 100)

		else:
			#print("the url is in the current directory",i)
			current_dir.append(urljoin(url, i))
			print(i,"----------",current_dir)
		
make_list_url()

def get_the_new_urls():
	pass





	
	

