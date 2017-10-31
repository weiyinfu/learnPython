HttpRequest对象的属性：
* path 路径信息
* method 字符串，GET 或者POST
* GET，POST，REQUEST(deprecated) QueryDict类型的对象，存储请求参数，REQUEST是GET和POST的合体
* COOKIES，FILES（filename，content-type，content）
* META 浏览器元信息等
* raw_post_data 原始post数据
* session 唯一的可读写属性
* user django内置的用户管理

HttpRequest对象的方法：
* has_key()
* get_full_path()
* is_secure()

QueryDict是一键多值字典，派生出GET、POST对象，举例：
```
q=QueryDict("a=1&a=2&a=3")
q.lists()
输出：[('a',['1','2','3'])]
```