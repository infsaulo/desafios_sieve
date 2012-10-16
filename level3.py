#coding: utf-8

import os.path
import urllib2

import re

PRICE_PATTERN = '.*(R\$ [0-9]+\.?[0-9]+,[0-9]+).*'

def set_up_cookie_stuff():
    COOKIEFILE = './cookies.txt'

    cj = None
    ClientCookie = None
    cookielib = None
    
    try:
        import cookielib
    except ImportError:
        try:
            import ClientCookie
        except ImportError:
            urlopen = urllib2.urlopen
            Request = urllib2.Request
        else:
            urlopen = ClientCookie.urlopen
            Request = ClientCookie.Request
            cj = ClientCookie.LWPCookieJar()
    else:
        urlopen = urllib2.urlopen
        Request = urllib2.Request
        cj = cookielib.LWPCookieJar()

    if cj is not None:
        if os.path.isfile(COOKIEFILE):
            cj.load(COOKIEFILE)
        if cookielib is not None:
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            urllib2.install_opener(opener)
        else:
            opener = ClientCookie.build_opener(ClientCookie.HTTPCookieProcessor(cj))
            ClientCookie.install_opener(opener)

def get_page_content_level3():

    set_up_cookie_stuff()

    url = 'http://hughes.sieve.com.br:9090/level3/'
    url2 = 'http://hughes.sieve.com.br:9090/level31/'
    
    # Definição de alguns parâmetros do Header
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/536.26.14 (KHTML, like Gecko) Version/6.0.1 Safari/536.26.14'
    accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8Response HeadersNameValue'
    accept_charset = 'utf-8'
    header_dict = {'Accept': accept, 'Accept-Charset': accept_charset, 'User-Agent': user_agent}

    req = urllib2.Request(url, headers= header_dict)
    response = urllib2.urlopen(req)
    req = urllib2.Request(url2, headers= header_dict)
    response = urllib2.urlopen(req)
    req = urllib2.Request(url, headers= header_dict)
    response = urllib2.urlopen(req)
    return response
    
def parse_content_level3(content):
    page_content = content.read()
    return re.findall(PRICE_PATTERN, page_content.strip())[0]

def main():
    open_page = get_page_content_level3()
    extracted_content = parse_content_level3(open_page)
    assert extracted_content == 'R$ 499,00'

if __name__ == '__main__':
    main()
