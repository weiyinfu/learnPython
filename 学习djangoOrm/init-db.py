import random

import numpy as np
import haha.wsgi
from one.models import *


def add_authors():
    for i in range(10):
        name = random.choice("赵钱孙李周吴郑王") + random.choice("床前明月光疑是地上霜")
        author, created = Author.objects.get_or_create(name=name)
        author.qq = ''.join(map(str, np.random.randint(0, 9, 7)))
        author.address = random.choice("江河湖海山") + random.choice("东西南北中")
        author.email = ''.join(map(str, np.random.randint(0, 10, 7))) + "@" + np.random.choice(
            ["qq", "buaa", '163']) + ".com"
        author.save()


def add_tags():
    for i in "语文 数学 英语 自然 品德 社会 物理 化学 地理 历史 政治 生物".split():
        tag, created = Tag.objects.get_or_create(name=i)
        tag.save()


def add_post():
    for i in range(30):
        title = "文章" + str(i)
        author = random.choice(Author.objects.all())
        article, created = Article.objects.get_or_create(title=title,
                                                         author=author,
                                                         content='content' + str(i))
        article.tags = [random.choice(Tag.objects.all()) for _ in range(3)]
        article.content = "content" + str(i)
        article.score = random.randint(0, 10)
        article.save()


add_tags()
add_authors()
add_post()
