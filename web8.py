#!/usr/bin/env python
# _*_coding:utf-8_*_
import zipfile
import os
f = zipfile.ZipFile('archive.zip','w',zipfile.ZIP_DEFLATED)
startdir = "/home/pc7/bb"
for dirpath, dirnames, filenames in os.walk(startdir):
  for filename in filenames:
    f.write(os.path.join(dirpath, filename))
f.close()