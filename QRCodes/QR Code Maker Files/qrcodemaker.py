def Qrcode():
	the_url = input("Enter URL: ")
	file_name = input("Enter File Name: ")
	
	import pyqrcode
	url = pyqrcode.create(the_url)
	url.svg(file_name + '.svg', scale=8)
	#print(url.terminal(quiet_zone=1))
	end_g = input("Press C to create another QR Code or Q to Quit: ")
	end_g_1 = end_g.upper()
	if end_g_1 == "C":
		Qrcode()
	elif end_g_1 == "Q":
		Quit()

Qrcode()
	

	
