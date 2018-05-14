# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-02-06 
"""

import os
import glob
from xml.etree import ElementTree as ET

class File_operation(object):
    """
    File operation
    """

    names = ['iConn.CreateXmlTools.vshost.exe', 'AutoUpdater.dll', 'Newtonsoft.Json.dll',
                 'Oracle.ManagedDataAccess.dll', 'Renci.SshNet.dll', 'Renci.SshNet.xml', 'zxing.dll',
                 'Images/ARX_HK.png', 'Images/ARX_USA_201803.png']

    def __init__(self, path_name=r"http://172.16.1.81:8081/UpdateClient/", name_list=None):
        self.old_path_name = path_name

        if name_list is not None:
            self.names = name_list

    def remove_file(self, file_name_list):
        """
        Remove file
        :param file_name_list:
        :return:
        """
        print("glob".center(50, "="))
        print("Current Working Directory is " + os.getcwd())
        files = []

        for file_name in file_name_list:
            files += glob.glob(file_name)

        for file in files:
            try:
                os.remove(file)
            except IOError:
                print(file + " don't delete")
            else:
                print(file)

        print("glob".center(50, "="))

    def change_file(self, path_name, file_name='AutoupdateService', file_type='xml'):
        """
        Change file
        :param file_type:
        :param file_name:
        :param path_name:
        :return:
        """
        if file_type.strip().lower() == "xml":
            self.change_xml_file(file_name, path_name)

    def change_xml_file(self, file_name, path_name):
        """
        Change xml file
        :param file_name:
        :param path_name:
        :return:
        """
        tree = ET.parse(os.getcwd() + os.sep + file_name + ".xml")
        root = tree.getroot()

        # for item in root.getchildren():
        #     item.set("url", item.get('url').replace(self.old_path_name, path_name))
        #
        #     if item.get('path') in self.names:
        #         root.remove(item)
        for item in root.findall('file'):
            item.set("url", item.get('url').replace(self.old_path_name, path_name))

            if item.get('path') in self.names:
                root.remove(item)

        tree.write(os.getcwd() + os.sep + file_name + ".xml", encoding="utf-8")

if __name__ == '__main__':
    pass