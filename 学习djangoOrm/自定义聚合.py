import haha.wsgi
from django.db.models import Aggregate, CharField
from one.models import Article, Author, Tag


class GroupConcat(Aggregate):
    function = 'GROUP_CONCAT'
    template = '%(function)s(%(distinct)s%(expressions)s%(ordering)s%(separator)s)'

    def __init__(self, expression, distinct=False, ordering=None, separator=',', **extra):
        super(GroupConcat, self).__init__(
            expression,
            distinct='DISTINCT ' if distinct else '',
            ordering=' ORDER BY %s' % ordering if ordering is not None else '',
            separator=' SEPARATOR "%s"' % separator,
            output_field=CharField(),
            **extra)


s = Article.objects.all()\
    .values('author')\
    .annotate(tags=GroupConcat('tags', separator='|'))
print(s)
print(s.query)
