import requests
from datetime import date




class get_data():
    today = date.today()


    def __init__(self,apikey):
        self.apikey=apikey

    # 获取位置的拼音，用于获取天气
    def get_areaen(self,area):
        url = "https://apis.tianapi.com/citylookup/index?key={}&area={}".format(self.apikey,area)
        response = requests.get(url)
        data = response.json()
        return data["result"]["list"][0]["areaen"]


    # 生活小窍门
    def get_tips(self):
        url = "https://apis.tianapi.com/qiaomen/index?key={}".format(self.apikey)
        response = requests.get(url)
        data = response.json()
        return data["result"]["content"]

    # 健康小提示
    def get_health(self):
        url = "https://apis.tianapi.com/healthtip/index?key={}".format(self.apikey)
        response = requests.get(url)
        data = response.json()
        return data["result"]["content"]


    # 老黄历查吉凶祸福
    def get_huangli(self):

        url = "https://apis.tianapi.com/lunar/index?key={}&date={}".format(self.apikey,self.today)
        response = requests.get(url)
        data = response.json()
        data=data["result"]
        return data["fitness"], data["taboo"]

    # 获取民俗对联
    def get_duilian(self):
        url = "https://apis.tianapi.com/msdl/index?key={}&num=1".format(self.apikey)
        response = requests.get(url)
        data = response.json()
        data=data["result"]["list"][0]
        return data["shanglian"], data["xialian"]

    # 获取诗词
    def get_poetry(self):
        url = "https://apis.tianapi.com/duishici/index?key={}".format(self.apikey)
        response = requests.get(url)
        data = response.json()
        data=data["result"]
        return data["quest"], data["answer"],data["source"]

    # 朋友圈文案
    def get_friend(self):
        url = "https://apis.tianapi.com/pyqwenan/index?key={}".format(self.apikey)
        response = requests.get(url)
        data = response.json()
        return data["result"]["content"]

    # 经典台词
    def get_taic(self):
        url = "https://apis.tianapi.com/dialogue/index?key={}".format(self.apikey)
        response = requests.get(url)
        data = response.json()
        return data["result"]["dialogue"], data["result"]["source"]

    # 彩虹屁
    def get_flatter(self):
        url = "https://apis.tianapi.com/caihongpi/index?key={}".format(self.apikey)
        response = requests.get(url)
        data = response.json()
        return data["result"]["content"]

    # 高级emo
    def get_emo(self):
        url = "https://apis.tianapi.com/hsjz/index?key={}".format(self.apikey)
        response = requests.get(url)
        data = response.json()
        return data["result"]["content"]

    # 卑微爱情的独白记录
    def get_love(self):
        url = "https://apis.tianapi.com/tiangou/index?key={}".format(self.apikey)
        response = requests.get(url)
        data = response.json()
        return data["result"]["content"]

    # 早安鸡汤
    def get_jitang(self):
        url = "https://apis.tianapi.com/zaoan/index?key={}".format(self.apikey)
        response = requests.get(url)
        data = response.json()
        return data["result"]["content"]

    # 猜字谜
    def get_riddle(self):
        url = "https://apis.tianapi.com/zimi/index?key={}".format(self.apikey)
        response = requests.get(url)
        data = response.json()
        data = data["result"]
        return data["content"], data["answer"], data["reason"]

    # 毒鸡汤
    def get_djt(self):
        url = "https://apis.tianapi.com/dujitang/index?key={}".format(self.apikey)
        response = requests.get(url)
        data = response.json()
        return data["result"]["content"]

    # 心里鸡汤
    def get_xlt(self):
        url = "https://apis.tianapi.com/mingyan/index?key={}".format(self.apikey)
        response = requests.get(url)
        data = response.json()
        data = data["result"]["list"][0]
        return data["content"],data["author"]

    # 脑筋急转弯
    def get_brain(self):
        url = "https://apis.tianapi.com/naowan/index?key={}&num=1".format(self.apikey)
        response = requests.get(url)
        data = response.json()
        data = data["result"]["list"][0]
        return data["quest"], data["result"]

    # 英语格言
    def get_english(self):
        url = "https://apis.tianapi.com/enmaxim/index?key={}".format(self.apikey)
        response = requests.get(url)
        data = response.json()
        data = data["result"]
        return data["en"], data["zh"]

    # 宋词
    def get_songci(self):
        url = "https://apis.tianapi.com/zmsc/index?key={}".format(self.apikey)
        response = requests.get(url)
        data = response.json()
        data = data["result"]
        return data["content"], data["source"]

    # 情诗
    def get_qingshi(self):
        url = "https://apis.tianapi.com/qingshi/index?key={}".format(self.apikey)
        response = requests.get(url)
        data = response.json()

        return data["result"]["content"]


