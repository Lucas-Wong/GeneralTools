# -*- coding: utf-8 -*-
"""
-----------------------------------------------------
    File Name:        download_file
    Author:           Lucas.wang
    Date:             2018-11-23 13:06
    Description:      
-----------------------------------------------------
    Change Activity:  2018-11-23 13:06
    Description:      
----------------------------------------------------
"""
from urllib.request import urlopen
import sys

# @app.route('/file/download/<filename>', methods=['GET'])
# def file_download(filename):
#     def send_chunk():  # 流式读取
#         store_path = './upload/%s' % filename
#         with open(store_path, 'rb') as target_file:
#             while True:
#                 chunk = target_file.read(20 * 1024 * 1024)  # 每次读取20M
#                 if not chunk:
#                     break
#                 yield chunk
#
#     return Response(send_chunk(), content_type='application/octet-stream')


def download_big_file(url, target_file_name):
    """
        使用python核心库下载大文件
        ref: https://stackoverflow.com/questions/1517616/stream-large-binary-files-with-urllib2-to-file
    """
    # import sys
    # if sys.version_info > (2, 7):
        # Python 3
        # from urllib.request import urlopen
    # else:
        # Python 2
        # from urllib2 import urlopen

    response = urlopen(url)
    chunk = 20 * 1024 * 1024
    with open(target_file_name, 'wb') as f:
        while True:
            chunk = response.read(chunk)
            if not chunk:
                break
            f.write(chunk)