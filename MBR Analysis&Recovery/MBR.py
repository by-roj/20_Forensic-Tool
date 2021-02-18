import sys
import os

def MBRSig():	# MBR Signature Check

	filename = raw_input("File Name : ")

	data = open(filename, 'rb')
	mbr = data.read()

	sig1 = mbr[511].encode("hex")
	sig2 = mbr[510].encode("hex")

	print("\n[+] MBR Signature")
	print("[-] MBR Signature Value : 0x" + sig1 + sig2)

	sig = mbr[510:512].encode("hex")

	if sig == '55aa':
		print("[-] MBR Signature Check : Safe\n")

	else:
		print("[-] MBR Signature Check : Warn\n")

	data.close()


def MBRPT():	# MBR Partition Table Check

	filename = raw_input("File Name : ")
	
	data = open(filename, 'rb')
	mbr = data.read()

	for i in range(0, 4):
		fs = mbr[450 + (i * 16)].encode("hex")

		if fs == '00':
			break

		print("\n[+] Partition" + str(i+1) + " Information")

		#Boot Flag
		bf = mbr[446 + (i * 16)].encode("hex")
		print("[-] Boot Flag : 0x" + bf)

		if bf == '80':
			print("	[-] Boot Enable")

		else:
			print("	[-] Boot Disable")

		#CHS Start Address
		schs1 = mbr[449 + (i * 16)].encode("hex")
		schs2 = mbr[448 + (i * 16)].encode("hex")
		schs3 = mbr[447 + (i * 16)].encode("hex")
		print("[-] CHS Start Address : 0x" + schs1 + schs2 + schs3)

		#File System Type
		if fs == '01':
			type = 'FAT12'
		elif fs == '04':
			type = 'FAT16'
		elif fs == '05':
			type = 'MS_Extended'
		elif fs == '06':
			type = 'FAT16'
		elif fs == '07':
			type = 'NTFS'
		elif fs == '0b':
			type = 'FAT32'
		elif fs == '0c':
			type = 'FAT32'	
		elif fs == '0e':
			type = 'FAT16'
		elif fs == '0f':
			type = 'MS_Extended'
		elif fs == '83':
			type = 'Linux'
		elif fs == '85':
			type = 'Linux_Extended'
		elif fs == 'a5':
			type = 'FreeBSD'
		elif fs == 'a8':
			type = 'MACOSX'
		elif fs == 'ab':
			type = 'MAC_OSX_BOOT'
		elif fs == 'ee':
			type = 'EFI_GTP_DICK'

		print("[-] File System Type : " + type)	

		#CHS End Address
		echs1 = mbr[453 + (i * 16)].encode("hex")
		echs2 = mbr[452 + (i * 16)].encode("hex")
		echs3 = mbr[451 + (i * 16)].encode("hex")
		print("[-] CHS End Address : 0x" + echs1 + echs2 + echs3)

		#LBA Start Address
		lba1 = mbr[457 + (i * 16)].encode("hex")
		lba2 = mbr[456 + (i * 16)].encode("hex")
		lba3 = mbr[455 + (i * 16)].encode("hex")
		lba4 = mbr[454 + (i * 16)].encode("hex")
		print("[-] LBA Start Address : 0x" + lba1 + lba2 + lba3 + lba4)

		#Sector Count
		sc1 = mbr[461 + (i * 16)].encode("hex")
		sc2 = mbr[460 + (i * 16)].encode("hex")
		sc3 = mbr[459 + (i * 16)].encode("hex")
		sc4 = mbr[458 + (i * 16)].encode("hex")
		print("[-] Sector Count : 0x" + sc1 + sc2 + sc3 + sc4 + "\n")

	data.close()

def MBRRe():	# MBR Partition Recovery

	filename = raw_input("File Name : ")
	num = raw_input("Partition Number : ")

	with open(filename, 'rb') as data1:
		mbr = data1.read()

		num = int(num) - 1

		fs = mbr[450 + (num * 16)].encode("hex")

		lba1 = mbr[457 + (num * 16)].encode("hex")
		lba2 = mbr[456 + (num * 16)].encode("hex")
		lba3 = mbr[455 + (num * 16)].encode("hex")
		lba4 = mbr[454 + (num * 16)].encode("hex")

		val = lba1 + lba2 + lba3 + lba4
		val = int(val, 16)

		if fs == '0b' or fs == '0c':
			backup = mbr[:512 * val] + mbr[512 * (val + 6):512 * (val + 7)] + mbr[512 * (val + 1):]

		elif fs == '07':
			sc1 = mbr[461 + (num * 16)].encode("hex")
			sc2 = mbr[460 + (num * 16)].encode("hex")
			sc3 = mbr[459 + (num * 16)].encode("hex")
			sc4 = mbr[458 + (num * 16)].encode("hex")

			count = sc1 + sc2 + sc3 + sc4
			count = int(count, 16)

			backup = mbr[:512 * val] + mbr[512 * (val + count - 1):512 * (val + count)] + mbr[512 * (val + 1):]
				

	data1.close()


	with open(filename, 'wb') as data2:
		data2.write(backup)

	data2.close()
	
	print("\nPartition" + str(num + 1) + " Recovery Complete\n")

def help():
	print """
	MBR Analysis & Recovery Command help

	View MBR Signature & Check : sig
	View MBR Partition table : pt
	Recover MBR partition table : re
	View Help : help
	Clear Command Line : clear / cls
	Program Exit : exit
	"""


def com():

	if command == 'sig':
		MBRSig()
	elif command == 'pt':
		MBRPT()
	elif command == 're':
		MBRRe()
	elif command == 'help':
		help()
	elif command in ('cls', 'clear'):
		os.system('cls')
		print "\nIf you don't know any commands, Please type 'help'\n"
	elif command == 'exit':
		exit()
	elif(len(command) == 0):
		pass
	else:
		print "\nWrong Command\n"



print "\nIf you don't know any commands, Please type 'help'\n"

while(1):
	command = raw_input("Command : ")
	com()
