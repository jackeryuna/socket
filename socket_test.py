#coding=utf-8

import threading
import concurrent.futures

from mq import (
    DMSMQ
    , DMSMQProcessor
)
class DMSSocketServer(threading.Thread, DMSMQProcessor):
    HOST = 'localhost'
    PORT = 47777
    SOCKET_PARSE_THREAD_NUM = 4
    def __init__(self, mqserver, mainProp, host = HOST, port = PORT):
        super().__init__()
        self.host = host
        self.port = port
        self.mqserver = mqserver
        self.mainProp = mainProp
        self.parseThreadPool = concurrent.futures.ThreadPoolExecutor(self.SOCKET_PARSE_THREAD_NUM)

