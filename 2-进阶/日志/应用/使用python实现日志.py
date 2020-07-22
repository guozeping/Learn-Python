# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/4-教程/18
# 创建一个日志器logger并设置其日志级别为DEBUG
import logging
logging = logging.getLogger('simple_logger')
logging.setLevel(logging.DEBUG)

# 创建一个流处理器handler并设置其日志级别为DEBUG
handler = logging.StreamHandler(sys.stdout)
handler.setLevle(logging.DEBUG)

# 创建一个格式器formatter并将其添加到处理器handler
formatter = logging.Formatter()

