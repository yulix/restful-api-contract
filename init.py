#!/usr/bin/env python

import os
import subprocess
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--lang', dest='lang', default='en')
    args = parser.parse_args()
    return args


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


if __name__ == '__main__':
    args = parse_args()
    init(args.lang)

