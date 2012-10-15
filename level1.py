#coding: utf-8
import urllib2


def main():
    url = 'http://hughes.sieve.com.br:9090/level1/'
    
    # Definição do header User-Agent como Google Chrome
    user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1284.0 Safari/537.13'
    header_dict = {'User-Agent': user_agent}
    req = urllib2.Request(url, headers = header_dict)
    response = urllib2.urlopen(req)
    price_page = response.read()
    print price_page

if __name__ == '__main__':
    main()
