# -*- coding: utf-8 -*-

LANG = 'en'

'''
* [中文](zh-cn)
* [English](en)
* [漢語](zh-tw)
'''

detail = u'''
<H3>验证码微服务以RESTful API的形式对外提供短信验证码和多种形式的图灵验证码接口。</H3>

'''

'''
RESTful API
<H3>快速，方便的RESTful API文档生成工具</H3>
<H3>同时提供在线浏览和API Mock服务</H3>
<H4>注1： 本文档由DocFk生成</H4>
'''

project = {
    "name": "project",
    "version": "1.0",
    "description": u"验证码微服务",
    "title": u"验证码微服务简介",
    "detail": detail,
    "url_prefix": "/doc"
}

groups = [
    {
        "name": "sms",
        "version": "1.0",
        "description": u"短信验证码接口",
        "title": u"短信验证码接口",
        "url_prefix": "/api/sms"
    },

    {
        "name": "captcha",
        "version": "1.0",
        "description": u"图灵验证码接口",
        "title": u"图灵验证码接口",
        "url_prefix": "/api/captcha"
    }
]
