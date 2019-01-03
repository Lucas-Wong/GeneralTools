# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-02-05 
"""

import paramiko

class SSHConnection(object):

    def __init__(self, host='172.16.1.215', port=22, username='tomcat', pwd='tomcat123'):
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self.__k = None

    def run(self):
        self.connect()
        pass
        self.close()

    def connect(self):
        transport = paramiko.Transport(self.host, self.port)
        transport.connect(username=self.username, password=self.pwd)
        self.__transport = transport

    def close(self):
        self.__transport.close()

    def cmd(self, command):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        result = stdout.read()
        return result

    def upload(self, local_path, target_path):
        # 连接，上传
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        # 将location.py 上传至服务器 /tmp/test.py
        sftp.put(local_path, target_path)

    def download(self, local_path, target_path):
        # 连接，上传
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        # 启动scp远程拷贝命令，实现将打包好的nginx日志复制到本地/home目录
        child = sftp.spawn('/usr/bin/scp', [user + "@" + ip + ':/data/nginx_access.tar.gz', '/home'])

if __name__ == '__main__':
    ssh = SSHConnection()
    ssh.connect()
    r1 = ssh.cmd('df')
    print(r1.decode())
    ssh.upload('class12.py', "test.py")
    ssh.close()