python中的import有可能是在运行时加载的，而运行时加载sys.module就已经开始分叉了，所以会执行多个import。

如果import的是需要编译的模块，那么这个模块有可能被多次编译，造成浪费。

sys.modules不是全局共享的。


为cython实现import存在一些问题：
* 因为import是并发执行的import，所以import的时候可能会编译多次，导致import特别缓慢。
* 只要实现了import hook都会影响性能。
* 需要避免影响其它模块的pyx文件，因为其它模块的pyx文件可能不需要编译，直接使用即可。

保持事物本身的形态，不要使用import hook，不要尝试把不一样的东西封装成import可以用的东西。如果import的东西是数据，则直接写一个数据加载模块即可。