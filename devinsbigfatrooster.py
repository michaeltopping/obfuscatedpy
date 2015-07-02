import sys
import subprocess
import time
import os
ii=0
length = 0
while 1:
	length += 1
	f = open("ssdfsdfsdfwerwerwersdfsdfsdxcvxvxcvxcvsdfsdfsdfsdfs.sh", "w")
	f.write("#!/bin/sh\n")
	rows, columns = os.popen('stty size', 'r').read().split()
	if length > int(columns):
		if length == int(columns)+2:
			os.remove('ssdfsdfsdfwerwerwersdfsdfsdxcvxvxcvxcvsdfsdfsdfsdfs.sh')
			exit()
		command = "printf "+' "\e[8;2;'+str(length)+';t" \n'
	else: 
		command = "printf "+' "\e[8;2;'+columns+';t" \n'
	f.write(command)
	f.close()
	os.chmod('./ssdfsdfsdfwerwerwersdfsdfsdxcvxvxcvxcvsdfsdfsdfsdfs.sh', 0777)
	subprocess.call(['./ssdfsdfsdfwerwerwersdfsdfsdxcvxvxcvxcvsdfsdfsdfsdfs.sh'])
	sys.stdout.write("\r8"+"="*(length-2)+"D")
	sys.stdout.flush()
	time.sleep(0.1)
