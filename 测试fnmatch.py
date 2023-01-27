import fnmatch
from os.path import *

print(fnmatch.fnmatch('one', '/one'))
print(fnmatch.fnmatch('one/', 'one'))
print(fnmatch.fnmatch('onetwo', 'one*'))
print(fnmatch.fnmatch('x/one/two', '*/one/two'))
print(fnmatch.fnmatch('two', '**/two'))
print(fnmatch.fnmatch('one/two', '**/two'))
print(relpath("one/two/three", "one"))
