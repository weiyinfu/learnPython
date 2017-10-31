import haha.wsgi
from one.models import Author, Article, Tag
from django.db import models

a = [
    # 查询全部文章
    Article.objects.all(),
    # 查询王明的全部文章
    Article.objects.filter(author__name='王明'),
    # 返回字典
    Article.objects.filter(author__name='王明').values('title', 'author__name'),
    # 返回元组
    Article.objects.filter(author__name='王明').values_list('title', 'author__name'),
    # 使用包含命令
    Article.objects.filter(tags__name__contains='语文').values_list('author__name'),
    # 使用flat处理单元素
    Article.objects.filter(tags__name__contains='语文').values_list('author__name', flat=True),
    # 使用extra添加额外列
    Article.objects.filter(tags__name='语文')
        .extra(select={'题目': 'title', "内容": 'content'}).all(),
    # 使用defer删除列
    Article.objects.filter(tags__name__contains='语文')
        .extra(select={'题目': 'title', "内容": 'content'})
        .defer('title', 'content').all(),

    # 使用聚合进行计数，统计每位作者的文章数
    Article.objects.all()
        .values('author_id').annotate(count=models.Count('author'))
        .values('author__name', 'count'),
    # 使用聚合进行求和，求平均：统计每位作者的平均得分
    Article.objects.all().values('author')
        .annotate(avg=models.Avg('score'),
                  sum=models.Sum('score'),
                  cnt=models.Count('score'))
        .values(*"avg sum cnt".split()),

    # 使用数组切片
    Tag.objects.all()[3:5],

    # 使用select_related进行外键关联查询，适合于多对一查询
    Article.objects.all().select_related("author")[:3],

    # 使用prefetch_related进行外键关联查询，这是多次查询，将最终查询结果拼凑到一起
    Article.objects.all().prefetch_related("tags").values('tags')[:3],


    # 使用only仅选择需要的字段
    Article.objects.all().only('author__name')
]

for j, i in enumerate(a):
    print("[INPUT %s]:" % j, i.query, '\n')
    print("[OUTPUT %s]:" % j, i, '\n')
