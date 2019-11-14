from seleniumwire import webdriver  # Import from seleniumwire
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from requests_html import HTMLSession

import requests


def req_html(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
    }
    req = requests.get(url, headers=header)
    html = req.text

    title = BeautifulSoup(html, 'lxml').find('h3').text
    desc = BeautifulSoup(html, 'html.parser').select_one('div.mvic-desc > div.desc').text
    desc = desc.replace('by ,', '')
    tags = BeautifulSoup(html, 'html.parser').select_one('div.mvic-info > div.mvici-left > p').text

    mp4 = None
    ele = BeautifulSoup(html, 'html.parser').select_one('div.jw-media.jw-reset > video')
    print(ele)
    mp4 = ele.attrs['src']

    result = {
        'title': title,
        'desc': desc,
        'tags': tags,
        'm3u8': None,
        'mp4': mp4
    }
    return result


class Browser(object):
    def __init__(self, driver_path='/usr/local/bin/chromedriver', headless=True):
        self.options = Options()
        self.options.headless = headless
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(driver_path, chrome_options=self.options)
        self.html = None

    def open_url(self, url):
        self.driver.get(url)
        self.html = self.driver.page_source

    def get_m3u8(self):
        m3u8_url = None
        for req in self.driver.requests:
            if req.response and 'm3u8' in req.path:
                m3u8_url = req.path
        return m3u8_url

    def get_mp4(self):
        ele = BeautifulSoup(self.html, 'html.parser').select_one('div.jw-media.jw-reset > video')
        mp4 = ''
        try:
            mp4 = ele.attrs['src']
        except Exception as err:
            pass
        return mp4

    def get_info(self):

        title = BeautifulSoup(self.html, 'lxml').find('h3').text

        desc = BeautifulSoup(self.html, 'html.parser').select_one('div.mvic-desc > div.desc').text
        desc = desc.replace('by ,', '')

        tags = BeautifulSoup(self.html, 'html.parser').select_one('div.mvic-info > div.mvici-left > p').text

        mp4 = self.get_mp4()
        m3u8 = ''
        if 'blob' in mp4 or mp4 is None:
            mp4 = ''
            try:
                m3u8 = self.get_m3u8()
            except Exception as err:
                print('failed to get mp4 url')

        info = {
            'title': title,
            'desc': desc,
            'tags': tags,
            'm3u8': m3u8,
            'mp4': mp4
        }

        return info

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':

    url = 'http://javforme.me/movies/caribbeancompr-110819-003-runa-sezaki-monthly'
    browser = Browser()
    browser.open_url(url)
    info = browser.get_info()
    print(info)
    browser.quit()

    # url = 'http://javforme.me/movies/h0930-ki191105-horny-naomi-sekimoto-0930-48-years-old'
    # info = req_html(url)
    # print(info)

