import json
from morning import push_message,tx_data

# 读取JSON配置文件
with open('config.json', mode="r", encoding="utf-8") as f:
    config = json.load(f)


# 读取数据库获取用户数据
def get_user_data():
    pass


token = config["token"]
tx_apikey = config["tx_apikey"]

# 实例化天行类
tianxing = tx_data.get_data(tx_apikey)

# 暂时从配置文件中获取用户数据
user_data = config["user_data"]

def send_notify(token, user_data):
    push_message.get_push(token, tianxing,user_data)


if __name__ == "__main__":
    send_notify(token, user_data)
    print(user_data)
