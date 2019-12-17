# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/4/16
"""
os.sep     可以取代操作系统特定的路径分割符


os.linesep  字符串给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n' 而Mac使用'\r'。

os.name         字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'

os.getcwd()   函数得到当前工作目录，

os.getenv()和os.putenv()   函数分别用来读取和设置环境变量。

os.listdir(dirname)： 列出dirname下的目录和文件

os.remove()  函数用来删除一个文件。

os.curdir:   返回但前目录（'.')

os.chdir(dirname): 改变工作目录到dirname

getatime(path):文件或文件夹的最后访问时间，从新纪元到访问时的秒数

getmtime(path):文件或文件夹的最后修改时间

getctime(path):文件或文件夹的创建时间




os.path模块:

os.path.isfile()和os.path.isdir()函数分别检验给出的路径是一个文件还是目录,返回bool值

os.path.exists()函数用来检验给出的路径是否真地存在 返回bool

os.path.getsize(name):获得文件大小，如果name是目录返回0L 返回long 单位是字节

os.path.abspath(name):获得绝对路径

os.path.normpath(path):规范path字符串形式, 结果一般情况下把/变为//,

os.path.split(name):将name分割成路径名和文件名，结果为（路径名，文件名.文件扩展名）（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在）

os.path.splitext(filename):分离文件名与扩展名 结果为（filename，扩展名） 如果参数为一个路径 则返回（路径，''）

os.path.join(path,name): 连接目录与文件名或目录 结果为path/name

os.path.basename(path):返回文件名 实际为把path的最后一个"/"分割，返回后者。不管参数是一个路径还是文件 与os.path.split(name)相同 不同之处后者返回两个值得元组




os.path.dirname(path): 返回文件路径 实际为把path的最后一个"/"分割，返回前者。不管参数是一个路径还是文件

os.system()函数用来运行shell命令




上面仅是常见的，一下列出所有的：




os模块包装了不同操作系统的通用接口，使用户在不同操作系统下，可以使用相同的函数接口，返回相同结构的结果。

os.name:返回当前操作系统名称（'posix', 'nt', 'os2', 'mac', 'ce' or 'riscos'）

os中定义了一组文件、路径在不同操作系统中的表现形式参数，如

os.sep（文件夹分隔符，windows中是 \ ）

os.extsep（扩展名分隔符，windows中是 . ）

os.pathsep（目录分隔符，windows中是 ; ）

os.linesep（换行分隔符，windows中是 \r\n ）

os中有大量文件、路径操作的相关函数，如：

listdir(path):列举目录下的所有文件

makedir(path):创建文件夹，注：创建已存在的文件夹将异常

makedirs(path):递归式的创建文件夹，注：创建已存在的文件夹将异常

remove(filename):删除一个文件

rmdir(path):删除一个文件夹，注：删除非空的文件夹将异常

removedirs(path):递归的删除文件夹，直到有一级的文件夹非空，注：文件夹路径不能以'\'结束

rename(src,dst):给文件或文件夹改名（可以改路径，但是不能覆盖目标文件）

renames(src,dst):递归式的给文件或文件名改名

walk(path):列举path下的所有文件、文件夹

os中与进程相关的操作，如：

execl(path):运行一个程序来替代当前进程，会阻塞式运行

_exit(n):退出程序

startfile(filename):用与文件关联的程序运行，关联程序打开后，立即返回

system(cmd):运行一个程序或命令，会立即返回，并在cmd执行完成后，会返回cmd退出代码

os.path:在不同的操作系统中调用不同的模块，是一个可import的模块，这个模块中提供很多有用的操作：

abspath(path):返回path的绝对路径，若path已经是绝对路径了，则保持。

basename(path):返回path中的文件名。

commonprefix(list):返回list中的统一前缀，用于获得一组字符串的左起相同的内容

dirname(path):返回path中的文件夹部分，结果不包含'\'

exists(path):文件或文件夹是否存在

getatime(path):文件或文件夹的最后访问时间，从新纪元到访问时的秒数

getmtime(path):文件或文件夹的最后修改时间

getctime(path):文件或文件夹的创建时间

getsize(path):文件或文件夹的大小，若是文件夹返回0

isabs(path):返回是否是绝对路径

isfile(path):返回是否是文件路径

isdir(path):返回是否是文件夹路径

islink(path):返回是否是快捷方式

join(path1,path2,...):将path进行组合，若其中有绝对路径，则之前的path将被删除

normcase(path):转换路径中的间隔符

normpath(path):转换路径为系统可识别的路径

realpath(path):转换路径为绝对路径

split(path):将路径分解为(文件夹,文件名)

splitext(path):将路径分解为(其余部分,.扩展名)，若文件名中没有扩展名，扩展名部分为空字符串

在操作与系统不支持的对象时，抛出OSError异常。


"""

