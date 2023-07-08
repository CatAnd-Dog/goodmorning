import json
import random
import requests

from morning import pic_url,spider_data


# 获取随机颜色
def get_color():
    get_colors = lambda n: list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF), range(n)))
    color_list = get_colors(100)
    return random.choice(color_list)


def add_content(tianxing,user_data):
    content = ""
    # 先来一张美图
    get_pic_url = random.choice(pic_url.url_pic)
    content += "<img src='{}' style='width: auto'>".format(get_pic_url)

    # 获取用户的位置转换为拼音，然后获取天气
    area = user_data["user_location"]
    areaen = tianxing.get_areaen(area)

    # 获取天气信息
    weather= spider_data.get_weather(areaen)
    for weather_data in weather:
        content += "<p style='color:{};'>{}</p>".format(get_color(),weather_data)

    # 下面的内容可以自由替换
    # 情诗一首
    if user_data["user_morning"] :
        jitang = tianxing.get_jitang()
        content += "<p style='color:{};'>早安：{}</p>".format(get_color(),jitang)

    # 生活小窍门
    if user_data["user_tips"] :
        tips = tianxing.get_tips()
        content += "<p style='color:{};'>生活小窍门：{}</p>".format(get_color(),tips)

    # 健康小提示
    if user_data["user_health"] :
        health = tianxing.get_health()
        content += "<p style='color:{};'>健康小提示：{}</p>".format(get_color(),health)

    # 老黄历
    if user_data["user_huangli"] :
        fitness, taboo = tianxing.get_huangli()
        content += "<p style='color:{};'>今日宜：{}</p>".format(get_color(),fitness)
        content += "<p style='color:{};'>今日忌：{}</p>".format(get_color(),taboo)

    # 中英文格言
    if user_data["user_english"] :
        en, zh = tianxing.get_english()
        content += "<p style='color:{};'>每日一句：{}</p>".format(get_color(),zh)
        content += "<p style='color:{};'>每日一句：{}</p>".format(get_color(),en)

    # 后面自己加

    return content


def get_push(token, tianxing, user_data):
    url = "https://www.pushplus.plus/send"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Content-Type': 'application / json',
        'charset': 'UTF - 8'
    }

    title = "亲爱的{},早上好！".format(user_data["user_name"])

    content = add_content(tianxing,user_data)

    data = {"to": user_data["user_token"],
            "token": token,
            "title": title,
            "content": content,
            "template": "html",
            "channel": "wechat"}
    body = json.dumps(data).encode(encoding='utf-8')
    response = requests.post(url, headers=headers, data=body).json()
    print(response["msg"])
