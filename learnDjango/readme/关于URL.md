在urls.py中，建立URL、函数、链接名称三者之间的映射  
`url(r'hhaa',myview.haha,name='haha')`

当url和函数发生改变并且name不变，就可以用name去调用这个函数，去访问这个链接  
在python manage.py shell 下，  
旧版使用：`django.core.urlresolvers.reverse("haha",args=(4,5))`
新版使用：`django.urls.reverse`
就会返回一个链接，“haha”表示URL的name  

在HTML中，使用`{url 'haha'}`(不带参数),`{url 'haha' 2  3 4}`（带参数）的形式来表示URL。

用reverse(name,args=())函数还可以进行重定向。
`return django.http.HttpResponseRedirect(reverse('add',args=(a,b)))`

