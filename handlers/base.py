#!/usr/bin/env python
# coding=utf-8

from tornado.web import RequestHandler
from db import news


class BaseHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
         super(BaseHandler, self).__init__(*argc, **argkw)
       
    @property
    def db(self):
        return self.application.db

    @property
    def news_model(self):
        return news.NewsModel(self.application.db)

    @property
    def email_model(self):
        return news.EmailModel(self.application.db)

