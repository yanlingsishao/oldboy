#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import paramiko
import sys
import threading

t = paramiko.Transport(('192.168.1.111', 22))
t.start_client()
t.auth_password('root', '123456')

chan = t.open_session()
chan.get_pty()
chan.invoke_shell()

#########
sys.stdout.write("Line-buffered terminal emulation. Press F6 or ^Z to send EOF.\r\n\r\n")


def writeall(sock):
    while True:
        data = sock.recv(256)
        if not data:
            sys.stdout.write('\r\n*** EOF ***\r\n\r\n')
            sys.stdout.flush()
            break


        sys.stdout.write(data)
        sys.stdout.flush()

        writer = threading.Thread(target=writeall, args=(chan,))
        writer.start()

        try:
            while True:
                d = sys.stdin.read(1)
                if not d:
                    break
                chan.send(d)
        except EOFError:
        # user hit ^Z or F6
            pass
#########
chan.close()
t.close()