# 简明python教程随笔

## 默认运行的python的版本
`python -V`           


## Print
`print 'Hello World'`


## 字符串  
- 单引号 `’`
- 双银行 `“`
- 三银行 `’‘’`
- 转义符(续行符） `\`


## 标识符
- 首字符是字母或者下划线
- 可以由字符，下划线，数字组成
- 大小写敏感


## 对象
- Python把在程序中 到的任何东 都称为 对象 


## 赋值
- `=` 从右往左赋值

## 逻辑行与物理行
-  一个物理中使用多于一个逻辑行，需分号 `;` 隔开
-  一个逻辑行写在多于一个物理行，需反斜线 `\` 续航


## 缩进
- 同一层次的语句必须有相同的缩进。
- 每一组这样的语句称为一个块。
- 每个缩进层次使用单个制表符 或 两个 或 四个空格
 
 
## 运算符

## 表达式

## 控制流
- if，elif，else
- while：循环语句，只要在一个条件为真的情况下，while语允许你重复执一块语句。（参考 while.py)
- for .. in：循环语句，它在一序列的对象上 递归 即逐一使用队列中的每个项目。（参考 for.py）
- break：终止循环语句，即使循环条件不是False或系列未被完全递归， 也停止循环语 。 PS：从for或while循环中终止，任何对应的循环else块将不执行 （参考 break.py）
- continue：跳过当前循环块中的剩余语，然后继续进行下一轮循环

## 参数形式
- 函数取得的参数是人工提供给函数的值，这样函数就可以利用不过它们的值做一些事情。这些参数就好像变量一样，只不过它们的值是在我们调用函数的时候定义的，而非在函数本身内赋值。- 参数在函数定义的圆括号对内指定，用逗号分割。当我们调用函数的时候，我们以同样的方式提供值。
- 注意我们使用过的术语
    + 形参：函数中的参数名称  
    + 实参：提供给函数调的值


## 变量
- 局部变量：函数定义内声明变量时，变量与函数外具有相同名称的其他变俩没有任何关系，即 变量名称对于函数来说是 局部 的。这称为变量的作用域。所有变量的作用域是它们被定义的块，从它们的名称被定义的那点开始
- 全局变量：global语句，表明变量是在外面的块定义的。是不可能为定义在函数外的变量赋值的。
  
## 参数
- 默认参考值：func_default.py
- 关键参数：函数有多个参数，你只想指定其中的一部分，那么你可以通过命名来为这些参数赋值——这被称作 关键参数 ——我们使用名字(关键字)而不是位置来给函数指定实参

## return
从一个函数返回即跳出函数。我们也可选从函数返回一个值。


## DocStrings ？？



## 模块
```
模块基本上就是一个包含了所有你定义的函数和变量的文件。为了在其他程序中重用模块，模块的件名必须以.py为扩展名。
```

### import

```
模块应该被放置以下目录才能被import
- sys.path 所列目录之一
- 和使用它的程序在同一个目录中
```

种类

1. `import`

```
import mymodulemymodule.sayhi()print 'Version',mymodule.version
```
    
2. `from...import`

```
from mymodule import sayhi, version 

sayhi()print 'Version',version
```


### sys模块

包含与Python解释和它的环境有关的函数,存放在sys.path变量中所列目录中

- sys.argv: 变量是一个字符串的列表. 这种方法的优势是这个名称不会与任何在你的程序中使用的argv变量冲突。另外，它也清晰地表明这个名称是sys模块的 部分。
- 脚本的名称总是sys.argv列表的第一个参数

  ```
  python using_sys.py wearearguments
  sys.argv[0]: `using_sys.py`
  sys.argv[1]: 'we'
  sys.argv[2]: 'are'
  sys.argv[3]: 'arguments'
  ```
  
- 查看sys模块的内容, dir()函数

```
$ python
Python 2.7.10 (default, Feb  7 2017, 00:08:15)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> dir(sys)
['__displayhook__', '__doc__', '__egginsert', '__excepthook__', '__name__', '__package__', '__plen', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_getframe', '_mercurial', 'api_version', 'argv', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_clear', 'exc_info', 'exc_type', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'gettrace', 'hexversion', 'long_info', 'maxint', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'py3kwarning', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'settrace', 'stderr', 'stdin', 'stdout', 'subversion', 'version', 'version_info', 'warnoptions']
```  

## 数据结构

### 分类

- 列表list: 处理一组有序项目的数据结构. list=[a,b,c]
- 元组tuple: 元组不可变,即不能修改元组. tuple=(a,b,c). %s被替换为变元组中的值
- 字典dict: key(唯一)和value dict={key1:value1, key2:value2}。字典中的键/值对是没有顺序的。如果你想要 个特定的顺序，那么你应该在使 前   对它们排序。

### 序列

列表、元组和字符串都是序列.
序列的两个主要特点
- 索引操作符(index): 从序列中抓取某个特定项. list[1]
- 切片操作符(slice): 序列的一个切片，即一部分序列. list[1:3]

对象和引用

- mylist = shoplist     mylist, shoplist指向同一片内存区域, 任何一方改变, 另一方都会跟着改变
- mylist = shoplist[:]  将shoplist某时刻的切片值赋给mylist, 之后改变shoplist的值, mylist的值不会改变.

### 字符串

字符串的操作

- a.startswith('x') 测试字符串是否以给定字符 开 始
- 'x' in name       in操作符检验一个给定字符串是否为另一个字符串的一部分
- name.find('x') != -1 找出给定字符串在另一个字符串中的位置

## python脚本
参考 backup_ver*.py

## 面对对象的编程

### 类

类中的函数与普通函数的区别只是一个额外的self变量.

- `__init__` 方法: 在类的一个对象被建立时，马上运行. (类似构造函数)


### 继承

### 储存器

### 异常
- try..except
- try..finally

