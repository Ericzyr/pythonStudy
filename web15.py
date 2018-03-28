#!/usr/bin/env python3
# -*-coding:utf-8-*-
import os
import zipfile, os

zipFile = zipfile.ZipFile(os.path.join(os.getcwd(), 'txt.zip'))
for file in zipFile.namelist():
    zipFile.extract(file, r'/home/pc7/pythonNote/55/search1/')
zipFile.close()


