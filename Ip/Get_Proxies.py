# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-02-07 
"""
# IP地址取自国内髙匿代理IP网站：http://www.xicidaili.com/nn/
# 仅仅爬取首页IP地址就足够一般使用

from bs4 import BeautifulSoup
import requests
import random

class Get_proxies(object):
    def get_ip_list(self, url, headers):
        web_data = requests.get(url, headers=headers)
        # print(web_data)
        soup = BeautifulSoup(web_data.text, 'lxml')
        # print(soup)
        ips = soup.find_all('tr')
        # print(ips)
        ip_list = []
        for i in range(1, len(ips)):
            ip_info = ips[i]
            # print(ip_info)
            tds = ip_info.find_all('td')
            # print(tds)

            ip_list.append(tds[1].text + ':' + tds[2].text)
        return ip_list

    def get_random_ip(self, ip_list):
        proxy_list = []
        for ip in ip_list:
            proxy_list.append('http://' + ip)
        # print(proxy_list)
        proxy_ip = random.choice(proxy_list)
        proxies = {'http': proxy_ip, }
        return proxies

if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nn/'
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    # }
    headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.5.506 UWS/2.10.1.22 Mobile Safari/537.36'
    }
    getProxies = Get_proxies()
    ip_list = getProxies.get_ip_list(url, headers=headers)
    proxies = getProxies.get_random_ip(ip_list)
    print(proxies)