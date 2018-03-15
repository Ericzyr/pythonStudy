#!/usr/bin/env python

import re
a = 'hello word'
strinfo = re.compile('word')
b = strinfo.sub('python', a)
print(b)