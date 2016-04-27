#!/usr/bin/env python


from contract import app
from flask.ext.script import Manager
from flask import url_for
import os
import subprocess

manager = Manager(app)


@manager.command
def help():
    usage = './manage.py runserver -p 7015'
    print(usage)


@manager.command
def url():
    with app.test_request_context():
        print(url_for('sms_api.require_sms_code'))


@manager.command
def init(lang='en'):
    dest_dir = 'contract/api'
    src_dir = 'examples/{}/api'.format(lang)
    if os.path.isdir(dest_dir):
        print('The directory {} existed, cancel copy.'.format(dest_dir))
        return

    if os.path.isdir(src_dir):
        s = 'cp -r {} {}'.format(src_dir, dest_dir)
        r = subprocess.call(s, shell=True)
        if r != 0:
            print('Copy directory failed, {}: {}'.format(r, s))
        print('Copy to {} from {}'.format(dest_dir, src_dir))
    else:
        print('Wrong lang name: {}'.format(lang))

    return


@manager.command
def urlmap():
    for a in app.url_map.iter_rules():
        print("endpoint %s" % a.endpoint)
        print("methods %s" %  (a.methods - set(['HEAD', 'OPTIONS'])))
        print("bind %s" % a.bind)
        print("rule %s" % a.rule)

    print(app.url_map)

if __name__ == '__main__':
    manager.run()
