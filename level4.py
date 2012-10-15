#coding: utf-8

import urllib2
import Cookie

def main():
	url = 'http://hughes.sieve.com.br:9090/level4/'
	user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/536.26.14 (KHTML, like Gecko) Version/6.0.1 Safari/536.26.14'
	
	req = urllib2.Request(url)
	req.add_header('User-Agent', user_agent)
	req.add_header('Cookie', 'cade-meu-cookie=\"esta aqui\"')
	response = urllib2.urlopen(req)
	page = response.read()
	print page
	
if __name__ == '__main__':
    main()
