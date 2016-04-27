# -*- coding: utf-8 -*-

LANG = 'en'

'''
* [中文](zh-cn)
* [English](en)
* [漢語](zh-tw)
'''

detail = u'''
<H3>RESTful API generator</H3>
<H3>Mock server</H3>
<H4></H4>
'''


project = {
    "name": "project",
    "version": "1.0",
    "description": "Demo",
    "title": "Demo",
    "detail": detail,
    "url_prefix": "/doc",
    "groups": [
        {
            "name": "groupA",
            "version": "1.0",
            "description": "Group A",
            "title": "Group A",
            "url_prefix": "/groupA"
        },

        {
            "name": "groupB",
            "version": "1.0",
            "description": "Group B",
            "title": "Group B",
            "url_prefix": "/groupB"
        }
    ]
}
