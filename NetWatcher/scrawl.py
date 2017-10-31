import requests
from datetime import datetime
from pyquery import PyQuery as pq
import time

board_list = ['ITjob', 'Intern', 'ParttimeJobPost']
base_url = 'http://www.newsmth.net/'
data = dict()
num = []  # 编号
now = None


def get_content(url):
    resp = get(url)
    resp.encoding = 'gbk'
    html = pq(resp.text)
    content = html('.b-content')('.a-content').eq(0).html()
    content = content.replace('<br>', '\n').replace('<p>', '\n').replace('</p>', '\n')
    content = pq(content).text()
    return content


def get_board(board):
    resp = get(base_url + 'nForum/board/%s?ajax' % board)
    resp.encoding = 'gbk'
    trs = pq(resp.text)('tbody')('tr').not_('.top')
    for i in range(len(trs)):
        tds = trs.eq(i).find('td')
        t = tds.eq(2).text()
        if ':' in t:
            t = time.strptime(time.strftime('%Y:%m:%d:', time.localtime()) + t, '%Y:%m:%d:%H:%M:%S')
        else:
            continue
        it = dict()
        it['time'] = t
        it['title'] = tds.eq(1).text()
        url = tds.eq(1).find('a').attr('href')
        if url in data:
            continue
        it['id'] = url
        it['content'] = get_content(base_url + url)
        data[url] = it
    return data


def get(url):
    for i in range(3):
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                return resp
        except:
            continue


def scrawl_data():
    global now, num
    print(scrawl_data.__name__)
    if datetime.now().hour == 0:
        data.clear()
    for i in board_list:
        get_board(i)
    n = 0
    now = ''
    num = []
    for i in data:
        num.append(data[i])
        now += '%d %s\n' % (n, data[i]['title'])
        n += 1
    print(scrawl_data.__name__, 'over')
