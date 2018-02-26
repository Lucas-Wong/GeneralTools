# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-02-26 
"""
import uuid
import getopt
import sys

class Create_Guid():

    New_Uuid = ''

    def Show_Version(self):
        print("Guid generator v1.0, by Lucas wang")

    def Show_Usage(self):
        self.Show_Version()
        print(
        '''
generate a new guid and printit in stdout.

Usage:
    createGuid [option]

    options:
        -v      get the version infomation
        -h      show the help infomation like this
        -u,-U   show guid in uppercase, default is uppercase
        -l,-L   show guid in lowercase
        -1      ake a UUID based on the host ID and current time
        -3      make a UUID using an MD5 hash of a namespace UUID and a name
        -4      make a random UUID
        -5      make a UUID using a SHA-1 hash of a namespace UUID and a name
        ''')

    def uuid1(self):
        self.New_Uuid = uuid.uuid1()

    def uuid3(self, str_name):
        self.New_Uuid = uuid.uuid3(uuid.NAMESPACE_DNS, str_name)

    def uuid4(self):
        self.New_Uuid = uuid.uuid4()

    def uuid5(self, str_name):
        self.New_Uuid = uuid.uuid5(uuid.NAMESPACE_DNS, str_name)

    def Getopt_Opts(self, opts):
        for o, a in opts:
            # print(o, '==', a)
            if o in ("-h", "--help"):
                self.Show_Usage()
            elif o in ("-v", "--version"):
                self.Show_Version()
            elif o == "-1":
                self.uuid1()
            elif o  == "-3" :
                if a is None:
                    a = 'ariix.com'
                self.uuid3(a)
            elif o == "-4" :
                self.uuid4()
            elif o == "-5" :
                if a is None:
                    a = 'ariix.com'
                self.uuid5(a)

        for o, a in opts:
            if o in ("-u", "-U"):
                print(self.New_Uuid.upper())
            elif o in ("-l", "-L"):
                print(self.New_Uuid)

    def Argv_Args(self, args):
        if args is None:
            print(args)

    def Main(self):
        # isUpper = True
        # act = 'uuid'

        try:
            opts, args = getopt.getopt(sys.argv[1:], "hvul1435", ["help", "output="])

            # print(opts)
            self.Getopt_Opts(opts)

            # print(args)
            self.Argv_Args(args)

        except getopt.GetoptError as ex:
            # print help information and exit:
            print(ex)
            print(''.center(50, "*"))
            # self.Show_Usage()
            sys.exit()

        # if '-u' in sys.argv: isUpper = True
        # if '-U' in sys.argv: isUpper = True
        # if '-l' in sys.argv: isUpper = False
        # if '-L' in sys.argv: isUpper = False
        # if '-v' in sys.argv: act = 'ver'
        # if '-h' in sys.argv: act = 'help'
        #
        # if act == 'uuid':
        #     result = str(uuid.uuid1())
        #     if isUpper:
        #         print(result.upper())
        #     else:
        #         print(result)
        # elif act == 'ver':
        #     self.Show_Version()
        # elif act == 'help':
        #     self.Show_Usage()

if __name__ == '__main__':
    test = Create_Guid()
    test.Main()