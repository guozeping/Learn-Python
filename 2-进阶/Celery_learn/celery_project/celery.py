# -*- coding: utf-8 -*-
# Created by Guozeping on 2019/6/19
from __future__ import absolute_import, unicode_literals
from celery import Celery


app = Celery('proj',
             broker='redis://47.102.153.238',
             backend='redis://47.102.153.238',
             include=['proj.tasks'])

app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()

