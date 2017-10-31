import hashlib
import re
import time
import xml.etree.ElementTree as ET
from datetime import datetime

import apscheduler.schedulers.background as bg
from flask import Flask, request

import scrawl

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def haha():
    if request.method == 'GET':
        token = '20124003'  # 微信配置所需的token
        signature = request.args.get('signature', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        echostr = request.args.get('echostr', '')
        s = ''.join(sorted([timestamp, nonce, token]))
        sha1 = hashlib.sha1()
        sha1.update(bytes(s, "utf8"))
        if sha1.hexdigest() == signature:
            return echostr
    else:
        xml = ET.fromstring(request.data)
        toUser = xml.find('ToUserName').text
        fromUser = xml.find('FromUserName').text
        msgType = xml.find("MsgType").text
        createTime = xml.find("CreateTime")
        if msgType == "text":
            content = xml.find('Content').text
            return reply_text(fromUser, toUser, reply(fromUser, content))
        else:
            return reply_text(fromUser, toUser, "我只懂文字")


@app.route("/ok")
def ok():
    return 'i am ok'


@app.route("/what")
def what():
    return str(scrawl.data)


def reply_text(to_user, from_user, content):
    """
    以文本类型的方式回复请求
    :param to_user: 
    :param from_user: 
    :param content: 
    :return: 
    """
    return """
    <xml>
        <ToUserName><![CDATA[{}]]></ToUserName>
        <FromUserName><![CDATA[{}]]></FromUserName>
        <CreateTime>{}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{}]]></Content>
    </xml>
    """.format(to_user, from_user,
               int(time.time() * 1000), content)


def reply(openid, msg):
    # 简单地翻转一下字符串就回复用户
    if re.match('\d+', msg):
        x = int(msg)
        if x < len(scrawl.num):
            return scrawl.num[x]['content']
    else:
        return scrawl.now


# 不能将初始化部分放在main部分，gunicorn运行时不执行main部分
scheduler = bg.BackgroundScheduler()
scheduler.add_job(scrawl.scrawl_data, 'interval', hours=1, next_run_time=datetime.now())
scheduler.start()
if __name__ == '__main__':
    app.run()
