from string import Template

x = Template("$who likes $what")
res = x.substitute({
    'who': 'weiyinfu',
    'what': 'programming'
})
print(res)


class CustomTemplate(Template):
    delimiter = '@'
    idpattern = "[a-z]+"  # 标识符的正则表达式


x = CustomTemplate("@who likes @what")
print(x.substitute({
    'who': "weiyinfu",
    "what": "programming",
}))
