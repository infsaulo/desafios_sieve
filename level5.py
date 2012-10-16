#coding: utf-8

import urllib2

import re

PRICE_PATTERN = '.*(R\$\s([0-9]\s?)+,([0-9]\s?)+).*'

def get_page_content_level5():
    url = 'http://hughes.sieve.com.br:9090/level5'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    url = response.geturl().replace('%', '%25')
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    return response
     
def main():
    open_page = get_page_content_level5()
    extracted_content = re.findall(PRICE_PATTERN, open_page.read().strip())[0][0]
    assert extracted_content == 'R$ 40 0,0 0'
    
if __name__ == '__main__':
    main()
