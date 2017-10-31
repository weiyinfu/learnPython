from jinja2 import Environment, PackageLoader, Undefined

env = Environment(loader=PackageLoader('学习jinja', 'template1'))
env2 = Environment(loader=PackageLoader('学习jinja', 'template2'))
template1 = env.get_template('a.html')
template2 = env2.get_template('a.html')
print(template1.render(name='wyf'))
print(template2.render(name='wyf'))
expr=env2.compile_templates(template2)
print(expr(name='wyf'))
