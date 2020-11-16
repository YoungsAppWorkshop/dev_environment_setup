#!/usr/bin/env python3
from threading import thread


class BuckysMessenger(thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())


x = BuckysMessenger(name='Send Out messages')
y = BuckysMessenger(name='Receive messages')

x.start()
y.start()
