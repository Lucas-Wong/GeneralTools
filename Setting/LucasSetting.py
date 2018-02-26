# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-02-26 
"""

class Lucas_Setting(object):

    def __init__(self):
        pass

    def Show_Version(self):
        print("Verion number: 1.0, by Lucas wang")

    def Show_Usage(self):
        self.Show_Version()
        print(
        '''
generate a new setting and printit in stdout.

Usage:
     setting [option]

    options:
        -v      get the version infomation
        -h      show the help infomation like this
        -u,-U   show guid in uppercase, default is uppercase
        -l,-L   show guid in lowercase
        ''')

if __name__ == '__main__':
    setting = Lucas_Setting()
    setting.Show_Usage()