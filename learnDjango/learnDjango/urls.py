from django.conf.urls import url
from django.contrib import admin
import 使用模板.views
import 使用URL.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", 使用模板.views.rawText),  # 默认视图
    url(r"rawHtml", 使用模板.views.rawHtml),
    url(r"useTemplate", 使用模板.views.useTemplate),
    url(r'passParam', 使用模板.views.passParam),
    url(r'redirect', 使用模板.views.redirect),
    url(r"extends", 使用模板.views.extends),
    url(r"includeExtends", 使用模板.views.includeExtends),

    # 使用模板
    url(r"^add/", 使用URL.views.add),
    url(r'useName', 使用URL.views.useName),
    # 正则表达式的每一个子组作为参数传递给view函数，args是一个元组
    url(r"^add2/(\d+)/(\d+)", 使用URL.views.add2, name='add2'),
]
