# -*- coding: GBK -*-

import sys
reload(sys)
sys.setdefaultencoding('GBK')

from qian import chouqian
import os
import logging
import random
import time
logging.basicConfig(
    level       = logging.INFO,
    format      = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt     = '%Y-%m-%d %H:%M:%S',
    filename    = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'CQHanlder.log'),
    filemode    = 'w+'
)
import CQSDK
last_time=time.strftime('%Y-%m-%d',time.localtime())
folder = os.path.exists("./data/app/xyz.shinnshi.chouqian")
if not folder:
    os.makedirs("./data/app/xyz.shinnshi.chouqian")
class CQHandler(object):
    def __init__(self):
        logging.info('__init__')
        
    def __del__(self):
        logging.info('__del__')
        
    def OnEvent_Enable(self):
        logging.info('OnEvent_Enable')

    def OnEvent_Disable(self):
        logging.info('OnEvent_Disable')

    def OnEvent_PrivateMsg(self, subType, sendTime, fromQQ, msg, font):
        global last_time
        logging.info('OnEvent_PrivateMsg: subType={0}, sendTime={1}, fromQQ={2}, msg={3}, font={4}'.format(subType, sendTime, fromQQ, msg, font))
        if msg == "��ǩ":
            try:
                folder = os.path.exists("./data/app/xyz.shinnshi.chouqian")
                if not folder:
                    os.makedirs("./data/app/xyz.shinnshi.chouqian")
                if not (os.path.exists("./data/app/xyz.shinnshi.chouqian/today.txt")):
                    with open("./data/app/xyz.shinnshi.chouqian/today.txt","w") as f:
                        f.write('��ǰ�ѳ飺\n')
                now_time = time.strftime('%Y-%m-%d',time.localtime())
                if last_time != now_time:
                    with open("./data/app/xyz.shinnshi.chouqian/today.txt","w") as f:
                        f.write('��ǰ�ѳ飺\n')
                        last_time = now_time
                with open("./data/app/xyz.shinnshi.chouqian/today.txt","r") as f:
                    today=[]
                    today=f.readlines()
                    qq = str(fromQQ)+"\n"
                    if  qq in today:
                        CQSDK.SendPrivateMsg(fromQQ, "������Ѿ������Ŷ������������~")
                        return
                id = random.randint(1,100)
                msg = chouqian(id).decode('UTF-8').encode('GBK')
                CQSDK.SendPrivateMsg(fromQQ, msg)
                with open("./data/app/xyz.shinnshi.chouqian/today.txt","a") as f:
                    f.write(str(fromQQ)+"\n")
            except Exception as e:
                logging.exception(e)
    def OnEvent_GroupMsg(self, subType, sendTime, fromGroup, fromQQ, fromAnonymous, msg, font):
        global last_time
        logging.info('OnEvent_GroupMsg: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, fromAnonymous={4}, msg={5}, font={6}'.format(subType, sendTime, fromGroup, fromQQ, fromAnonymous, msg, font))
        if msg == "��ǩ":
            try:
                folder = os.path.exists("./data/app/xyz.shinnshi.chouqian")
                if not folder:
                    os.makedirs("./data/app/xyz.shinnshi.chouqian")
                if not (os.path.exists("./data/app/xyz.shinnshi.chouqian/today.txt")):
                    with open("./data/app/xyz.shinnshi.chouqian/today.txt","w") as f:
                        f.write('��ǰ�ѳ飺\n')
                now_time = time.strftime('%Y-%m-%d',time.localtime())
                if last_time != now_time:
                    with open("./data/app/xyz.shinnshi.chouqian/today.txt","w") as f:
                        f.write('��ǰ�ѳ飺\n')
                        last_time = now_time
                with open("./data/app/xyz.shinnshi.chouqian/today.txt","r") as f:
                    today=[]
                    today=f.readlines()
                    qq = str(fromQQ)+"\n"
                    if  qq in today:
                        CQSDK.SendGroupMsg(fromGroup, "������Ѿ������Ŷ������������~")
                        return
                id = random.randint(1,100)
                msg = chouqian(id).decode('UTF-8').encode('GBK')
                CQSDK.SendGroupMsg(fromGroup, msg)
                with open("./data/app/xyz.shinnshi.chouqian/today.txt","a") as f:
                    f.write(str(fromQQ)+"\n")
            except Exception as e:
                logging.exception(e)