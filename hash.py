import hashlib
import sys

flag = 0

try:
	import pefile
	flag =1
except:
	pass


if __name__ == '__main__':
	argc = len(sys.argv)
	if argc != 2:
		print "python hash.py <filename>"
		sys.exit(1)
	file_name = sys.argv[1]

	with open(file_name,'rb') as f:
		strings = f.read()

	print "md5    : ",hashlib.md5(strings).hexdigest()
	print "sha1   : ",hashlib.sha1(strings).hexdigest()
	print "sha256 : ",hashlib.sha256(strings).hexdigest()

	if flag == 1:
		try:
			pe = pefile.PE(sys.argv[1])
			print "Import Hash: %s" % pe.get_imphash()
		except:
			pass
