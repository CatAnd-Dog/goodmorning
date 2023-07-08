
import requests
from bs4 import BeautifulSoup as bs
import random


# 爬虫获取天气
def get_weather(region):
    url = 'https://www.tianqi.com/'+region+'/'
    UserAgent = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",

        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",

        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",

        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",

        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",

        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',

        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',

        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',

        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',

        'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',

        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",

        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "

    ]
    header = {'User-Agent': UserAgent[random.randint(0, 12)]}
    resp = requests.request("GET", url, headers=header)
    resp.encoding = 'utf-8'
    soup = bs(resp.text, "html.parser")
    data = soup.find("dl", {"class": "weather_info"})

    shidu = data.find("dd", {"class": "shidu"}).find_all("b")
    kongqi = data.find("dd", {"class": "kongqi"})

    today_time = data.find("dd", {"class": "week"}).text
    today_weather = data.find("dd", {"class": "weather"}).find("span").text
    today_humidity, today_wind, today_ul= shidu[0].text, shidu[1].text, shidu[2].text
    today_air=kongqi.find("h5").text
    today_pm=kongqi.find("h6").text
    today_sun=kongqi.find("span").text

    line2=today_weather + "   " + today_air + "   " + today_pm
    line3=today_humidity + "   " + today_wind + "   " + today_ul
    # line4=today_air + "   " + today_pm
    # return today_time,today_weather, today_humidity, today_wind, today_ul, today_air, today_pm, today_sun # 返回今日天气数据
    # 组合一下再返回

    return today_time, line2,line3 # 返回今日天气数据

# 爬虫获取每日情话
def getword():
    '''
    获取一段暖话
    :return:
    '''
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }
    user_url = 'http://www.ainicr.cn/qh/t83.html'
    resp = requests.get(user_url, headers=headers)
    soup_texts = bs(resp.text, 'html.parser')
    # 『one -个』 中的每日一句
    num = random.randint(0,30)
    every_msg = soup_texts.find_all('div', class_='pbllists')[0].find_all('p')[num].text
    return every_msg

# 爬虫获取英语每日一句
def get_ciba():
    url = "http://open.iciba.com/dsapi/"
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    note_en = r.json()["content"]
    note_ch = r.json()["note"]
    return note_ch, note_en