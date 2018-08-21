#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import json
import time
import datetime
import decimal

abspath = os.path.dirname(__file__)
os.chdir(abspath)
os.chdir('../../')
sys.path.append(os.getcwd())

from flask import current_app
from sqlalchemy import func, or_
from app import create_app
from app.ext import db
from app.utils.utils import strftime

def migrate_blog(record):
    title = record['title'].replace('/', ' ').replace('[', '【').replace(']', '】').replace(':', ' ')
    if not title:
        return

    content = record['content']
    create_time = record['date']

    title_path = "tools/blog/%s.md" % title
    f = open(title_path, "w")
    f.write("---\n")
    f.write("title: %s\n" % title)
    f.write("date: %s\n" % strftime(create_time))
    f.write("---\n")
    if "##" not in content:
        f.write("{% raw %}\n")
        f.write(content)
        f.write("{% endraw %}\n")
    else:
        f.write(content)

    f.close()

    print(title, 'success')

def main():
    records = db.engine.execute('select * from emlog_blog;')
    count = 0
    for record in records:
        migrate_blog(record)
        count += 1
    db.session.commit()
    print(count, 'success')

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        try:
            main()
        except:
            app.logger.exception('process fail')
