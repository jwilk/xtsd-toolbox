# encoding=UTF-8

# Copyright © 2019 Jakub Wilk <jwilk@jwilk.net>
# SPDX-License-Identifier: MIT

'''
xterm screendump helper functions
'''

import re

...  # Python 3 is required

def fix_color(s):
    match = re.match(r'^rgb[(](\d+[.]\d+)%, (\d+[.]\d+)%, (\d+[.]\d+)%[)]$', s)
    result = ['#']
    for i in range(1, 4):
        v = match.group(i)
        v = float(v)
        v = int(15 * v / 100.0)
        v = '{0:x}'.format(v)
        result += [v]
    return ''.join(result)

__all__ = ['fix_color']

# vim:ts=4 sts=4 sw=4 et
