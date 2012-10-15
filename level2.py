#coding: utf-8

import os.path
import urllib2

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

def main():

    set_up_cookie_stuff()

    url = 'http://hughes.sieve.com.br:9090/level2/'
    
    # Definição de alguns parâmetros do Header
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/536.26.14 (KHTML, like Gecko) Version/6.0.1 Safari/536.26.14'
    accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8Response HeadersNameValue'
    accept_charset = 'utf-8'
    header_dict = {'Accept': accept, 'Accept-Charset': accept_charset, 'User-Agent': user_agent}

    req = urllib2.Request(url, headers= header_dict)
    response = urllib2.urlopen(req)
    req = urllib2.Request(url, headers= header_dict)
    response = urllib2.urlopen(req)
    price_page = response.read()
    print price_page
    
if __name__ == '__main__':
    main()
