#coding: utf-8

import urllib2
import Cookie

import re

PRICE_PATTERN = '.*(R\$\s([0-9]\s?)+,([0-9]\s?)+).*'

def main():
	url = 'http://hughes.sieve.com.br:9090/level4/'
	user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/536.26.14 (KHTML, like Gecko) Version/6.0.1 Safari/536.26.14'
	
	req = urllib2.Request(url)
	req.add_header('User-Agent', user_agent)
	req.add_header('Cookie', 'cade-meu-cookie=\"esta aqui\"')
	response = urllib2.urlopen(req)
	page = response.read()
	print re.findall(PRICE_PATTERN, page.strip())[0][0]
	
if __name__ == '__main__':
    main()
