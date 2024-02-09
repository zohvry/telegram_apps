import requests
from bs4 import BeautifulSoup as b

# هذا الكود خاص بالمطور @z0hary

def getapi():
	r = requests.session()
	phone = input("enter ur phone number : ")
	headers = {
	    'Host': 'my.telegram.org',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'x-requested-with': 'XMLHttpRequest',
	    'sec-ch-ua-mobile': '?0',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
	    'sec-ch-ua-platform': 'Android',
	    'origin': 'https://my.telegram.org',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-dest': 'empty',
	    'referer': 'https://my.telegram.org/auth',
	    'accept-language': 'en-GB,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,en-US;q=0.6',
	}
	
	data = {
	    'phone': phone,
	}
	
	response = r.post('https://my.telegram.org/auth/send_password', headers=headers, data=data)
	if 'random_hash' in response.text:
		x = response.json()
		ran = x['random_hash']
	else:
		return print('جربت كتير ريح')
	passw = input('enter ur pass : ')
	data = {
	    'phone': phone,
	    'random_hash': ran,
	    'password': passw.strip(),
	}
	response = r.post('https://my.telegram.org/auth/login', headers=headers, data=data)
	if 'true' in response.text:
		headers = {
		    'Host': 'my.telegram.org',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-platform': 'Android',
		    'upgrade-insecure-requests': '1',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
		    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		    'sec-fetch-site': 'same-origin',
		    'sec-fetch-mode': 'navigate',
		    'sec-fetch-user': '?1',
		    'sec-fetch-dest': 'document',
		    'referer': 'https://my.telegram.org/',
		    'accept-language': 'en-GB,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,en-US;q=0.6'
		}

		response = r.get('https://my.telegram.org/apps', headers=headers)
		soup = b(response.text,'html.parser')
		find_tag = soup.findAll('div',{"class":"col-md-7"})
		api_id = str(find_tag[0].find("span")).split('>')[2].split('<')[0]
		api_hash = str(find_tag[1].find("span")).split('>')[1].split('<')[0]
		print("api_id => "+api_id+"\n"+"api_hash => "+api_hash)
		
getapi()	

# هذا الكود خاص بالمطور @z0hary
