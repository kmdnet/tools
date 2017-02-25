import requests
import hashlib
import sys


def main():
	argc = len(sys.argv)
	if argc != 2:
		print "python vt.py <filename>"
		sys.exit(1)
	
	file_name = sys.argv[1]
	with open(file_name,'rb') as f:
		strings = f.read()

	sha256 = hashlib.sha256(strings).hexdigest()

	# Your API Key add here :)
	params = {'apikey' : 'Your API Key', 'resource' : sha256 }
	headers = {
	"Accept-Encoding": "gzip, deflate",
	"User-Agent" : "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1)Gecko/2008071615Fedora/3.0.1-1.fc9 Firefox/3.0.1"
	}
	
	response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params, headers=headers)

	json_response = response.json()
	print "\n\n",json_response


if __name__ == '__main__':
	main()
