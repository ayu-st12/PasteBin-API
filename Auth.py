import requests

API_HTTPLINK = "https://pastebin.com/api/api_post.php"
API_HTTPLINK_SESSION = "https://pastebin.com/api/api_login.php"

API_KEY = "5a2144c1456ac896a8e05970d951351c"

session_id = ""

source_code = '''
print("Hello World!")
'''

data = {'api_dev_key':API_KEY,
	'api_option':'paste',
	'api_paste_code':source_code,
	'api_paste_format':'python',
	'api_user_key':'avardhan',
	'api_paste_name':'Vardhan',
	'api_paste_expire_date':'10M',
	'api_paste_private':'0'
	}

data_session = {'api_dev_key':API_KEY,
	'api_user_name':'avardhan',
	'api_option':'paste',
	'api_user_password':'sucess@1'
	}

data_trnd = {'api_dev_key':API_KEY}

data_list = {'api_dev_key':API_KEY,
	'api_option':'paste',
	'api_user_name':'avardhan',
	'api_user_password':'sucess@1',
	'api_user_key': session_id,
	'api_results_limit':'10'
	}

def AuthenticateDev():
	r = requests.post(url = API_HTTPLINK, data = data)
	pastebin_url = r.text
	return pastebin_url

def CreateOne():
	r = requests.post(url = API_HTTPLINK, data = data)
	pastebin_url = r.text
	return pastebin_url

def getSession():
	r = requests.post(url = API_HTTPLINK_SESSION, data = data_session)
	session_id = r.text
	return;

def getPasteList():
	getSession()
	r1 = requests.post(url = API_HTTPLINK, data = data_list)
	res_id = r1
	return res_id

def getTrends():
	r1 = requests.post(url = API_HTTPLINK, data = data_trnd)
	res_id = r1
	return res_id
