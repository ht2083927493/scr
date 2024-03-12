from time import strftime
import os
import sys
import requests
from time import sleep
from datetime import datetime, timedelta
import requests
import os
try:
  from faker import Faker
  import requests
  from colorama import Fore, Style
  import re
  import pystyle
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system('pip install requests && pip install bs4 && pip install pystyle')
  print('__Vui Lòng Chạy Lại Tool__')
# màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
tim = '\033[1;39m'
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb = "\033[1;37m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
os.system("cls" if os.name == "nt" else "clear")

# đánh dấu bản quyền
ndp_tool = "\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"

ip = requests.get("https://api.ipgeolocation.io/getip").json()
def banner():
    banner = f"""


\033[1;34m ╭╮╱╭┳━━┳━━━┳╮╱╭╮╱╭━━━━┳━━━┳━━━┳╮
\033[1;37m ┃┃╱┃┣┫┣┫╭━━┫┃╱┃┃╱┃╭╮╭╮┃╭━╮┃╭━╮┃┃
\033[1;34m ┃╰━╯┃┃┃┃╰━━┫┃╱┃┃╱╰╯┃┃╰┫┃╱┃┃┃╱┃┃┃
\033[1;37m ┃╭━╮┃┃┃┃╭━━┫┃╱┃┣━━╮┃┃╱┃┃╱┃┃┃╱┃┃┃╱╭╮
\033[1;34m ┃┃╱┃┣┫┣┫╰━━┫╰━╯┣━━╯┃┃╱┃╰━╯┃╰━╯┃╰━╯┃
\033[1;37m ╰╯╱╰┻━━┻━━━┻━━━╯╱╱╱╰╯╱╰━━━┻━━━┻━━━╯
\033[1;34m 𝐀𝐃𝐌𝐈𝐍_𝐇𝐈𝐄𝐔_𝐓𝐎𝐎𝐋
\033[1;31m────────────────────────────────────────────────────────────
\033[1;31m────────────────────────────────────────────────────────────
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
\033[1;39m┌────────────────────────💚 HIẾU TOOL💚────────────────────────┐
\033[1;32m║   \033[1;39mPYTHON VERSION\033[1;32m     :  5.0                                  \033[1;32m║
\033[1;32m║   \033[1;39mZALO               :  84939271874                          \033[1;32m║
\033[1;32m║   \033[1;39mGROP_zalo          :  https://zalo.me/g/wfakde942          \033[1;32m║
\033[1;32m║   \033[1;39mYOUTUBER           :  HIẾU TOOL                            \033[1;32m║
\033[1;32m║   \033[1;39mYOTUBE_LINK        :  https://www.youtube.com/@hieutool248 \033[1;32m║
\033[1;39m└──────────────────────────────────────────────────────────────┘
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
\033[1;31m────────────────────────────────────────────────────────────
"""

    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.00125)
banner()


