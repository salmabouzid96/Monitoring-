"""
File name: monitor.py
Author: Salma Bouzid
		salma.bouzid@usherbrooke.ca
Date created: 30/07/2020
"""


import os
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
from string import Template
try:
	import urllib.request as urllib2
except ImportError:
	import urllib2
import platform

def check_java_exist():
	java = subprocess.Popen(["java", "-version"],
	stdout = subprocess.PIPE,
	stderr = subprocess.STDOUT)
	out, err = java.communicate()
	if err:
		print('Java is not installed, please download it and install it for proper use')
	return err
def check_java_version():
	java_version = subprocess.check_output(["java", "-version"],
			   stderr=subprocess.STDOUT)
	vers_tmp = java_version.decode('utf8').strip()
	version = vers_tmp.splitlines()[0].split()[-1].strip('"')
	version = version[2:3]
	return version


def download_install_java(packages, version, update, auth, b):
	site = "http://download.oracle.com/otn-pub/java/jdk"
	osEx = sys.platform
	if osEx.startswith("linux"):
		osEx = "linux"
		ext = "tar.gz"
	urlTemplate = Template("${site}/${version}u${update}-b${b}/${auth}/${package}-${version}u${update}-${osEx}-x${arch}.${ext}")
	fileTemplate = Template("${package}-${version}u${update}-${osEx}-x${arch}.${ext}")
	arch = platform.architecture()[0]
	arch = arch[0:2]
	for package in packages:
		d = dict(
			site = site,
			package = package,
			version = version,
			update = update,
			b = b,
			auth = auth,
			osEx = osEx, 
			arch = arch,
			ext= ext
		)
		url = urlTemplate.safe_substitute(d)
		file = fileTemplate.safe_substitute(d)
		fileName = file.split(".")[0]
		print("Downloading %s" % (url))
		opener = urllib2.build_opener()
		opener = urllib2.build_opener()
		cookie = 'Cookie'
		license = 'oraclelicense=accept-securebackup-cookie'
		opener.addheaders.append((cookie, license))
		f = opener.open(url)
		with open(file, 'wb+') as save:
			save.write(f.read())
		pathJava =  "/usr/bin/java"
		fileName = file.split(".")[0]
		pathLocal = os.getcwd()+"/"+fileName+"/bin/java"
		subprocess.Popen(["tar", "-xvf", file], stdin=PIPE,stdout=PIPE,stderr=PIPE)
		variables = ["java", "javac", "javaws"]
		for var in variables:
			print("Installing %s" % (var))
			process = subprocess.Popen(["sudo", "update-alternatives", "--install",  pathJava, var, pathLocal], 
				stdin=subprocess.PIPE,
				stdout=subprocess.PIPE,
				stderr=subprocess.PIPE)
			out, err = process.communicate()
			if not err:
				print("Done installing %s" % (var))

			
def send_email(From, Pwd, To, emailContent):
	msg = MIMEMultipart()
	msg['Subject'] = 'Java installation updates'
	msg['From'] = From
	msg['To'] = To
	body = MIMEText(emailContent)
	msg.attach(body)
	server = smtplib.SMTP(host='your_host_address_here', port='your_port_here')
	server.starttls()
	server.login(From, Pwd)
	server.sendmail(msg['From'], msg['To'], msg.as_string())

def main():
	java = check_java_exist()
	From = "Your address here "
	Pwd = "Your Pwd here"
	To = "Your recipients here" #List in case of multiple recipients
	if not java:
		version = check_java_version()
		print ("Java version installed :" + version)
		emailContent += "\n\n This email is automatically sent, please do not reply to this email"
		send_email(From, Pwd,  To, emailContent)
	else:
		"""
		Update the parameters considered in the url of the download 
		function to download and install the desired function
		"""
		packages = ["jdk"]
		b = "11"
		version = 8
		update = "131"
		auth = "d54c1d3a095b4ff2b6607d096fa80163"
		download_install_java(packages, version, update, auth, b)
		if not java:
			version = check_java_version()
			emailContent = "Java was not installed, the version that is installed now:" + version
			emailContent += "\n\n This email is automatically sent, please do not reply to this email"
			send_email(From,Pwd, To, emailContent)

if __name__=='__main__':
	main()



