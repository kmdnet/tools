#from pymisp import PyMISP
import pymisp


import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

MISP_URL = 'https://localhost'
MISP_KEY = ''

ip_list = ['192.168.56.100', '192.168.56.101','192.168.56.102']

class AutoMisp():
	def __init__(self):
		self.misp =  pymisp.ExpandedPyMISP(MISP_URL, MISP_KEY, False)

	def create_event(self):
		event = pymisp.MISPEvent()
		
		event.info = 'test_event'
		event.threat_level_id = 3
		event.distribution = 2
		event.analysis = 1
		event.add_attribute('ip-src', ip_list, comment='hogehoge')
		event.add_tag('test-dayo')

		event.publish()
		res = self.misp.add_event(event)
		#print(res)
		

def main():

	am = AutoMisp()
	am.create_event()

if __name__ == '__main__':
	main()

