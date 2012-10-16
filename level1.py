#coding: utf-8
import urllib2

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

import re

PRICE_PATTERN = '.*(R\$ [0-9]+,[0-9]+).*'

class Level1Handler(ContentHandler):
    def __init__(self):
        self.extracted_content = ''
        self.is_div_element = False

    def startElement(self, name, attrs):
        if name == 'div':
            self.is_div_element = True

    def endElement(self, name):
        if name == 'div':
            self.is_div_element = False
             
    def characters(self, ch):
        if self.is_div_element:
            self.extracted_content += ch

def get_page_content_level1():
    url = 'http://hughes.sieve.com.br:9090/level1/'
    
    user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1284.0 Safari/537.13'
    header_dict = {'User-Agent': user_agent}
    req = urllib2.Request(url, headers = header_dict)
    response = urllib2.urlopen(req)
    return response

def parse_content_level1(content):
    parser = make_parser()
    handler = Level1Handler()
    parser.setContentHandler(handler)
    try:
        parser.parse(content)
    except:
        pass

    return re.findall(PRICE_PATTERN, handler.extracted_content.strip())[0]

def main():
    open_page = get_page_content_level1()
    extracted_content = parse_content_level1(open_page)
    assert extracted_content == 'R$ 44,99'
if __name__ == '__main__':
    main()
