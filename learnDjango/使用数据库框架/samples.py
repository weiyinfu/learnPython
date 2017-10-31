from 使用数据库框架.models import *

"""
Django自带ORM框架，这个ORM框架也是挺复杂的，需要把SQL那一套照搬一遍，只不过写起来都是python函数，不用写SQL语句了
学习Django，这个ORM框架是很有必要精通的
"""

# 查看底层执行了什么样的SQL语句
print(Author.objects.all().query.__str__())
print(Author.objects.filter(name="WeizhongTu").query.__str__())

# values_list获取元组形式的结果，list中每个元素都是元组
print(Author.objects.values_list('name', 'qq').__str__())
# 如果元组中只有一个属性，那么可以使用flat参数，去掉元组,默认flat=False
print(Author.objects.values_list('name', flat=True).__str__())

# values获取字典形式的结果，list中的每个元素都是字典
print(Author.objects.values('name', 'qq'))

"""
注意：

1. values_list 和 values 返回的并不是真正的 列表 或 字典，也是 queryset，他们也是 lazy evaluation 的（惰性评估，通俗地说，就是用的时候才真正的去数据库查）
2. 如果查询后没有使用，在数据库更新后再使用，你发现得到在是新内容！！！如果想要旧内容保持着，数据库更新后不要变，可以 list 一下
3. 如果只是遍历这些结果，没有必要 list 它们转成列表（浪费内存，数据量大的时候要更谨慎！！！）
"""

# extra实现别名、条件、排序，因为条件和排序可以分别用filter和order_by函数实现，所以extra的主要功能就是重命名某个属性
# 别名，如果不加defer，会查询两个name属性
print(Tag.objects.all().extra(select={'tag_name': 'name'}).query.__str__())
print(Tag.objects.all().extra(select={'tag_name': 'name'}).defer('name').query.__str__())

# annotate聚合、计数、求和、平均数等操作
# annotate计数
from django.db.models import Count

# 查询作者及其文章数列表
Article.objects.all().values('author_id').annotate(count=Count('author')).values('author_id', 'count')
# 查询作者姓名及其文章数列表
Article.objects.all().values('author__name').annotate(count=Count('author')).values('author__name', 'count')
# 注意，上面两例中，直接使用author__id,author__name访问author表中的属性

# annotate求平均值
from django.db.models import Avg

Article.objects.values('author_id').annotate(avg_score=Avg('score')).values('author_id', 'avg_score')
# annotate求和
from django.db.models import Sum

Article.objects.values('author__name').annotate(sum_score=Sum('score')).values('author__name', 'sum_score')

# select_related 进行关联查询，下面这句话会把author的具体内容（例如name）查出来
# 而默认是只会查询article这一个表
# select_related用于优化多对一、一对一查询
articles = Article.objects.all().select_related('author')

# prefetch_related 也是进行关联查询，但它是一对多、多对多查询
# 会查询多个表
articles = Article.objects.all().prefetch_related('tags')

# defer去除不需要的字段
Article.objects.all().defer('content')
# only只要需要的字段
Article.objects.all().only('content')