print(f"\033[1;37m\033[1;33mip của bạn là: {ip['ip']}  \033[1;37m")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Trao Đổi Sub  \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mTool TDS FB FULL JOD")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mTool TDS FB VIP")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3\033[1;31m] \033[1;32mTool \033[1;31m[\033[1;33m 1 page \033[1;31m]")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3.1\033[1;31m] \033[1;32mTool \033[1;31m[\033[1;33m Đa page\033[1;31m]")

print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m4\033[1;31m] \033[1;32mTool TDS IG \033[1;31m[\033[1;33mV1\033[1;31m] ")

print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m5\033[1;31m] \033[1;32mTool TDS TikTok & TDS TIKTOK NOW")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═══════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Tương Tác Chéo  \033[1;37m║")
print("\033[1;37m╚═══════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m6\033[1;31m] \033[1;32mTool TTC TikTok [chưa fix] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m7\033[1;31m] \033[1;32mTool TTC Pro5 ")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Tiện Ích      \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m8\033[1;31m] \033[1;32mTool Đào Mail ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m9\033[1;31m] \033[1;32mTool Tạo Thẻ Thanh Toán ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m10\033[1;31m] \033[1;32mTool Check Valid")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m11\033[1;31m] \033[1;32mTool LOC PROXY ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m12\033[1;31m] \033[1;32mtool lọc proxy new max speed\033[1;31m『\033[1;33mNEW \033[1;31m』 ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m13\033[1;31m] \033[1;32mTool Get Cookie Pro5 Facebook")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m14\033[1;31m] \033[1;32mTool Nuôi Acc FB")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool PROFILE       \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m15\033[1;31m] \033[1;32mTool SHARE Facebook")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m16\033[1;31m] \033[1;32mTool Reg Page Pro5 \033[1;31m[\033[1;33mV2\033[1;31m]")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m16.1\033[1;31m] \033[1;32mTool Reg Page Pro5 + Up Avatar \033[1;31m[\033[1;33mV3\033[1;31m]")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m17\033[1;31m] \033[1;32mTOOL TĂNG SHARE AO BẰNG TOKEN")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m18\033[1;31m] \033[1;32mTool Buff View Story Max Speed Pro5 ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m18.1\033[1;31m] \033[1;32mTOOL CHUYỂN QUYỀN QUẢN TRỊ VIÊN PRO5")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool SPAM SMS      \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m19\033[1;31m] \033[1;32mtool spam sms\033[1;31m[\033[1;33mV5\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m20\033[1;31m] \033[1;32mTool SPAM SMS \033[1;31m[\033[1;33mV6\033[1;31m] ")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔══════════════╗")
print("\033[1;37m║ \033[1;33mTool Golike  \033[1;37m║")
print("\033[1;37m╚══════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m21\033[1;31m] \033[1;32mTool Golike Tiktok ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m22\033[1;31m] \033[1;32mTool Golike Tiktok\033[1;31m[\033[1;33mV2\033[1;31m] [Delay_5s]")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m22.1\033[1;31m] \033[1;32mTool Golike Tiktok\033[1;31m[\033[1;33mV3\033[1;31m] [Delay_0s]")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔══════════════╗")
print("\033[1;37m║ \033[1;33mTool zefoy   \033[1;37m║")
print("\033[1;37m╚══════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m23\033[1;31m] \033[1;32mTool zefoy \033[1;31m[\033[1;33mBuff view TikTok New\033[1;31m]")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mLưu ý tool chỉ chạy khi web zefoy tắt tường lửa")
print("\033[1;31m────────────────────────────────────────────────────────────")

print("\033[1;37m╔═══════════╗")
print("\033[1;37m║\033[1;33mhỗ trợ Tool\033[1;37m║")
print("\033[1;37m╚═══════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m101\033[1;31m] \033[1;32mĐể support qua zalo ngay")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m102\033[1;31m] \033[1;32mĐể vào nhóm zalo cập nhật tool")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m103\033[1;31m] \033[1;32mĐể vào kênh yotube")

print("\033[1;31m────────────────────────────────────────────────────────────")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m00\033[1;31m] \033[1;32mThoát Tool")
print("\033[1;31m────────────────────────────────────────────────────────────")

chon = float(input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;37m: \033[1;33m'))
#tool tds
try:
	if chon == 1 :
		response = requests.get('https://raw.githubusercontent.com/ht2083927493/tool/main/1.TDS%20FB%20FULL%20JOD.py')
		exec(response.text)
	elif chon == 2:
		response = requests.get('https://raw.githubusercontent.com/ht2083927493/tool/main/2.TDS%20FB%20VIP.py')
		exec(response.text)
	elif chon == 3 :
		response = requests.get('https://raw.githubusercontent.com/ht2083927493/tool/main/3.TDS%20Pro5.py')
		exec(response.text) 
	elif chon == 3.1 :
		response = requests.get('https://hieutoolsuocecodepython.000webhostapp.com/3.1tdspro5_da_page_99919824.html')
		exec(response.text)
	elif chon == 4 :
		response = requests.get('https://raw.githubusercontent.com/ht2083927493/tool/main/4.TDS%20IG.py')
		exec(response.text)
	elif chon == 5 : 
		response = requests.get('https://raw.githubusercontent.com/ht2083927493/tool/main/5.TDS%20TikTok.py')
		exec(response.text)
	#tool ttc
	elif chon == 6 :
		response = requests.get('')
		exec(response.text)
	elif chon == 7 :
		response = requests.get('https://raw.githubusercontent.com/ht2083927493/tool/main/7.TTC%20Pro5.py')
		exec(response.text)
	#tool công cụ 
	elif chon == 8 :
		response = requests.get('https://raw.githubusercontent.com/ht2083927493/tool/main/8.%C4%90%C3%A0o%20Mail.py')
		exec(response.text)
	elif chon == 9 :
		response = requests.get('https://raw.githubusercontent.com/ht2083927493/tool/main/9.T%E1%BA%A1o%20Th%E1%BA%BB%20Thanh%20To%C3%A1n.py')
		exec(response.text)
	elif chon == 10 :
		response = requests.get('https://raw.githubusercontent.com/ht2083927493/tool/main/10.Check%20Valid.py')
		exec(response.text)
	elif chon == 11 :
		response = requests.get('https://hieutoolsuocecodepython.000webhostapp.com/11.LOC%20PROXY.html')
		exec(response.text)
	elif chon == 12 :
		response = requests.get('https://hieutoolsuocecodepython.000webhostapp.com/12.locprxnewHT.html')
		exec(response.text)
	elif chon == 13 :
		response = requests.get('https://hieutoolsuocecodepython.000webhostapp.com/13.Get%20Cookie%20Pro5%20Facebook.html')
		exec(response.text)
	elif chon == 14:
		response = requests.get('https://hieutoolsuocecodepython.000webhostapp.com/14.nuoiFb736423.html')
		exec(response.text)
	elif chon == 15 :
		response = requests.get('https://hieutoolsuocecodepython.000webhostapp.com/15.sharefb.html')
		exec(response.text)
	elif chon == 16 :
		response = requests.get('https://hieutoolsuocecodepython.000webhostapp.com/16.Reg%20Page%20Pro5.html')
		exec(response.text)
	elif chon == 16.1:
		response = requests.get('https://hieutoolsuocecodepython.000webhostapp.com/16.1.reg_pro5.HT.33668899.php')
		exec(response.text)

	elif chon == 17 :
		response = requests.get('https://hieutoolsuocecodepython.000webhostapp.com/17.T%C4%82NG%20SHARE%20TOKEN.html')
		exec(response.text)
	elif chon == 18 :
		response = requests.get('https://hieutoolsuocecodepython.000webhostapp.com/18.Buff%20View%20Story%20Max%20Speed%20Pro5.html')
		exec(response.text)
	elif chon == 18.1 :
		response = requests.get('https://hieutoolsuocecodepython.000webhostapp.com/18.1.TOOL%20CHUY%E1%BB%82N%20QUY%E1%BB%80N%20QU%E1%BA%A2N%20TR%E1%BB%8A%20VI%C3%8AN%20PRO5.html')
		exec(response.text)
	elif chon == 19 :
		response = requests.get('https://hieutoolsuocecodepython.000webhostapp.com/19.spamv5.html')
		exec(response.text)
	elif chon == 20 :
		response = requests.get('https://hieutoolsuocecodepython.000webhostapp.com/20.spamv6.html')
		exec(response.text)
	elif chon == 21 :
		response = requests.get('https://raw.githubusercontent.com/ht2083927493/tool/main/golikev1.py')
		exec(response.text)
	elif chon == 22 :
		response = requests.get('https://raw.githubusercontent.com/ht2083927493/tool/main/glv3.py')
		exec(response.text)
	elif chon == 22.1 :
		response = requests.get('https://raw.githubusercontent.com/ht2083927493/tool/main/glv3.py')
		exec(response.text)
	elif chon == 23 :
		response = requests.get('https://raw.githubusercontent.com/ht2083927493/tool/main/exit.py')
		exec(response.text)
	# elif chon == 12 :
	# 	response = requests.get('https://hieutoolsuocecodepython.000webhostapp.com/12.buff%20view,tym,..%20tiktok.html')
	# 	exec(response.text)
	elif chon == 00 :
		response = requests.get('https://hieutoolsuocecodepython.000webhostapp.com/00.exit.html')
		exec(response.text)
	elif chon == 101:
		os.system("termux-open-url https://zalo.me/84939271874")
	elif chon == 102:
		os.system("termux-open-url https://zalo.me/g/wfakde942")
	elif chon == 103:
		os.system("termux-open-url https://www.youtube.com/@hieutool248")
	else :
		exit()
except:
	print("\033[1;31m"'''Kiểm Tra kết nối mạng hoặc sever chứa tool đang có lỗi''') 